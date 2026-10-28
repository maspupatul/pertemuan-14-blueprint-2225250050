from pathlib import Path

from src.input_data import baca_data
from src.proses import hitung_statistik
from src.output import buat_laporan, tampilkan_laporan, simpan_laporan

BASE_DIR = Path(__file__).resolve().parent
FILE_DATA = BASE_DIR / "data" / "nilai_contoh.txt"
FILE_LAPORAN = BASE_DIR / "output" / "laporan.txt"
KKM = 75


def main():
    """Menjalankan alur utama program analisis nilai."""
    print("=== PROGRAM ANALISIS NILAI MATEMATIKA SISWA ===")

    try:
        data_siswa, catatan = baca_data(FILE_DATA)
    except FileNotFoundError:
        print(f"File data tidak ditemukan: {FILE_DATA}")
        return

    for pesan in catatan:
        print(f"Catatan: {pesan}")

    if not data_siswa:
        print("Tidak ada data valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data_siswa, KKM)
    laporan = buat_laporan(statistik, data_siswa, KKM)
    tampilkan_laporan(laporan)
    simpan_laporan(FILE_LAPORAN, laporan)
    print(f"\nLaporan berhasil disimpan ke: {FILE_LAPORAN}")


if __name__ == "__main__":
    main()
