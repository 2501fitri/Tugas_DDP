import math
def hitung_tabung(radius, tinggi):
# Menghitung luas permukaan tabung
    luas_permukaan = 2 * math.pi * radius * (radius + tinggi)
    
    # Menghitung keliling alas tabung
    keliling_alas = 2 * math.pi * radius
    
    return luas_permukaan, keliling_alas
def main():
    # Input dari pengguna
    radius = float(input("Masukkan jari-jari tabung (dalam satuan meter): "))
    tinggi = float(input("Masukkan tinggi tabung (dalam satuan meter): "))
    
    # Menghitung luas dan keliling
    luas_permukaan, keliling_alas = hitung_tabung(radius, tinggi)
    
    # Menampilkan hasil
    print(f"Luas permukaan tabung: {luas_permukaan:.2f} m²")
    print(f"Keliling alas tabung: {keliling_alas:.2f} m")

if __name__ == "__main__":
    main()
