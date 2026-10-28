def validasi_nilai(nilai):
    """Mengembalikan True jika nilai berupa angka dalam rentang 0 sampai 100."""
    return isinstance(nilai, (int, float)) and 0 <= nilai <= 100


def baca_data(path):
    """Membaca file berformat nama,nilai dan mengembalikan (data_valid, catatan).

    Baris dengan format salah atau nilai di luar rentang akan dilewati dan dicatat.
    File yang tidak ditemukan diteruskan agar dapat ditangani oleh pemanggil.
    """
    data_siswa = []
    catatan = []

    with open(path, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris:
                continue

            bagian = baris.split(",")
            if len(bagian) != 2:
                catatan.append(f"Baris {nomor_baris} dilewati: format harus nama,nilai.")
                continue

            nama = bagian[0].strip()
            if not nama:
                catatan.append(f"Baris {nomor_baris} dilewati: nama belum diisi.")
                continue

            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                catatan.append(f"Baris {nomor_baris} dilewati: nilai bukan angka.")
                continue

            if not validasi_nilai(nilai):
                catatan.append(f"Baris {nomor_baris} dilewati: nilai harus 0 sampai 100.")
                continue

            data_siswa.append({"nama": nama, "nilai": nilai})

    return data_siswa, catatan
