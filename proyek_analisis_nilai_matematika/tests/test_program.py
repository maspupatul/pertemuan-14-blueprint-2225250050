import tempfile
import unittest
from pathlib import Path

from src.input_data import baca_data, validasi_nilai
from src.proses import hitung_statistik


class TestAnalisisNilai(unittest.TestCase):
    def test_validasi_nilai_batas_bawah_dan_atas(self):
        self.assertTrue(validasi_nilai(0))
        self.assertTrue(validasi_nilai(100))

    def test_validasi_nilai_di_luar_rentang(self):
        self.assertFalse(validasi_nilai(-1))
        self.assertFalse(validasi_nilai(101))

    def test_hitung_statistik_normal(self):
        data = [
            {"nama": "Ayu", "nilai": 70},
            {"nama": "Budi", "nilai": 80},
            {"nama": "Citra", "nilai": 90},
        ]
        hasil = hitung_statistik(data, kkm=75)
        self.assertEqual(hasil["rata_rata"], 80)
        self.assertEqual(hasil["minimum"], 70)
        self.assertEqual(hasil["maksimum"], 90)
        self.assertEqual(hasil["tuntas"], 2)
        self.assertEqual(hasil["belum_tuntas"], 1)

    def test_data_invalid_dilewati(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nilai.txt"
            path.write_text("Ayu,85\nBudi,105\nCitra,abc\n", encoding="utf-8")
            data, catatan = baca_data(path)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["nama"], "Ayu")
            self.assertEqual(len(catatan), 2)

    def test_data_kosong(self):
        hasil = hitung_statistik([], kkm=75)
        self.assertEqual(hasil["jumlah"], 0)
        self.assertIsNone(hasil["minimum"])
        self.assertIsNone(hasil["maksimum"])

    def test_file_tidak_ditemukan(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tidak_ada.txt"
            with self.assertRaises(FileNotFoundError):
                baca_data(path)


if __name__ == "__main__":
    unittest.main()
