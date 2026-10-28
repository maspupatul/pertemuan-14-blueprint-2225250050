# Test Case Program Analisis Nilai

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Nilai 70, 80, 90 | Rata-rata 80 | Isi setelah dijalankan | Belum diuji |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid | Isi setelah dijalankan | Belum diuji |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid | Isi setelah dijalankan | Belum diuji |
| TC04 | Invalid | Nilai 105 | Baris ditolak dan catatan validasi muncul | Isi setelah dijalankan | Belum diuji |
| TC05 | Invalid | Teks nilai `abc` | Baris ditolak dan catatan bahwa nilai bukan angka muncul | Isi setelah dijalankan | Belum diuji |
| TC06 | Khusus/kosong | Tidak ada data valid | Program memberi pesan dan tidak membagi dengan nol | Isi setelah dijalankan | Belum diuji |
| TC07 | File | File tidak ditemukan | Kesalahan ditangani dengan pesan yang jelas | Isi setelah dijalankan | Belum diuji |

Catatan: setelah menjalankan program dan pengujian otomatis, ubah kolom Hasil Aktual dan Status sesuai hasil yang benar-benar kamu dapatkan. Jangan menandai PASS jika belum diuji.
