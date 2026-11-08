STYLE = """
:root{--brand:#2563eb;--ink:#1f2937;--mut:#6b7280;--line:#e5e7eb;--ok:#15803d;--warn:#b45309;--bad:#b91c1c}
*{box-sizing:border-box}
body{margin:0;background:#f5f7fb;color:var(--ink);font:16px/1.55 system-ui,"Segoe UI",Roboto,sans-serif}
nav{background:var(--brand);display:flex;flex-wrap:wrap;gap:4px;align-items:center;padding:8px 16px;color:#fff}
nav .brand{margin-right:12px;font-size:18px;font-weight:700}
nav a,nav button{color:#fff;text-decoration:none;padding:8px 12px;border-radius:8px;background:none;border:0;font:inherit;cursor:pointer}
nav a:hover,nav button:hover{background:rgba(255,255,255,.2)}
nav form{margin:0}.sp{flex:1}
main{max-width:1000px;margin:24px auto;padding:0 16px}
h1,h2{margin:0 0 12px}h1{font-size:24px}
.bar{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:12px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px}
.narrow{max-width:520px;margin:0 auto}.scroll{overflow-x:auto;padding:0}
table{width:100%;border-collapse:collapse}
th,td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:13px;color:var(--mut);text-transform:uppercase}small{color:var(--mut)}
label{display:block;margin-bottom:14px;font-weight:600}
input,select{display:block;width:100%;margin-top:6px;padding:11px 12px;font:inherit;border:1px solid #cbd5e1;border-radius:8px;background:#fff}
input:focus,select:focus,a:focus-visible,button:focus-visible{outline:3px solid #bfdbfe;border-color:var(--brand)}
.btn{display:inline-block;padding:10px 16px;border:0;border-radius:8px;background:var(--brand);color:#fff;font:inherit;font-weight:600;text-decoration:none;cursor:pointer}
.ghost{background:#e0e7ff;color:#1e3a8a}.danger{background:#fee2e2;color:var(--bad)}.sm{padding:6px 10px;font-size:14px}
.search{display:flex;gap:8px;margin-bottom:16px}.search input{flex:1;margin:0}.search select{width:auto;margin:0}
.row{display:flex;gap:10px}.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.act{white-space:nowrap}.act form{display:inline}
.act .inl{display:inline-flex;gap:6px}.inl input{width:130px;margin:0;padding:6px 8px}
.pill{padding:2px 10px;border-radius:99px;font-size:14px;font-weight:600}
.ok{background:#dcfce7;color:var(--ok)}.warn{background:#fef3c7;color:var(--warn)}.bad{background:#fee2e2;color:var(--bad)}
.msg{padding:12px 16px;border-radius:8px;margin-bottom:16px;font-weight:600}.msg a{color:inherit}
.empty{text-align:center;color:var(--mut);padding:32px}
.hint{color:var(--mut);margin:-6px 0 14px;font-size:14px}
.pager{display:flex;gap:12px;align-items:center;justify-content:center;margin:24px 0}
.hero{padding:8px 0 4px}
.hero h1{font:800 clamp(28px,5vw,40px)/1.15 "Trebuchet MS","Segoe UI",system-ui,sans-serif;color:#14213d;margin:0 0 6px}
.hero p{margin:0 0 16px;color:var(--mut);max-width:60ch}
.big{display:flex;gap:8px;max-width:640px}
.big input{flex:1;margin:0;padding:15px 18px;font-size:18px;border:2px solid #c7d7f5;border-radius:14px}
.big .btn{padding:0 26px;font-size:18px;border-radius:14px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 8px}
.chip{padding:6px 14px;border-radius:99px;background:#fff;border:2px solid #c7d7f5;color:#1e3a8a;text-decoration:none;font-weight:700}
.chip.on{background:#1e3a8a;border-color:#1e3a8a;color:#fff}
.hasil{margin:8px 0 18px;color:var(--mut)}.hasil a{color:#1e3a8a;font-weight:700}
.rak{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:20px}
.buku{position:relative;display:flex;flex-direction:column;justify-content:flex-end;gap:2px;aspect-ratio:3/4;padding:14px 12px 14px 18px;overflow:hidden;color:#fff;
background:hsl(var(--h) 55% 30%);border-left:10px solid hsl(var(--h) 55% 21%);border-radius:5px 14px 14px 5px}
.buku b{font:800 18px/1.2 "Trebuchet MS","Segoe UI",system-ui,sans-serif;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.buku small{color:rgba(255,255,255,.88);font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.buku small.info{white-space:normal}
.stiker{position:absolute;top:10px;right:10px;width:50px;height:50px;border-radius:50%;display:grid;place-items:center;text-align:center;
font-weight:800;font-size:14px;line-height:1.05;background:#fcd34d;color:#3b2f00;transform:rotate(8deg)}
.stiker.habis{background:#e2e8f0;color:#475569}
@media(max-width:480px){nav .brand{margin-right:0;font-size:17px}}
"""

T = {
"base.html": """<!doctype html>
<html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Perpustakaan SD</title><style>""" + STYLE + """</style></head><body>
<nav><a class="brand" href="{{ url_for('landing') }}">📚 Perpustakaan SDN 4 Jati Mulyo</a>
{% if g.user %}
<a href="{{ url_for('buku_list') }}">Buku</a>
<a href="{{ url_for('anggota_list') }}">Anggota</a>
<a href="{{ url_for('pinjam') }}">Pinjam</a>
<a href="{{ url_for('transaksi') }}">Transaksi</a>
{% if g.user.role == 'admin' %}<a href="{{ url_for('pengguna') }}">Pengguna</a><a href="{{ url_for('pengaturan') }}">Pengaturan</a>{% endif %}
<span class="sp"></span><a href="{{ url_for('akun') }}">{{ g.user.nama }}</a>
<form method="post" action="{{ url_for('logout') }}"><button>Keluar</button></form>
{% else %}<span class="sp"></span><a href="{{ url_for('login') }}">Masuk petugas</a>{% endif %}
</nav><main>
{% set o = request.args.get('ok') %}{% set e = err or request.args.get('err') %}
{% if o %}<div class="msg ok">{{ o }}</div>{% endif %}
{% if e %}<div class="msg bad">{{ e }}</div>{% endif %}
{% block body %}{% endblock %}
</main></body></html>""",

"login.html": """{% extends "base.html" %}{% block body %}
<div class="card narrow"><h1>Masuk</h1>
<form method="post">
<label>Nama pengguna<input name="username" autocomplete="username" autofocus required></label>
<label>Kata sandi<input type="password" name="password" autocomplete="current-password" required></label>
<button class="btn">Masuk</button></form></div>{% endblock %}""",

"setup.html": """{% extends "base.html" %}{% block body %}
<div class="card narrow"><h1>Buat akun admin pertama</h1>
<form method="post">
<label>Nama lengkap<input name="nama" required></label>
<label>Nama pengguna<input name="username" autocomplete="username" required></label>
<label>Kata sandi (min. 8 karakter)<input type="password" name="password" minlength="8" autocomplete="new-password" required></label>
<button class="btn">Buat akun</button></form></div>{% endblock %}""",

"landing.html": """{% extends "base.html" %}{% block body %}
{% if belum_setup %}<div class="msg warn">Belum ada akun admin. <a href="{{ url_for('setup') }}">Buat akun admin pertama</a>.</div>{% endif %}
<section class="hero">
<h1>Cari buku yang mau kamu baca</h1>
<p>Catat kode dan rak bukunya, lalu ambil di perpustakaan. Pinjam lewat petugas.</p>
<form class="big" method="get" role="search">
<input name="q" value="{{ q }}" placeholder="Judul atau pengarang" aria-label="Cari buku" autofocus>
{% if kat %}<input type="hidden" name="kat" value="{{ kat }}">{% endif %}{% if semua %}<input type="hidden" name="tampil" value="semua">{% endif %}
<button class="btn">Cari</button></form>
</section>
{% if kats %}<div class="chips">
<a class="chip {{ '' if kat else 'on' }}" href="{{ semua_kat }}">Semua</a>
{% for k in kats %}<a class="chip {{ 'on' if k.kategori == kat else '' }}" href="{{ k.href }}">{{ k.kategori }} ({{ k.n }})</a>{% endfor %}
</div>{% endif %}
<p class="hasil">{{ total }} buku {{ 'ditemukan' if (q or kat) else ('terdaftar' if semua else 'bisa dipinjam sekarang') }}.
<a href="{{ ganti_tampil }}">{{ 'Tampilkan yang tersedia saja' if semua else 'Tampilkan juga yang sedang dipinjam' }}</a></p>
<div class="rak">
{% for b in buku %}<article class="buku" style="--h:{{ b.hue }}">
<span class="stiker {{ '' if b.tersedia > 0 else 'habis' }}" title="{{ ('Tersedia ' ~ b.tersedia ~ ' eksemplar') if b.tersedia > 0 else 'Semua eksemplar sedang dipinjam' }}">{% if b.tersedia > 0 %}Ada<br>{{ b.tersedia }}{% else %}Habis{% endif %}</span>
<b>{{ b.judul }}</b>
{% if b.pengarang %}<small>{{ b.pengarang }}</small>{% endif %}
<small class="info">{% if b.rak %}Rak {{ b.rak }}, kode {{ b.kode }}{% else %}Kode {{ b.kode }}{% endif %}</small>
</article>
{% else %}<p class="empty">Tidak ada buku yang cocok. Coba kata lain, atau tampilkan juga buku yang sedang dipinjam.</p>{% endfor %}
</div>
{% if hal_maks > 1 %}<div class="pager">
{% if prev %}<a class="btn ghost" href="{{ prev }}">Sebelumnya</a>{% endif %}<span>Halaman {{ hal }} dari {{ hal_maks }}</span>{% if next %}<a class="btn ghost" href="{{ next }}">Berikutnya</a>{% endif %}
</div>{% endif %}{% endblock %}""",

"buku.html": """{% extends "base.html" %}{% block body %}
<div class="bar"><h1>Daftar Buku</h1><div class="row">
<a class="btn ghost" href="{{ url_for('export_buku', q=cari) }}">⬇ Unduh Excel</a>
<a class="btn" href="{{ url_for('buku_baru') }}">+ Tambah buku</a></div></div>
<form class="search" method="get">
<input name="q" value="{{ cari }}" placeholder="Cari judul, pengarang, atau kode buku…">
<button class="btn ghost">Cari</button></form>
<div class="card scroll"><table>
<tr><th>Kode</th><th>Judul</th><th>Pengarang</th><th>Rak</th><th>Tersedia</th><th></th></tr>
{% for b in buku %}<tr>
<td>{{ b.kode }}</td>
<td><strong>{{ b.judul }}</strong><br><small>{{ b.kategori }}</small></td>
<td>{{ b.pengarang }}</td><td>{{ b.rak }}</td>
<td><span class="pill {{ 'ok' if b.tersedia > 0 else 'bad' }}">{{ b.tersedia }} / {{ b.stok }}</span></td>
<td class="act">
{% if b.tersedia > 0 %}<a class="btn sm" href="{{ url_for('pinjam', buku=b.id) }}">Pinjam</a>{% endif %}
<a class="btn sm ghost" href="{{ url_for('buku_ubah', id=b.id) }}">Ubah</a>
<form method="post" action="{{ url_for('buku_hapus', id=b.id) }}" onsubmit="return confirm('Hapus buku ini?')"><button class="btn sm danger">Hapus</button></form>
</td></tr>
{% else %}<tr><td colspan="6" class="empty">Belum ada buku.</td></tr>{% endfor %}
</table></div>{% endblock %}""",

"buku_form.html": """{% extends "base.html" %}{% block body %}
<div class="card narrow"><h1>{{ 'Ubah' if b.id else 'Tambah' }} Buku</h1>
<form method="post">
<label>Kode buku<input name="kode" value="{{ b.kode }}" {{ '' if b.id else 'autofocus' }} required></label>
<label>Judul<input name="judul" value="{{ b.judul }}" required></label>
<label>Pengarang<input name="pengarang" value="{{ b.pengarang }}"></label>
<label>Penerbit<input name="penerbit" value="{{ b.penerbit }}"></label>
<div class="row2">
<label>Tahun<input name="tahun" value="{{ b.tahun }}" inputmode="numeric" maxlength="4"></label>
<label>Jumlah eksemplar<input type="number" min="0" name="stok" value="{{ b.stok }}" required></label></div>
<label>Kategori<input name="kategori" value="{{ b.kategori }}" placeholder="mis. Cerita anak, IPA, Kamus"></label>
<label>Lokasi rak<input name="rak" value="{{ b.rak }}" placeholder="mis. A-2"></label>
<div class="row"><button class="btn">Simpan</button><a class="btn ghost" href="{{ url_for('buku_list') }}">{{ 'Batal' if b.id else 'Kembali ke daftar' }}</a></div>
</form></div>{% endblock %}""",

"anggota.html": """{% extends "base.html" %}{% block body %}
<div class="bar"><h1>Data Anggota</h1><a class="btn" href="{{ url_for('anggota_baru') }}">+ Tambah anggota</a></div>
<form class="search" method="get">
<input name="q" value="{{ cari }}" placeholder="Cari nama, nomor, atau kelas…">
<button class="btn ghost">Cari</button></form>
<div class="card scroll"><table>
<tr><th>Nomor</th><th>Nama</th><th>Kelas</th><th>Jenis</th><th>Status</th><th></th></tr>
{% for a in rows %}<tr>
<td>{{ a.nomor }}</td><td><strong>{{ a.nama }}</strong></td><td>{{ a.kelas }}</td><td>{{ a.tipe|capitalize }}</td>
<td><span class="pill {{ 'ok' if a.aktif else 'bad' }}">{{ 'Aktif' if a.aktif else 'Nonaktif' }}</span></td>
<td class="act"><a class="btn sm ghost" href="{{ url_for('anggota_ubah', id=a.id) }}">Ubah</a>
<form method="post" action="{{ url_for('anggota_aktif', id=a.id) }}"><button class="btn sm {{ 'danger' if a.aktif else '' }}">{{ 'Nonaktifkan' if a.aktif else 'Aktifkan' }}</button></form></td>
</tr>{% else %}<tr><td colspan="6" class="empty">Belum ada anggota.</td></tr>{% endfor %}
</table></div>
{% if hal_maks > 1 %}<div class="pager">
{% if prev %}<a class="btn ghost" href="{{ prev }}">Sebelumnya</a>{% endif %}<span>Halaman {{ hal }} dari {{ hal_maks }} ({{ total }} anggota)</span>{% if next %}<a class="btn ghost" href="{{ next }}">Berikutnya</a>{% endif %}
</div>{% endif %}{% endblock %}""",

"anggota_form.html": """{% extends "base.html" %}{% block body %}
<div class="card narrow"><h1>{{ 'Ubah' if a.id else 'Tambah' }} Anggota</h1>
<form method="post">
<label>Nomor anggota (NIS/NIP)<input name="nomor" value="{{ a.nomor }}" {{ '' if a.id else 'autofocus' }} required></label>
<label>Nama lengkap<input name="nama" value="{{ a.nama }}" required></label>
<label>Kelas<input name="kelas" value="{{ a.kelas }}" placeholder="mis. 4B (kosongkan untuk guru)"></label>
<label>Jenis<select name="tipe">
{% for v, t in [('siswa', 'Siswa'), ('guru', 'Guru'), ('lainnya', 'Lainnya')] %}<option value="{{ v }}" {{ 'selected' if v == a.tipe else '' }}>{{ t }}</option>{% endfor %}
</select></label>
<div class="row"><button class="btn">Simpan</button><a class="btn ghost" href="{{ url_for('anggota_list') }}">{{ 'Batal' if a.id else 'Kembali ke daftar' }}</a></div>
</form></div>{% endblock %}""",

"pinjam.html": """{% extends "base.html" %}{% block body %}
<div class="card narrow"><h1>Peminjaman Buku</h1>
<form method="post" id="fp">
<label>Buku<input id="bk" list="bkList" placeholder="Ketik judul atau kode buku" value="{{ pilih_label }}" autocomplete="off" {{ '' if pilih_label else 'autofocus' }} required></label>
<input type="hidden" name="buku_id" id="bkId">
<datalist id="bkList">{% for k in buku_peta %}<option value="{{ k }}"></option>{% endfor %}</datalist>
<label>Anggota<input id="ang" list="angList" placeholder="Ketik nama atau nomor anggota" autocomplete="off" {{ 'autofocus' if pilih_label else '' }} required></label>
<input type="hidden" name="anggota_id" id="angId">
<datalist id="angList">{% for k in peta %}<option value="{{ k }}"></option>{% endfor %}</datalist>
<p class="hint">Pilih dari daftar yang muncul saat mengetik. Anggota belum terdaftar? <a href="{{ url_for('anggota_baru') }}">Tambah anggota baru</a>.</p>
<label>Batas pengembalian<input type="date" name="jatuh_tempo" value="{{ jatuh_tempo }}" required></label>
<button class="btn">Catat peminjaman</button></form></div>
<script>
function combo(i,h,map,pesan){const inp=document.getElementById(i),hid=document.getElementById(h);
const sync=()=>{hid.value=map[inp.value]||'';inp.setCustomValidity('')};inp.addEventListener('input',sync);sync();return {inp,hid,pesan}}
const cs=[combo('bk','bkId',{{ buku_peta|tojson }},'Pilih buku dari daftar yang muncul.'),
combo('ang','angId',{{ peta|tojson }},'Pilih anggota dari daftar yang muncul.')];
document.getElementById('fp').addEventListener('submit',e=>{for(const c of cs)if(!c.hid.value){e.preventDefault();c.inp.setCustomValidity(c.pesan);c.inp.reportValidity();return}});
</script>{% endblock %}""",

"transaksi.html": """{% extends "base.html" %}{% block body %}
<div class="bar"><h1>Transaksi</h1>
<a class="btn" href="{{ url_for('export_xlsx', status=status, q=cari) }}">⬇ Unduh Excel</a></div>
<form class="search" method="get">
<input name="q" value="{{ cari }}" placeholder="Cari peminjam, nomor anggota, judul, atau kode…">
<select name="status">
{% for v, t in [('', 'Semua'), ('dipinjam', 'Masih dipinjam'), ('kembali', 'Sudah kembali'), ('denda', 'Denda belum lunas')] %}
<option value="{{ v }}" {{ 'selected' if v == status else '' }}>{{ t }}</option>{% endfor %}
</select><button class="btn ghost">Terapkan</button></form>
<div class="card scroll"><table>
<tr><th>Tgl pinjam</th><th>Buku</th><th>Peminjam</th><th>Batas kembali</th><th>Status</th><th></th></tr>
{% for r in rows %}<tr>
<td>{{ r.tgl_pinjam }}</td>
<td><strong>{{ r.judul }}</strong><br><small>{{ r.kode }}</small></td>
<td>{{ r.peminjam }}<br><small>{{ r.kelas }}</small></td>
<td>{{ r.tgl_jatuh_tempo }}{% if r.tgl_kembali %}<br><small>kembali {{ r.tgl_kembali }}</small>{% endif %}</td>
<td><span class="pill {{ r.css }}">{{ r.status }}</span>
{% if r.denda_now %}<br><small>Denda {{ r.denda_now|rupiah }} ({{ r.telat }} hari){% if r.tgl_kembali %}, {{ 'lunas' if r.denda_lunas else 'belum lunas' }}{% else %}, berjalan{% endif %}</small>{% endif %}</td>
<td class="act">{% if not r.tgl_kembali %}
<form method="post" action="{{ url_for('kembali', id=r.id) }}"><input type="hidden" name="status" value="{{ status }}"><button class="btn sm">Kembalikan</button></form>
{% elif r.denda and not r.denda_lunas %}
<form method="post" action="{{ url_for('denda_aksi', id=r.id) }}"><input type="hidden" name="aksi" value="lunas"><input type="hidden" name="status" value="{{ status }}"><button class="btn sm">Tandai lunas</button></form>
<form method="post" action="{{ url_for('denda_aksi', id=r.id) }}" onsubmit="return confirm('Bebaskan denda ini?')"><input type="hidden" name="aksi" value="bebas"><input type="hidden" name="status" value="{{ status }}"><button class="btn sm ghost">Bebaskan</button></form>
{% endif %}</td></tr>
{% else %}<tr><td colspan="6" class="empty">Belum ada transaksi.</td></tr>{% endfor %}
</table></div>{% endblock %}""",

"pengguna.html": """{% extends "base.html" %}{% block body %}
<div class="bar"><h1>Pengguna</h1></div>
<div class="card scroll"><table>
<tr><th>Nama</th><th>Username</th><th>Peran</th><th>Status</th><th></th></tr>
{% for u in users %}<tr>
<td>{{ u.nama }}</td><td>{{ u.username }}</td><td>{{ u.role }}</td>
<td><span class="pill {{ 'ok' if u.aktif else 'bad' }}">{{ 'Aktif' if u.aktif else 'Nonaktif' }}</span></td>
<td class="act">
<form method="post" action="{{ url_for('pengguna_aktif', id=u.id) }}"><button class="btn sm ghost">{{ 'Nonaktifkan' if u.aktif else 'Aktifkan' }}</button></form>
<form class="inl" method="post" action="{{ url_for('pengguna_reset', id=u.id) }}"><input type="password" name="password" placeholder="Sandi baru" minlength="8" required><button class="btn sm">Ganti</button></form>
</td></tr>{% endfor %}
</table></div>
<div class="card narrow" style="margin-top:20px"><h2>Tambah pengguna</h2>
<form method="post" action="{{ url_for('pengguna_baru') }}">
<label>Nama lengkap<input name="nama" required></label>
<label>Nama pengguna<input name="username" required></label>
<label>Kata sandi (min. 8 karakter)<input type="password" name="password" minlength="8" required></label>
<label>Peran<select name="role"><option value="pustakawan">Pustakawan</option><option value="admin">Admin</option></select></label>
<button class="btn">Tambah</button></form></div>{% endblock %}""",

"akun.html": """{% extends "base.html" %}{% block body %}
<div class="card narrow"><h1>Akun saya</h1>
<p class="hint">Masuk sebagai {{ g.user.nama }} ({{ g.user.username }}), peran {{ g.user.role }}.</p>
<h2>Ganti kata sandi</h2>
<form method="post">
<label>Kata sandi lama<input type="password" name="lama" autocomplete="current-password" required></label>
<label>Kata sandi baru (min. 8 karakter)<input type="password" name="baru" minlength="8" autocomplete="new-password" required></label>
<label>Ulangi kata sandi baru<input type="password" name="ulang" minlength="8" autocomplete="new-password" required></label>
<button class="btn">Simpan kata sandi</button></form></div>{% endblock %}""",

"pengaturan.html": """{% extends "base.html" %}{% block body %}
<div class="card narrow"><h1>Pengaturan</h1>
<form method="post">
<label>Lama peminjaman (hari)<input type="number" min="1" max="90" name="masa_pinjam" value="{{ cfg.masa_pinjam }}" required></label>
<label>Denda per hari terlambat (Rp)<input type="number" min="0" name="denda_per_hari" value="{{ cfg.denda_per_hari }}" required></label>
<p class="hint">Isi 0 jika perpustakaan tidak memakai denda. Denda dihitung per buku.</p>
<label>Batas maksimal denda per buku (Rp)<input type="number" min="0" name="denda_maks" value="{{ cfg.denda_maks }}" required></label>
<p class="hint">Isi 0 untuk tanpa batas. Perubahan berlaku untuk pengembalian berikutnya.</p>
<button class="btn">Simpan pengaturan</button></form></div>{% endblock %}""",
}