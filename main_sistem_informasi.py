from sistem_informasi.service.mahasiswa_service import (
    tambah_mahasiswa,
    lihat_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa
)

from sistem_informasi.utils.helper import tampilkan_data


if __name__ == "__main__":

    # Create
    print("=== TAMBAH MAHASISWA ===")
    print(tambah_mahasiswa("23032", "Keysha", "Informatika"))
    print(tambah_mahasiswa("23033", "Reswan", "Sistem Informasi"))

    # Read
    print("\n=== DATA MAHASISWA ===")
    tampilkan_data(lihat_mahasiswa())

    # Update
    print("\n=== UBAH DATA MAHASISWA ===")
    print(ubah_mahasiswa("23032", "Keysha Aprilya", "Informatika"))

    tampilkan_data(lihat_mahasiswa())

    # Delete
    print("\n=== HAPUS DATA MAHASISWA ===")
    print(hapus_mahasiswa("23033"))

    # Menampilkan data setelah dihapus
    print("\n=== DATA TERAKHIR ===")
    tampilkan_data(lihat_mahasiswa())