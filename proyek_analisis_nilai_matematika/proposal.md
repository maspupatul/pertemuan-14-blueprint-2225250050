# Proposal Proyek: Program Analisis Nilai Matematika Siswa

## 1. Judul Proyek
Program Analisis Nilai Matematika Siswa.

## 2. Latar Belakang
Pengolahan nilai siswa secara manual membutuhkan waktu dan berisiko menimbulkan kesalahan perhitungan. Program sederhana berbasis Python dapat membantu menghitung statistik nilai dan merangkum ketuntasan secara lebih konsisten.

## 3. Pengguna dan Tujuan
**Pengguna:** guru matematika atau mahasiswa calon guru yang berlatih mengolah data nilai.

**Tujuan:** membantu membaca data nilai, menghitung statistik dasar, menentukan status ketuntasan berdasarkan KKM, dan menyimpan ringkasan hasil.

## 4. Ruang Lingkup
### Fitur wajib
1. Membaca data nama dan nilai dari file teks.
2. Memeriksa apakah nilai berada pada rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM 75.
5. Menampilkan dan menyimpan laporan ke file teks.

### Batasan
- Program berjalan melalui terminal/console.
- Data contoh menggunakan format `nama,nilai`, satu data per baris.
- Program tidak menggunakan database atau layanan eksternal.
- Data contoh tidak menggunakan informasi pribadi nyata.

## 5. Kebutuhan
### Fungsional
- F01: Program membaca file data nilai.
- F02: Program menerima nilai hanya pada rentang 0–100.
- F03: Program menghitung rata-rata, minimum, dan maksimum dari data valid.
- F04: Program menentukan status tuntas jika nilai >= 75.
- F05: Program menyimpan laporan ke `output/laporan.txt`.
- F06: Program menampilkan pesan yang mudah dipahami jika file tidak ditemukan atau tidak ada data valid.

### Nonfungsional
- Nama fungsi dan variabel mudah dipahami.
- Program dapat dijalankan dari terminal VS Code.
- Pengujian dapat diulang dengan test case yang sama.
- Pesan kesalahan dibuat jelas.

## 6. Input, Proses, Output (IPO)
| Input | Proses | Output |
|---|---|---|
| File `data/nilai_contoh.txt` berisi nama dan nilai | Membaca baris, memeriksa format dan rentang nilai, menghitung statistik, menentukan ketuntasan | Ringkasan statistik di terminal dan laporan di `output/laporan.txt` |

## 7. Algoritma/Pseudocode
```text
MULAI
  tentukan lokasi file data
  baca data dari file
  jika file tidak ditemukan:
    tampilkan pesan kesalahan
    SELESAI
  periksa setiap baris data
  simpan hanya data dengan format dan nilai yang valid
  jika tidak ada data valid:
    tampilkan pesan
    SELESAI
  hitung rata-rata, minimum, dan maksimum
  hitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM
  tampilkan ringkasan
  simpan ringkasan ke file laporan
SELESAI
```

## 8. Struktur Program
- `main.py`: mengatur alur utama program.
- `src/input_data.py`: membaca dan memvalidasi data dari file.
- `src/proses.py`: menghitung statistik dan status ketuntasan.
- `src/output.py`: menyusun, menampilkan, dan menyimpan laporan.
- `tests/test_program.py`: pengujian fungsi program.
- `tests/test_case.md`: tabel test case.
- `docs/bug_log.md`: catatan bug dan perbaikannya.

## 9. Struktur Data
- **List:** menyimpan daftar data siswa dan nilai.
- **Dictionary:** menyimpan data tiap siswa (`nama` dan `nilai`) serta ringkasan statistik.
- **String:** menyusun laporan teks.

## 10. Test Case Awal
Lihat `tests/test_case.md`. Test case mencakup kondisi normal, batas, invalid, data kosong, dan file yang tidak ditemukan.

## 11. Pelaksanaan Individu
Proyek dikerjakan secara individu. Penulis bertanggung jawab atas perancangan, penulisan kode, pengujian, debugging, dokumentasi, dan pengunggahan ke GitHub.

## 12. Jadwal/Milestone
- Pertemuan 14: menyusun rancangan, proposal, struktur folder, dan test case awal.
- Pertemuan 15: mengimplementasikan program, menjalankan pengujian, memperbaiki bug, dan melengkapi dokumentasi.
- Pertemuan 16: menyiapkan demonstrasi dan menjelaskan alur program serta hasil pengujian.

## 13. Repository
https://github.com/maspupatul/pertemuan-14-blueprint-2225250050.git