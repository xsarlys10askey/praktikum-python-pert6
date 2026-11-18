def konversi_nilai_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"

def hitung_ipk(nilai):
    total = 0

    for n in nilai:
        if n >= 85:
            total += 4.0
        elif n >= 80:
            total += 3.0
        elif n >= 70:
            total += 2.0
        elif n >= 60:
            total += 1.0
        else:
            total += 0.0

    return total / len(nilai)

def generate_transkrip(nama, nilai):
    transkrip = {
        "nama": nama,
        "nilai": nilai,
        "nilai_huruf": [
            konversi_nilai_huruf(n) for n in nilai
        ],
        "ipk": hitung_ipk(nilai)
    }

    return transkrip

if __name__ == "__main__":
    print(hitung_ipk([85, 90, 80]))