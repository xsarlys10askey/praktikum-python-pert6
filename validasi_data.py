def validasi_data(data, schema, *args, **kwargs):
    errors = []

    # Memeriksa data yang wajib diisi
    for field in args:
        if field not in data:
            errors.append(f"{field} wajib diisi")

    # Mengambil pengaturan tambahan
    allow_extra = kwargs.get("allow_extra", True)

    # Memeriksa setiap aturan dalam schema
    for field, aturan in schema.items():
        if field not in data:
            continue

        nilai = data[field]
        tipe = aturan.get("type")

        # Memeriksa tipe data
        if tipe and not isinstance(nilai, tipe):
            errors.append(f"{field} harus bertipe {tipe.__name__}")
            continue

        # Memeriksa batas minimum
        if "min" in aturan and nilai < aturan["min"]:
            errors.append(f"{field} minimal {aturan['min']}")

        # Memeriksa batas maksimum
        if "max" in aturan and nilai > aturan["max"]:
            errors.append(f"{field} maksimal {aturan['max']}")

    # Memeriksa apakah ada data tambahan
    if not allow_extra:
        for field in data:
            if field not in schema:
                errors.append(f"{field} tidak ada dalam schema")

    is_valid = len(errors) == 0

    return is_valid, errors


# Aturan validasi data mahasiswa
schema_mahasiswa = {
    "nama": {"type": str},
    "umur": {"type": int, "min": 17, "max": 60},
    "ipk": {"type": (int, float), "min": 0, "max": 4}
}

# Contoh data mahasiswa
data_mahasiswa = {
    "nama": "Andi",
    "umur": 15,
    "ipk": 4.5
}

# Menjalankan validasi
is_valid, errors = validasi_data(
    data_mahasiswa,
    schema_mahasiswa,
    "nama", "umur", "ipk",
    allow_extra=False
)

print("Hasil Validasi Data:")
print("Status Valid:", is_valid)
print("Errors:", errors)