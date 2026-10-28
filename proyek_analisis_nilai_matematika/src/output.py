def buat_laporan(statistik, data_siswa, kkm):
    """Menyusun laporan sebagai string."""
    baris = [
        "LAPORAN ANALISIS NILAI MATEMATIKA",
        "=" * 36,
        f"KKM: {kkm}",
        f"Jumlah siswa valid: {statistik['jumlah']}",
    ]

    if statistik["jumlah"] == 0:
        baris.append("Tidak ada data valid untuk dianalisis.")
        return "\n".join(baris)

    baris.extend([
        f"Rata-rata: {statistik['rata_rata']:.2f}",
        f"Nilai minimum: {statistik['minimum']:g}",
        f"Nilai maksimum: {statistik['maksimum']:g}",
        f"Jumlah tuntas: {statistik['tuntas']}",
        f"Jumlah belum tuntas: {statistik['belum_tuntas']}",
        "",
        "Rincian siswa:",
    ])

    for siswa in data_siswa:
        status = "Tuntas" if siswa["nilai"] >= kkm else "Belum tuntas"
        baris.append(f"- {siswa['nama']}: {siswa['nilai']:g} ({status})")

    return "\n".join(baris)


def tampilkan_laporan(laporan):
    """Menampilkan laporan ke terminal."""
    print()
    print(laporan)


def simpan_laporan(path, laporan):
    """Menyimpan laporan ke file teks."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        file.write(laporan + "\n")
