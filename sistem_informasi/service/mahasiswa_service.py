from sistem_informasi.model.mahasiswa import buat_mahasiswa

# Penyimpanan data mahasiswa
data_mahasiswa = {}


# Menambahkan mahasiswa
def tambah_mahasiswa(nim, nama, prodi):
    if nim in data_mahasiswa:
        return "NIM sudah terdaftar"

    data_mahasiswa[nim] = buat_mahasiswa(nim, nama, prodi)
    return "Data mahasiswa berhasil ditambahkan"


# Menampilkan semua mahasiswa
def lihat_mahasiswa():
    return list(data_mahasiswa.values())


# Mengubah data mahasiswa
def ubah_mahasiswa(nim, nama, prodi):
    if nim not in data_mahasiswa:
        return "Data mahasiswa tidak ditemukan"

    data_mahasiswa[nim]["nama"] = nama
    data_mahasiswa[nim]["prodi"] = prodi

    return "Data mahasiswa berhasil diubah"


# Menghapus data mahasiswa
def hapus_mahasiswa(nim):
    if nim not in data_mahasiswa:
        return "Data mahasiswa tidak ditemukan"

    del data_mahasiswa[nim]
    return "Data mahasiswa berhasil dihapus"