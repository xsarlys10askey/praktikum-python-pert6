
import requests
import json


# Mengambil data dari API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Mengambil nama dan email menggunakan map
    hasil = list(map(
        lambda user: {
            "nama": user["name"],
            "email": user["email"],
            "kota": user["address"]["city"]
        },
        data
    ))

    # Menyaring pengguna dari kota tertentu
    data_filter = list(filter(
        lambda user: user["kota"] == "Gwenborough",
        hasil
    ))

    # Mengurutkan data berdasarkan nama
    data_urut = sorted(
        hasil,
        key=lambda user: user["nama"]
    )

    # Menggabungkan hasil analisis
    hasil_analisis = {
        "total_pengguna": len(data),
        "data_pengguna": hasil,
        "pengguna_gwenborough": data_filter,
        "data_urut_nama": data_urut
    }

    # Menyimpan hasil ke file JSON
    with open("hasil_analisis.json", "w") as file:
        json.dump(hasil_analisis, file, indent=4)

    print("Data berhasil diambil dari API!")
    print("Total pengguna:", len(data))
    print("Pengguna dari Gwenborough:", len(data_filter))
    print("Data berhasil disimpan ke hasil_analisis.json")

else:
    print("Gagal mengambil data dari API")
    print("Status code:", response.status_code)


if __name__ == "__main__":
    print("=== PROGRAM ANALISIS DATA API ===")
