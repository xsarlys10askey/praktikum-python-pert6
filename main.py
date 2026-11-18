from utilitas_akademik import (
    hitung_ipk,
    konversi_nilai_huruf,
    generate_transkrip
)

nama = "Keysha"
nilai = [85, 90, 80]

if __name__ == "__main__":
    hasil = generate_transkrip(nama, nilai)

    print("=== TRANSKRIP NILAI ===")
    print("Nama:", hasil["nama"])
    print("Nilai:", hasil["nilai"])
    print("Nilai Huruf:", hasil["nilai_huruf"])
    print("IPK:", round(hasil["ipk"], 2))