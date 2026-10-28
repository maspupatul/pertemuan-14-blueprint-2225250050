def hitung_statistik(data_siswa, kkm=75):
    """Menghitung statistik nilai dan jumlah siswa tuntas/belum tuntas."""
    if not data_siswa:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "tuntas": 0,
            "belum_tuntas": 0,
        }

    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]
    jumlah_tuntas = sum(1 for nilai in daftar_nilai if nilai >= kkm)

    return {
        "jumlah": len(daftar_nilai),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "tuntas": jumlah_tuntas,
        "belum_tuntas": len(daftar_nilai) - jumlah_tuntas,
    }
