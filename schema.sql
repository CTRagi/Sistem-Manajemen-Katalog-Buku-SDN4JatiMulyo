CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  nama TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK (role IN ('admin', 'pustakawan')),
  aktif INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS buku (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  kode TEXT NOT NULL UNIQUE,
  judul TEXT NOT NULL,
  pengarang TEXT NOT NULL DEFAULT '',
  penerbit TEXT NOT NULL DEFAULT '',
  tahun TEXT NOT NULL DEFAULT '',
  kategori TEXT NOT NULL DEFAULT '',
  rak TEXT NOT NULL DEFAULT '',
  stok INTEGER NOT NULL DEFAULT 1 CHECK (stok >= 0)
);

CREATE TABLE IF NOT EXISTS anggota (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nomor TEXT NOT NULL UNIQUE,
  nama TEXT NOT NULL,
  kelas TEXT NOT NULL DEFAULT '',
  tipe TEXT NOT NULL DEFAULT 'siswa' CHECK (tipe IN ('siswa', 'guru', 'lainnya')),
  aktif INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS transaksi (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  buku_id INTEGER NOT NULL REFERENCES buku(id),
  anggota_id INTEGER REFERENCES anggota(id),
  peminjam TEXT NOT NULL,
  kelas TEXT NOT NULL DEFAULT '',
  tgl_pinjam TEXT NOT NULL,
  tgl_jatuh_tempo TEXT NOT NULL,
  tgl_kembali TEXT,
  petugas TEXT NOT NULL DEFAULT '',
  denda INTEGER NOT NULL DEFAULT 0,
  denda_lunas INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_transaksi_aktif ON transaksi(buku_id) WHERE tgl_kembali IS NULL;
CREATE INDEX IF NOT EXISTS idx_transaksi_anggota ON transaksi(anggota_id);

CREATE TABLE IF NOT EXISTS pengaturan (
  kunci TEXT PRIMARY KEY,
  nilai TEXT NOT NULL
);
INSERT OR IGNORE INTO pengaturan (kunci, nilai)
VALUES ('masa_pinjam', '7'), ('denda_per_hari', '500'), ('denda_maks', '0');

CREATE TABLE IF NOT EXISTS percobaan_login (
  kunci TEXT PRIMARY KEY,
  gagal INTEGER NOT NULL,
  mulai INTEGER NOT NULL,
  terkunci_sampai INTEGER NOT NULL DEFAULT 0
);