def tampilkan_data(data):
    if not data:
        print("Belum ada data mahasiswa")
        return

    for mahasiswa in data:
        print("-------------------------")
        print("NIM  :", mahasiswa["nim"])
        print("Nama :", mahasiswa["nama"])
        print("Prodi:", mahasiswa["prodi"])