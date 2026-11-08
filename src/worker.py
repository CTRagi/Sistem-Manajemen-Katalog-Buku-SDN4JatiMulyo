import hashlib
import io
import re
import time
from datetime import date, datetime, timedelta, timezone
from functools import wraps

import xlsxwriter
from flask import Flask, Response, abort, g, redirect, render_template, request, url_for
from itsdangerous import BadSignature, URLSafeTimedSerializer
from jinja2 import DictLoader
from pyodide.ffi import run_sync
from werkzeug.security import check_password_hash, generate_password_hash
from workers import wsgi

from tpl import T
import hashfix

app = Flask(__name__, static_folder=None)
app.jinja_loader = DictLoader(T)

COOKIE, MAX_AGE = "sid", 8 * 3600
HASH = "pbkdf2:sha256:100000"       # turunkan jika kena batas CPU Workers
TZ = timezone(timedelta(hours=7))   # WIB; ganti jika WITA/WIT
PUBLIC = {"login", "setup", "landing"}
FIELDS = ("kode", "judul", "pengarang", "penerbit", "tahun", "kategori", "rak")
TIPE = ("siswa", "guru", "lainnya")
PILL = {"Kembali": "ok", "Dipinjam": "warn", "Terlambat": "bad"}
PER_HAL, PER_ANGGOTA = 24, 50
BATAS_LOGIN = {"up": 5, "ip": 20}   # gagal beruntun per (pengguna+IP) dan per IP
JENDELA = KUNCI = 15 * 60           # detik: jendela hitung gagal & lama terkunci
BUKU_SQL = ("SELECT b.*, b.stok - (SELECT COUNT(*) FROM transaksi t "
            "WHERE t.buku_id = b.id AND t.tgl_kembali IS NULL) AS tersedia FROM buku b")


# ---------- helper D1 (Flask sinkron -> D1 async lewat run_sync) ----------
def env():
    return request.environ["workers.env"]

def _py(v):
    return v.to_py() if hasattr(v, "to_py") else v

def _stmt(sql, args):
    st = env().DB.prepare(sql)
    return st.bind(*args) if args else st

def sel(sql, *args):
    res = _py(run_sync(_stmt(sql, args).all()))
    rows = res["results"] if isinstance(res, dict) else res.results
    return list(_py(rows))

def run(sql, *args):
    run_sync(_stmt(sql, args).run())

def today():
    return datetime.now(TZ).date()

@app.template_filter("rupiah")
def rupiah(n):
    return "Rp " + f"{int(n or 0):,}".replace(",", ".")

def tautan(endpoint, base, **kw):
    """URL dengan parameter query yang tidak kosong (untuk filter & halaman)."""
    return url_for(endpoint, **{k: v for k, v in {**base, **kw}.items() if v})


# ---------- pengaturan & denda ----------
def cfg_muat():
    cfg = {"masa_pinjam": 7, "denda_per_hari": 500, "denda_maks": 0}
    for r in sel("SELECT kunci, nilai FROM pengaturan"):
        if r["kunci"] in cfg and str(r["nilai"]).isdigit():
            cfg[r["kunci"]] = int(r["nilai"])
    return cfg

def hitung_denda(tempo, kembali, cfg):
    akhir = date.fromisoformat(kembali) if kembali else today()
    telat = max(0, (akhir - date.fromisoformat(tempo)).days)
    denda = telat * cfg["denda_per_hari"]
    if cfg["denda_maks"] > 0:
        denda = min(denda, cfg["denda_maks"])
    return telat, denda


# ---------- sesi, CSRF, pembatasan login ----------
def signer(salt="perpus-sd"):
    return URLSafeTimedSerializer(env().SECRET_KEY, salt=salt)

def sidik(pw_hash):
    return hashlib.sha256(pw_hash.encode()).hexdigest()[:16]

def beri_sesi(resp, uid, pw_hash):
    # sidik hash sandi ikut di cookie: ganti/reset sandi otomatis mematikan sesi lama
    resp.set_cookie(COOKIE, signer().dumps([uid, sidik(pw_hash)]), max_age=MAX_AGE,
                    httponly=True, secure=request.is_secure, samesite="Lax")
    return resp

def csrf_uid():
    u = g.get("user")
    return u["id"] if u else 0

def csrf_ok():
    try:
        return signer("perpus-csrf").loads(request.form.get("csrf_token", ""), max_age=MAX_AGE) == csrf_uid()
    except BadSignature:
        return False

FORM_POST = re.compile(r'(<form\b[^>]*\bmethod="post"[^>]*>)', re.I)

@app.after_request
def sisip_csrf(resp):
    """Sisipkan token CSRF ke setiap <form method="post"> di halaman HTML."""
    if resp.mimetype == "text/html" and not resp.direct_passthrough:
        html = resp.get_data(as_text=True)
        if "<form" in html:
            tok = f'<input type="hidden" name="csrf_token" value="{signer("perpus-csrf").dumps(csrf_uid())}">'
            resp.set_data(FORM_POST.sub(lambda m: m.group(1) + tok, html))
    return resp

def kunci_login(user):
    ip = (request.headers.get("CF-Connecting-IP") or request.remote_addr or "?")[:64]
    return f"up:{user}|{ip}", f"ip:{ip}"

def menit_terkunci(keys):
    now = int(time.time())
    rows = sel("SELECT terkunci_sampai FROM percobaan_login WHERE kunci IN (?, ?)", *keys)
    return max([(r["terkunci_sampai"] - now + 59) // 60 for r in rows if r["terkunci_sampai"] > now], default=0)

def catat_gagal(kunci):
    now, maks = int(time.time()), BATAS_LOGIN[kunci.split(":")[0]]
    r = sel("SELECT gagal, mulai FROM percobaan_login WHERE kunci = ?", kunci)
    n, mulai = (r[0]["gagal"] + 1, r[0]["mulai"]) if r and now - r[0]["mulai"] <= JENDELA else (1, now)
    run("INSERT INTO percobaan_login (kunci, gagal, mulai, terkunci_sampai) VALUES (?, ?, ?, ?) "
        "ON CONFLICT(kunci) DO UPDATE SET gagal = excluded.gagal, mulai = excluded.mulai, "
        "terkunci_sampai = excluded.terkunci_sampai", kunci, n, mulai, now + KUNCI if n >= maks else 0)

@app.before_request
def guard():
    g.user = None
    tok = request.cookies.get(COOKIE)
    if tok:
        try:
            uid, fp = signer().loads(tok, max_age=MAX_AGE)
            rows = sel("SELECT id, username, nama, role, password_hash FROM users WHERE id = ? AND aktif = 1", uid)
            if rows and sidik(rows[0].pop("password_hash")) == fp:
                g.user = rows[0]
        except (BadSignature, TypeError, ValueError):
            pass
    if request.method == "POST" and not csrf_ok():
        return Response("Token keamanan formulir tidak valid atau sudah kedaluwarsa. "
                        "Muat ulang halaman, lalu coba lagi.", 400)
    if g.user or request.endpoint in PUBLIC:
        return None
    return redirect(url_for("login" if sel("SELECT 1 AS x FROM users LIMIT 1") else "setup"))

def admin_only(fn):
    @wraps(fn)
    def inner(*a, **k):
        if g.user["role"] != "admin":
            abort(403)
        return fn(*a, **k)
    return inner

@app.route("/setup", methods=["GET", "POST"])
def setup():
    if sel("SELECT 1 AS x FROM users LIMIT 1"):
        return redirect(url_for("login"))
    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        user = request.form.get("username", "").strip().lower()
        pw = request.form.get("password", "")
        if not nama or not user or len(pw) < 8:
            return render_template("setup.html", err="Lengkapi data; kata sandi minimal 8 karakter."), 400
        run("INSERT INTO users (username, nama, password_hash, role) VALUES (?, ?, ?, 'admin')",
            user, nama, generate_password_hash(pw, method=HASH))
        return redirect(url_for("login", ok="Akun admin dibuat. Silakan masuk."))
    return render_template("setup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username", "").strip().lower()[:64]
        keys = kunci_login(user)
        pesan = "Terlalu banyak percobaan gagal. Coba lagi dalam {} menit."
        if menit := menit_terkunci(keys):
            return render_template("login.html", err=pesan.format(menit)), 429
        rows = sel("SELECT id, password_hash FROM users WHERE username = ? AND aktif = 1", user)
        if rows and check_password_hash(rows[0]["password_hash"], request.form.get("password", "")):
            run("DELETE FROM percobaan_login WHERE kunci = ?", keys[0])
            return beri_sesi(redirect(url_for("buku_list")), rows[0]["id"], rows[0]["password_hash"])
        for k in keys:
            catat_gagal(k)
        menit = menit_terkunci(keys)
        return render_template("login.html",
                               err=pesan.format(menit) if menit else "Nama pengguna atau kata sandi salah."), 401
    return render_template("login.html")

@app.post("/logout")
def logout():
    resp = redirect(url_for("landing"))
    resp.delete_cookie(COOKIE)
    return resp

@app.route("/akun", methods=["GET", "POST"])
def akun():
    if request.method == "POST":
        lama, baru, ulang = (request.form.get(k, "") for k in ("lama", "baru", "ulang"))
        h = sel("SELECT password_hash FROM users WHERE id = ?", g.user["id"])[0]["password_hash"]
        if not check_password_hash(h, lama):
            err = "Kata sandi lama salah."
        elif len(baru) < 8:
            err = "Kata sandi baru minimal 8 karakter."
        elif baru != ulang:
            err = "Konfirmasi kata sandi tidak sama."
        elif baru == lama:
            err = "Kata sandi baru harus berbeda dari yang lama."
        else:
            h = generate_password_hash(baru, method=HASH)
            run("UPDATE users SET password_hash = ? WHERE id = ?", h, g.user["id"])
            return beri_sesi(redirect(url_for("akun", ok="Kata sandi diganti. Perangkat lain otomatis keluar.")),
                             g.user["id"], h)
        return render_template("akun.html", err=err), 400
    return render_template("akun.html")


# ---------- halaman publik: daftar buku tersedia ----------
@app.get("/")
def landing():
    q, kat = request.args.get("q", "").strip(), request.args.get("kat", "").strip()
    semua = request.args.get("tampil") == "semua"
    hal = max(1, request.args.get("hal", 1, type=int))
    where, args = " WHERE 1 = 1", []
    if q:
        where += " AND (judul LIKE ? OR pengarang LIKE ? OR kode LIKE ? OR kategori LIKE ?)"
        args += [f"%{q}%"] * 4
    if kat:
        where += " AND kategori = ?"
        args.append(kat)
    if not semua:
        where += " AND tersedia > 0"
    src = f"({BUKU_SQL})"
    total = sel(f"SELECT COUNT(*) AS n FROM {src}{where}", *args)[0]["n"]
    buku = sel(f"SELECT * FROM {src}{where} ORDER BY judul LIMIT ? OFFSET ?", *args, PER_HAL, (hal - 1) * PER_HAL)
    for b in buku:
        b["hue"] = int(hashlib.sha256(b["kode"].encode()).hexdigest()[:4], 16) % 360
    base = {"q": q, "kat": kat, "tampil": "semua" if semua else ""}
    kats = sel("SELECT kategori, COUNT(*) AS n FROM buku WHERE kategori != '' GROUP BY kategori ORDER BY kategori")
    for k in kats:
        k["href"] = tautan("landing", base, kat=k["kategori"])
    hal_maks = max(1, -(-total // PER_HAL))
    return render_template(
        "landing.html", buku=buku, total=total, q=q, kat=kat, semua=semua, hal=hal, hal_maks=hal_maks, kats=kats,
        semua_kat=tautan("landing", base, kat=""), ganti_tampil=tautan("landing", base, tampil="" if semua else "semua"),
        prev=tautan("landing", base, hal=hal - 1) if hal > 1 else "",
        next=tautan("landing", base, hal=hal + 1) if hal < hal_maks else "",
        belum_setup=not sel("SELECT 1 AS x FROM users LIMIT 1"))


# ---------- excel ----------
def xlsx_response(sheet, head, rows, widths, nama):
    buf = io.BytesIO()
    wb = xlsxwriter.Workbook(buf, {"in_memory": True})
    ws = wb.add_worksheet(sheet)
    ws.write_row(0, 0, head, wb.add_format({"bold": True, "bg_color": "#DBEAFE", "border": 1}))
    for i, r in enumerate(rows, 1):
        ws.write_row(i, 0, [i, *r])
    for c, w in enumerate(widths):
        ws.set_column(c, c, w)
    ws.freeze_panes(1, 0)
    ws.autofilter(0, 0, max(len(rows), 1), len(head) - 1)
    wb.close()
    return Response(buf.getvalue(),
                    mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    headers={"Content-Disposition": f'attachment; filename="{nama}-{today()}.xlsx"'})


# ---------- buku ----------
def buku_rows(cari=""):
    sql, args = BUKU_SQL, []
    if cari:
        sql += " WHERE b.judul LIKE ? OR b.pengarang LIKE ? OR b.kode LIKE ?"
        args = [f"%{cari}%"] * 3
    return sel(sql + " ORDER BY b.judul", *args)

@app.get("/buku")
def buku_list():
    cari = request.args.get("q", "").strip()
    return render_template("buku.html", buku=buku_rows(cari), cari=cari)

@app.get("/buku/export.xlsx")
def export_buku():
    rows = buku_rows(request.args.get("q", "").strip())
    head = ["No", "Kode", "Judul", "Pengarang", "Penerbit", "Tahun", "Kategori", "Rak",
            "Jumlah Eksemplar", "Dipinjam", "Tersedia"]
    data = [[b["kode"], b["judul"], b["pengarang"], b["penerbit"], b["tahun"], b["kategori"], b["rak"],
             b["stok"], b["stok"] - b["tersedia"], b["tersedia"]] for b in rows]
    return xlsx_response("Buku", head, data, [5, 12, 38, 22, 22, 8, 16, 8, 18, 10, 10], "data-buku")

def simpan_buku(bid=None):
    f = {k: request.form.get(k, "").strip() for k in FIELDS}
    try:
        f["stok"] = max(0, int(request.form.get("stok", "1")))
    except ValueError:
        f["stok"] = 1
    f["id"] = bid
    err = None
    if not f["kode"] or not f["judul"]:
        err = "Kode dan judul wajib diisi."
    elif sel("SELECT id FROM buku WHERE kode = ? AND id != ?", f["kode"], bid or 0):
        err = "Kode buku sudah dipakai."
    elif bid:
        n = sel("SELECT COUNT(*) AS n FROM transaksi WHERE buku_id = ? AND tgl_kembali IS NULL", bid)[0]["n"]
        if f["stok"] < n:
            err = f"Jumlah eksemplar tidak boleh kurang dari {n} (sedang dipinjam)."
    if err:
        return render_template("buku_form.html", b=f, err=err), 400
    vals = [f[k] for k in FIELDS] + [f["stok"]]
    if bid:
        run("UPDATE buku SET kode=?, judul=?, pengarang=?, penerbit=?, tahun=?, kategori=?, rak=?, stok=? "
            "WHERE id=?", *vals, bid)
        return redirect(url_for("buku_list", ok="Buku disimpan."))
    run("INSERT INTO buku (kode, judul, pengarang, penerbit, tahun, kategori, rak, stok) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", *vals)
    return redirect(url_for("buku_baru", ok=f"Buku “{f['judul']}” disimpan. Silakan isi buku berikutnya."))

@app.route("/buku/baru", methods=["GET", "POST"])
def buku_baru():
    if request.method == "POST":
        return simpan_buku()
    return render_template("buku_form.html", b={"stok": 1})

@app.route("/buku/<int:id>/ubah", methods=["GET", "POST"])
def buku_ubah(id):
    if request.method == "POST":
        return simpan_buku(id)
    rows = sel("SELECT * FROM buku WHERE id = ?", id)
    if not rows:
        abort(404)
    return render_template("buku_form.html", b=rows[0])

@app.post("/buku/<int:id>/hapus")
def buku_hapus(id):
    if sel("SELECT 1 AS x FROM transaksi WHERE buku_id = ? LIMIT 1", id):
        return redirect(url_for("buku_list",
                                err="Buku punya riwayat transaksi, tidak bisa dihapus. Ubah jumlah eksemplar menjadi 0."))
    run("DELETE FROM buku WHERE id = ?", id)
    return redirect(url_for("buku_list", ok="Buku dihapus."))


# ---------- anggota ----------
@app.get("/anggota")
def anggota_list():
    cari = request.args.get("q", "").strip()
    hal = max(1, request.args.get("hal", 1, type=int))
    where, args = "", []
    if cari:
        where, args = " WHERE nama LIKE ? OR nomor LIKE ? OR kelas LIKE ?", [f"%{cari}%"] * 3
    total = sel(f"SELECT COUNT(*) AS n FROM anggota{where}", *args)[0]["n"]
    rows = sel(f"SELECT * FROM anggota{where} ORDER BY aktif DESC, nama LIMIT ? OFFSET ?",
               *args, PER_ANGGOTA, (hal - 1) * PER_ANGGOTA)
    hal_maks = max(1, -(-total // PER_ANGGOTA))
    return render_template("anggota.html", rows=rows, cari=cari, total=total, hal=hal, hal_maks=hal_maks,
                           prev=tautan("anggota_list", {"q": cari}, hal=hal - 1) if hal > 1 else "",
                           next=tautan("anggota_list", {"q": cari}, hal=hal + 1) if hal < hal_maks else "")

def simpan_anggota(aid=None):
    f = {k: request.form.get(k, "").strip() for k in ("nomor", "nama", "kelas", "tipe")}
    f["id"] = aid
    if f["tipe"] not in TIPE:
        f["tipe"] = "siswa"
    err = None
    if not f["nomor"] or not f["nama"]:
        err = "Nomor anggota dan nama wajib diisi."
    elif sel("SELECT id FROM anggota WHERE nomor = ? AND id != ?", f["nomor"], aid or 0):
        err = "Nomor anggota sudah dipakai."
    if err:
        return render_template("anggota_form.html", a=f, err=err), 400
    vals = [f["nomor"], f["nama"], f["kelas"], f["tipe"]]
    if aid:
        run("UPDATE anggota SET nomor=?, nama=?, kelas=?, tipe=? WHERE id=?", *vals, aid)
        return redirect(url_for("anggota_list", ok="Anggota disimpan."))
    run("INSERT INTO anggota (nomor, nama, kelas, tipe) VALUES (?, ?, ?, ?)", *vals)
    return redirect(url_for("anggota_baru", ok=f"Anggota “{f['nama']}” disimpan. Silakan isi anggota berikutnya."))

@app.route("/anggota/baru", methods=["GET", "POST"])
def anggota_baru():
    if request.method == "POST":
        return simpan_anggota()
    return render_template("anggota_form.html", a={"tipe": "siswa"})

@app.route("/anggota/<int:id>/ubah", methods=["GET", "POST"])
def anggota_ubah(id):
    if request.method == "POST":
        return simpan_anggota(id)
    rows = sel("SELECT * FROM anggota WHERE id = ?", id)
    if not rows:
        abort(404)
    return render_template("anggota_form.html", a=rows[0])

@app.post("/anggota/<int:id>/aktif")
def anggota_aktif(id):
    run("UPDATE anggota SET aktif = 1 - aktif WHERE id = ?", id)
    return redirect(url_for("anggota_list", ok="Status anggota diubah."))


# ---------- peminjaman, pengembalian, denda ----------
@app.route("/pinjam", methods=["GET", "POST"])
def pinjam():
    cfg = cfg_muat()
    if request.method == "POST":
        f = request.form
        bid, aid, tempo = f.get("buku_id", type=int), f.get("anggota_id", type=int), f.get("jatuh_tempo", "")
        try:
            date.fromisoformat(tempo)
        except ValueError:
            tempo = ""
        b = sel(BUKU_SQL + " WHERE b.id = ?", bid) if bid else []
        a = sel("SELECT nama, kelas FROM anggota WHERE id = ? AND aktif = 1", aid) if aid else []
        if not (b and a and tempo):
            return redirect(url_for("pinjam", err="Pilih buku dan anggota dari daftar, lalu tentukan batas pengembalian."))
        if b[0]["tersedia"] < 1:
            return redirect(url_for("pinjam", err="Semua eksemplar buku ini sedang dipinjam."))
        run("INSERT INTO transaksi (buku_id, anggota_id, peminjam, kelas, tgl_pinjam, tgl_jatuh_tempo, petugas) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)", bid, aid, a[0]["nama"], a[0]["kelas"], str(today()), tempo, g.user["nama"])
        return redirect(url_for("transaksi", ok=f"Peminjaman “{b[0]['judul']}” oleh {a[0]['nama']} dicatat."))
    pilih = request.args.get("buku", type=int)
    buku_peta = {f"{b['judul']} ({b['kode']}), tersedia {b['tersedia']}": b["id"]
                 for b in sel(BUKU_SQL + " ORDER BY b.judul") if b["tersedia"] > 0}
    daftar = sel("SELECT id, nomor, nama, kelas FROM anggota WHERE aktif = 1 ORDER BY nama")
    peta = {f"{a['nama']} ({a['kelas'] or '-'}) {a['nomor']}": a["id"] for a in daftar}
    return render_template("pinjam.html", buku_peta=buku_peta, peta=peta,
                           pilih_label=next((k for k, v in buku_peta.items() if v == pilih), ""),
                           jatuh_tempo=str(today() + timedelta(days=cfg["masa_pinjam"])))

def transaksi_rows(status="", cari=""):
    sql = ("SELECT t.*, b.kode, b.judul, a.nomor FROM transaksi t JOIN buku b ON b.id = t.buku_id "
           "LEFT JOIN anggota a ON a.id = t.anggota_id WHERE 1 = 1")
    args = []
    if status == "dipinjam":
        sql += " AND t.tgl_kembali IS NULL"
    elif status == "kembali":
        sql += " AND t.tgl_kembali IS NOT NULL"
    elif status == "denda":
        sql += " AND t.denda > 0 AND t.denda_lunas = 0"
    if cari:
        sql += " AND (t.peminjam LIKE ? OR b.judul LIKE ? OR b.kode LIKE ? OR a.nomor LIKE ?)"
        args = [f"%{cari}%"] * 4
    cfg, hari = cfg_muat(), str(today())
    rows = sel(sql + " ORDER BY t.id DESC", *args)
    for r in rows:
        r["status"] = ("Kembali" if r["tgl_kembali"] else
                       "Terlambat" if r["tgl_jatuh_tempo"] < hari else "Dipinjam")
        r["css"] = PILL[r["status"]]
        r["telat"], berjalan = hitung_denda(r["tgl_jatuh_tempo"], r["tgl_kembali"], cfg)
        r["denda_now"] = r["denda"] if r["tgl_kembali"] else berjalan
    return rows

@app.get("/transaksi")
def transaksi():
    status, cari = request.args.get("status", ""), request.args.get("q", "").strip()
    return render_template("transaksi.html", rows=transaksi_rows(status, cari), status=status, cari=cari)

@app.post("/transaksi/<int:id>/kembali")
def kembali(id):
    t = sel("SELECT tgl_jatuh_tempo FROM transaksi WHERE id = ? AND tgl_kembali IS NULL", id)
    if not t:
        return redirect(url_for("transaksi", err="Transaksi tidak ditemukan atau sudah dikembalikan."))
    telat, denda = hitung_denda(t[0]["tgl_jatuh_tempo"], None, cfg_muat())
    run("UPDATE transaksi SET tgl_kembali = ?, denda = ? WHERE id = ? AND tgl_kembali IS NULL",
        str(today()), denda, id)
    ok = "Pengembalian dicatat." + (f" Terlambat {telat} hari, denda {rupiah(denda)}." if denda else "")
    return redirect(url_for("transaksi", ok=ok, status=request.form.get("status", "")))

@app.post("/transaksi/<int:id>/denda")
def denda_aksi(id):
    aksi = request.form.get("aksi")
    if aksi == "lunas":
        run("UPDATE transaksi SET denda_lunas = 1 WHERE id = ? AND denda > 0 AND tgl_kembali IS NOT NULL", id)
        ok = "Denda ditandai lunas."
    elif aksi == "bebas":
        run("UPDATE transaksi SET denda = 0, denda_lunas = 0 WHERE id = ? AND tgl_kembali IS NOT NULL", id)
        ok = "Denda dibebaskan."
    else:
        abort(400)
    return redirect(url_for("transaksi", ok=ok, status=request.form.get("status", "")))

@app.get("/transaksi/export.xlsx")
def export_xlsx():
    rows = transaksi_rows(request.args.get("status", ""), request.args.get("q", "").strip())
    head = ["No", "Kode Buku", "Judul", "No. Anggota", "Peminjam", "Kelas", "Tgl Pinjam", "Batas Kembali",
            "Tgl Kembali", "Status", "Terlambat (hari)", "Denda (Rp)", "Status Denda", "Petugas"]

    def status_denda(r):
        if not r["denda_now"]:
            return ""
        return ("Lunas" if r["denda_lunas"] else "Belum lunas") if r["tgl_kembali"] else "Berjalan"

    data = [[r["kode"], r["judul"], r["nomor"] or "", r["peminjam"], r["kelas"], r["tgl_pinjam"],
             r["tgl_jatuh_tempo"], r["tgl_kembali"] or "", r["status"], r["telat"], r["denda_now"],
             status_denda(r), r["petugas"]] for r in rows]
    return xlsx_response("Transaksi", head, data, [5, 12, 36, 12, 18, 8, 13, 13, 13, 12, 14, 12, 14, 16], "transaksi")


# ---------- kelola pengguna & pengaturan (admin) ----------
@app.get("/pengguna")
@admin_only
def pengguna():
    return render_template("pengguna.html",
                           users=sel("SELECT id, username, nama, role, aktif FROM users ORDER BY id"))

@app.post("/pengguna/baru")
@admin_only
def pengguna_baru():
    f = request.form
    user, nama = f.get("username", "").strip().lower(), f.get("nama", "").strip()
    pw, role = f.get("password", ""), f.get("role", "pustakawan")
    if not user or not nama or len(pw) < 8 or role not in ("admin", "pustakawan"):
        return redirect(url_for("pengguna", err="Lengkapi data; kata sandi minimal 8 karakter."))
    if sel("SELECT 1 AS x FROM users WHERE username = ?", user):
        return redirect(url_for("pengguna", err="Nama pengguna sudah dipakai."))
    run("INSERT INTO users (username, nama, password_hash, role) VALUES (?, ?, ?, ?)",
        user, nama, generate_password_hash(pw, method=HASH), role)
    return redirect(url_for("pengguna", ok="Pengguna ditambahkan."))

@app.post("/pengguna/<int:id>/aktif")
@admin_only
def pengguna_aktif(id):
    if id == g.user["id"]:
        return redirect(url_for("pengguna", err="Tidak bisa menonaktifkan akun sendiri."))
    run("UPDATE users SET aktif = 1 - aktif WHERE id = ?", id)
    return redirect(url_for("pengguna", ok="Status pengguna diubah."))

@app.post("/pengguna/<int:id>/reset")
@admin_only
def pengguna_reset(id):
    pw = request.form.get("password", "")
    if len(pw) < 8:
        return redirect(url_for("pengguna", err="Kata sandi minimal 8 karakter."))
    run("UPDATE users SET password_hash = ? WHERE id = ?", generate_password_hash(pw, method=HASH), id)
    return redirect(url_for("pengguna", ok="Kata sandi diganti."))

BATAS = {"masa_pinjam": (1, 90), "denda_per_hari": (0, 100000), "denda_maks": (0, 10000000)}

@app.route("/pengaturan", methods=["GET", "POST"])
@admin_only
def pengaturan():
    if request.method == "POST":
        vals = {k: request.form.get(k, "").strip() for k in BATAS}
        if any(not v.isdigit() or not BATAS[k][0] <= int(v) <= BATAS[k][1] for k, v in vals.items()):
            return render_template("pengaturan.html", cfg=cfg_muat(),
                                   err="Isi semua kolom dengan angka yang wajar (masa pinjam 1-90 hari)."), 400
        for k, v in vals.items():
            run("INSERT INTO pengaturan (kunci, nilai) VALUES (?, ?) "
                "ON CONFLICT(kunci) DO UPDATE SET nilai = excluded.nilai", k, v)
        return redirect(url_for("pengaturan", ok="Pengaturan disimpan."))
    return render_template("pengaturan.html", cfg=cfg_muat())


Default = wsgi.entrypoint(app)