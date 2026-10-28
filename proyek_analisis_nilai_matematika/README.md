# Program Analisis Nilai Matematika Siswa

## Deskripsi
Program Python berbasis terminal untuk membaca data nilai siswa dari file, memeriksa nilai yang valid, menghitung statistik kelas, menentukan status ketuntasan, dan menyimpan laporan ke file teks.

Proyek ini dibuat untuk tugas individu mata kuliah Algoritma dan Pemrograman, Pertemuan 14 dan 15.

## Fitur
- Membaca nama dan nilai siswa dari `data/nilai_contoh.txt`.
- Memvalidasi nilai pada rentang 0 sampai 100.
- Menghitung rata-rata, nilai minimum, dan nilai maksimum.
- Menentukan jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
- Menyimpan hasil ke `output/laporan.txt`.
- Menangani baris data yang tidak valid dan file yang tidak ditemukan.

## Persyaratan
- Python 3
- Visual Studio Code (disarankan)

## Cara Menjalankan
1. Buka folder proyek ini di VS Code.
2. Buka terminal melalui menu **Terminal > New Terminal**.
3. Jalankan perintah:

   ```bash
   python main.py
   ```

   Jika perintah `python` tidak dikenali di Windows, coba:

   ```bash
   py main.py
   ```

4. Hasil akan tampil di terminal dan tersimpan di `output/laporan.txt`.

## Cara Menjalankan Pengujian
Di terminal VS Code, jalankan:

```bash
python -m unittest discover -s tests -v
```

Jika perintah `python` tidak dikenali, coba:

```bash
py -m unittest discover -s tests -v
```

## Struktur Folder
```text
proyek_analisis_nilai_matematika/
├── README.md
├── proposal.md
├── .gitignore
├── main.py
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── tests/
│   ├── test_case.md
│   └── test_program.py
├── docs/
│   └── bug_log.md
└── output/
    └── .gitkeep
```

## Test Case
Rencana dan hasil pengujian awal dicatat di `tests/test_case.md`. Pengujian otomatis dijalankan melalui `tests/test_program.py`.

## Known Issues
- Program membaca format data sederhana `nama,nilai`, satu siswa per baris.
- Nama siswa pada file contoh merupakan nama fiktif. Jangan masukkan data pribadi nyata ke repositori publik.

## Kontribusi
Proyek ini dikerjakan secara individu. Seluruh perancangan, implementasi, pengujian, dan dokumentasi dikerjakan oleh penulis.

## Referensi dan Bantuan
- Bahan Ajar Algoritma dan Pemrograman Pertemuan 14: Perancangan Proyek Program Sederhana.
- Bahan Ajar Algoritma dan Pemrograman Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi Proyek.
- Dokumentasi Python: https://docs.python.org/3/
- Bantuan AI digunakan untuk membantu menyusun kerangka awal dan penjelasan teknis; kode tetap perlu dipahami, dijalankan, dan diperiksa oleh penulis.
