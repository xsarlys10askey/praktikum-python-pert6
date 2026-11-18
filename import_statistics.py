import statistics

def hitung_statistik(data):
    hasil = {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "modus": statistics.mode(data),
        "range": max(data) - min(data),
        "standard_deviation": statistics.stdev(data)
    }

    return hasil

angka = [70, 75, 80, 80, 85, 90]

hasil = hitung_statistik(angka)

print("Hasil Statistik:")
print(f"Mean               : {hasil['mean']}")
print(f"Median             : {hasil['median']}")
print(f"Modus              : {hasil['modus']}")
print(f"Range              : {hasil['range']}")
print(f"Standard Deviation : {hasil['standard_deviation']}")