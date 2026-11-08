CREATE TABLE IF NOT EXISTS anggota (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nomor TEXT NOT NULL UNIQUE,
  nama TEXT NOT NULL,
  kelas TEXT NOT NULL DEFAULT '',
  tipe TEXT NOT NULL DEFAULT 'siswa' CHECK (tipe IN ('siswa', 'guru', 'lainnya')),
  aktif INTEGER NOT NULL DEFAULT 1
);
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

ALTER TABLE transaksi ADD COLUMN anggota_id INTEGER REFERENCES anggota(id);
ALTER TABLE transaksi ADD COLUMN denda INTEGER NOT NULL DEFAULT 0;
ALTER TABLE transaksi ADD COLUMN denda_lunas INTEGER NOT NULL DEFAULT 0;

-- Peminjam lama dijadikan anggota (nomor sementara L0001, L0002, ...; bisa diubah di menu Anggota).
INSERT INTO anggota (nomor, nama, kelas)
SELECT 'L' || printf('%04d', ROW_NUMBER() OVER (ORDER BY peminjam, kelas)), peminjam, kelas
FROM (SELECT DISTINCT peminjam, kelas FROM transaksi);

UPDATE transaksi SET anggota_id = (
  SELECT a.id FROM anggota a WHERE a.nama = transaksi.peminjam AND a.kelas = transaksi.kelas
);
CREATE INDEX IF NOT EXISTS idx_transaksi_anggota ON transaksi(anggota_id);