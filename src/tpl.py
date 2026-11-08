STYLE = """
:root{--merah:#900F0F;--merah-tua:#6E0B0B;--merah-muda:#F4DAD6;--krem:#EADBC8;--krem-muda:#F6EEE3;--krem-tua:#D5BFA2;--tinta:#1F2937;--redup:rgba(31,41,55,.72);
--f-judul:"Fredoka","Trebuchet MS","Segoe UI",system-ui,sans-serif;--f-isi:"Lexend","Segoe UI",system-ui,sans-serif}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;flex-direction:column;background:var(--krem);color:var(--tinta);font:400 16px/1.6 var(--f-isi)}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.1;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 420'%3E%3Cg fill='%23900F0F'%3E%3Crect y='400' width='1000' height='8'/%3E%3Crect x='250' y='215' width='500' height='185'/%3E%3Cpolygon points='228,220 500,118 772,220'/%3E%3Crect x='418' y='255' width='164' height='145'/%3E%3Cpolygon points='408,258 500,200 592,258'/%3E%3Crect x='862' y='120' width='7' height='280'/%3E%3Cpolygon points='869,124 940,146 869,168'/%3E%3Ccircle cx='120' cy='320' r='58'/%3E%3Crect x='114' y='360' width='12' height='40'/%3E%3C/g%3E%3Cg fill='%23EADBC8'%3E%3Crect x='482' y='322' width='36' height='78'/%3E%3Crect x='285' y='255' width='46' height='56'/%3E%3Crect x='355' y='255' width='46' height='56'/%3E%3Crect x='599' y='255' width='46' height='56'/%3E%3Crect x='669' y='255' width='46' height='56'/%3E%3C/g%3E%3C/svg%3E") center bottom/min(1100px,100%) no-repeat}
body.ada-latar::before{opacity:.22;background:var(--latar) center/cover no-repeat}
header{background:var(--tinta);color:var(--krem);border-bottom:4px solid var(--merah)}
.hd{max-width:1080px;margin:0 auto;padding:12px 16px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:14px;color:inherit;text-decoration:none;margin-right:auto}
.logo{width:56px;height:56px;border-radius:50%;flex:none;object-fit:contain;background:var(--krem);border:3px solid var(--krem)}
.logo-ph{display:grid;place-items:center;font:700 20px var(--f-judul);color:var(--merah)}
.brand small{display:block;font-size:13px;color:rgba(234,219,200,.85)}
.brand b{display:block;font:700 22px/1.2 var(--f-judul);color:var(--krem)}
.kanan{display:flex;align-items:center;gap:8px;margin-left:auto}.kanan form{margin:0}
.akun{color:var(--krem);text-decoration:none;font-weight:500;padding:6px 10px;border-radius:99px}.akun:hover{background:rgba(234,219,200,.14)}
.btn-ol{display:inline-block;padding:7px 16px;border:1.5px solid var(--krem);border-radius:99px;background:none;color:var(--krem);font:500 15px var(--f-isi);text-decoration:none;cursor:pointer}
.btn-ol:hover{background:var(--krem);color:var(--tinta)}
.menu{max-width:1080px;margin:0 auto;padding:0 16px 12px;display:flex;gap:6px;overflow-x:auto;white-space:nowrap}
.menu a{color:var(--krem);text-decoration:none;padding:8px 18px;border-radius:99px;font-weight:500}
.menu a:hover{background:rgba(234,219,200,.14)}.menu a.on{background:var(--merah);color:#fff}
header a:focus-visible,header button:focus-visible{outline:3px solid var(--krem);outline-offset:2px}
main{flex:1;width:100%;max-width:1080px;margin:0 auto;padding:28px 16px 44px}
h1,h2,h3{margin:0 0 12px;font-family:var(--f-judul);font-weight:700;color:var(--merah);line-height:1.2}
h1{font-size:30px}h2{font-size:22px}
.jdl{font:700 17px/1.3 var(--f-judul);color:var(--merah)}.nw{white-space:nowrap}
.bar{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.card{background:var(--krem-muda);border:1.5px solid var(--krem-tua);border-radius:16px;padding:22px;box-shadow:0 14px 24px -18px rgba(31,41,55,.5)}
.narrow{max-width:540px;margin:0 auto}.scroll{overflow-x:auto;padding:0}
table{width:100%;border-collapse:collapse}
th,td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--krem-tua);vertical-align:top}
tr:last-child td{border-bottom:0}
th{font-weight:500;font-size:14px;color:var(--redup);background:rgba(234,219,200,.6)}
small{color:var(--redup)}a{color:var(--merah)}
label{display:block;margin-bottom:14px;font-weight:500}
input,select{display:block;width:100%;margin-top:6px;padding:11px 13px;font:400 16px var(--f-isi);color:var(--tinta);background:#fff;border:1.5px solid var(--krem-tua);border-radius:10px}
input:focus,select:focus{outline:3px solid rgba(144,15,15,.28);border-color:var(--merah)}
main a:focus-visible,main button:focus-visible{outline:3px solid rgba(144,15,15,.45);outline-offset:2px}
.btn{display:inline-block;padding:10px 20px;border:1.5px solid var(--merah);border-radius:12px;background:var(--merah);color:#fff;font:500 16px var(--f-isi);text-decoration:none;cursor:pointer}
.btn:hover{background:var(--merah-tua);border-color:var(--merah-tua)}
.ghost{background:var(--krem-muda);border-color:var(--krem-tua);color:var(--tinta)}.ghost:hover{background:var(--krem);border-color:var(--krem-tua)}
.danger{background:#fff;color:var(--merah)}.danger:hover{background:var(--merah-muda);border-color:var(--merah)}
.sm{padding:5px 12px;font-size:14px;border-radius:10px}
.search{display:flex;gap:8px;margin-bottom:18px}.search input{flex:1;margin:0}.search select{width:auto;margin:0}
.row{display:flex;gap:10px;flex-wrap:wrap}.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.act{white-space:nowrap}.act form{display:inline}
.act .inl{display:inline-flex;gap:6px}.inl input{width:130px;margin:0;padding:6px 8px}
.pill{display:inline-block;padding:1px 12px;border:1.5px solid transparent;border-radius:99px;font-size:14px;font-weight:500}
.pill.ok{border-color:var(--tinta);color:var(--tinta)}.pill.warn{background:var(--tinta);color:var(--krem)}.pill.bad{background:var(--merah);color:#fff}
.msg{padding:13px 16px;border:1.5px solid var(--krem-tua);border-radius:12px;margin-bottom:18px;font-weight:500;background:var(--krem-muda)}
.msg.ok{border-color:var(--tinta)}.msg.bad{background:var(--merah-muda);border-color:var(--merah);color:var(--merah-tua)}.msg a{color:inherit}
.empty{text-align:center;color:var(--redup);padding:32px}
.hint{color:var(--redup);margin:-6px 0 14px;font-size:14px}
.pager{display:flex;gap:12px;align-items:center;justify-content:center;margin:26px 0}
.hero{padding:4px 0}
.hero h1{font-size:clamp(30px,5vw,46px);margin-bottom:8px}
.hero p{margin:0 0 18px;max-width:58ch}
.big{display:flex;gap:10px;max-width:660px}
.big input{flex:1;margin:0;padding:15px 18px;font-size:18px;border-radius:14px}
.big .btn{padding:0 28px;font-size:18px;border-radius:14px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 6px}
.chip{padding:6px 16px;border:1.5px solid var(--krem-tua);border-radius:99px;background:var(--krem-muda);color:var(--tinta);text-decoration:none;font-weight:500}
.chip:hover{background:#fff}.chip.on{background:var(--merah);border-color:var(--merah);color:#fff}
.hasil{margin:10px 0 20px;color:var(--redup)}.hasil a{font-weight:500}
.rak{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:20px}
.buku{--spine:var(--merah);position:relative;display:flex;flex-direction:column;justify-content:flex-end;gap:3px;aspect-ratio:3/4;padding:16px 14px 16px 18px;overflow:hidden;
background:var(--krem-muda);border:1.5px solid var(--krem-tua);border-left:14px solid var(--spine);border-radius:6px 16px 16px 6px;box-shadow:0 12px 18px -14px rgba(31,41,55,.6)}
.buku.v1{--spine:var(--tinta)}.buku.v2{--spine:var(--krem-tua)}
.buku b{font:700 19px/1.2 var(--f-judul);color:var(--merah);display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.buku small{font-size:14px;color:var(--tinta);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.buku small.info{white-space:normal;font-size:13px;color:var(--redup)}
.stiker{position:absolute;top:10px;right:10px;width:50px;height:50px;border-radius:50%;display:grid;place-items:center;text-align:center;
font:500 13px/1.05 var(--f-isi);background:var(--merah);color:#fff;transform:rotate(8deg);box-shadow:0 3px 0 rgba(31,41,55,.25)}
.stiker.habis{background:var(--krem);color:var(--tinta);border:1.5px solid var(--tinta)}
footer{background:var(--tinta);color:var(--krem)}
.ft{max-width:1080px;margin:0 auto;padding:28px 16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
footer b{display:block;margin-bottom:6px;font:700 18px var(--f-judul)}footer p{margin:2px 0;color:rgba(234,219,200,.9)}
@media(max-width:480px){.brand b{font-size:19px}.logo{width:48px;height:48px}}
"""

T = {
"base.html": """<!doctype html>
<html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Perpustakaan Sekolah — {{ sekolah.nama }}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@700&amp;family=Lexend:wght@400;500&amp;display=swap" rel="stylesheet">
<style>""" + STYLE + """</style></head>
<body{% if latar_url %} class="ada-latar" style="--latar:url('{{ latar_url }}')"{% endif %}>
<header><div class="hd">
<a class="brand" href="{{ url_for('landing') }}">
{% if logo_url %}<img class="logo" src="{{ logo_url }}" alt="Logo sekolah">{% else %}<span class="logo logo-ph">SD</span>{% endif %}
<span><small>{{ sekolah.nama }}</small><b>Perpustakaan Sekolah</b></span></a>
<div class="kanan">
{% if g.user %}<a class="akun" href="{{ url_for('akun') }}">{{ g.user.nama }}</a>
<form method="post" action="{{ url_for('logout') }}"><button class="btn-ol">Keluar</button></form>
{% else %}<a class="btn-ol" href="{{ url_for('login') }}">Masuk petugas</a>{% endif %}
</div></div>
{% if g.user %}{% set ep = request.endpoint or '' %}
<nav class="menu" aria-label="Menu petugas">
<a class="{{ 'on' if ep.startswith('buku') else '' }}" href="{{ url_for('buku_list') }}">Buku</a>
<a class="{{ 'on' if ep.startswith('anggota') else '' }}" href="{{ url_for('anggota_list') }}">Anggota</a>
<a class="{{ 'on' if ep == 'pinjam' else '' }}" href="{{ url_for('pinjam') }}">Pinjam</a>
<a class="{{ 'on' if ep == 'transaksi' else '' }}" href="{{ url_for('transaksi') }}">Transaksi</a>
{% if g.user.role == 'admin' %}<a class="{{ 'on' if ep == 'pengguna' else '' }}" href="{{ url_for('pengguna') }}">Pengguna</a>
<a class="{{ 'on' if ep == 'pengaturan' else '' }}" href="{{ url_for('pengaturan') }}">Pengaturan</a>{% endif %}
</nav>{% endif %}
</header>
<main>
{% set o = request.args.get('ok') %}{% set e = err or request.args.get('err') %}
{% if o %}<div class="msg ok">{{ o }}</div>{% endif %}
{% if e %}<div class="msg bad">{{ e }}</div>{% endif %}
{% block body %}{% endblock %}
</main>
<footer><div class="ft">
<div><b>Perpustakaan {{ sekolah.nama }}</b><p>{{ sekolah.alamat }}</p></div>
<div><b>Layanan</b><p>{{ sekolah.jam }}</p></div>
</div></footer>
</body></html>""",

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
<p>Catat rak dan kode bukunya, lalu ambil di perpustakaan. Untuk meminjam, temui petugas perpustakaan.</p>
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
{% for b in buku %}<article class="buku v{{ b.v }}">
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
<td class="nw">{{ b.kode }}</td>
<td><strong class="jdl">{{ b.judul }}</strong><br><small>{{ b.kategori }}</small></td>
<td>{{ b.pengarang }}</td><td class="nw">{{ b.rak }}</td>
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
<td class="nw">{{ r.tgl_pinjam }}</td>
<td><strong class="jdl">{{ r.judul }}</strong><br><small>{{ r.kode }}</small></td>
<td>{{ r.peminjam }}<br><small>{{ r.kelas }}</small></td>
<td class="nw">{{ r.tgl_jatuh_tempo }}{% if r.tgl_kembali %}<br><small>kembali {{ r.tgl_kembali }}</small>{% endif %}</td>
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