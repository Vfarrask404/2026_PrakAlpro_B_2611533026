#Buat program untuk operator aritmatika dalam python
#Program ini menggunakan fungsi input()
#Nilai yang dimasukkan akan dikonversi menjadi tipe data interger

#TEMPAT MENGIMPUT ANGKA
angka1_3026 = int(input("Input angka-1: "))
angka2_3026 = int(input("Input angka-2: "))

#PENJUMLAHAN
hasil_3026 = angka1_3026 + angka2_3026
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3026)

#PENGURANGAN
hasil_3026 = angka1_3026 - angka2_3026
print("\nOperator Pengurangan")
print("Hasil =", hasil_3026)

#PERKALIAN
hasil_3026 = angka1_3026 * angka2_3026
print("\nOperator Perkalian")
print("Hasil =", hasil_3026)

#PEMBAGIAN
if angka2_3026 != 0:
    hasil_3026 = angka1_3026 / angka2_3026
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3026)

#PEMBAGIAN BULAT
    hasil_3026 = angka1_3026 // angka2_3026
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3026)

#SISA BAGI
    hasil_3026 = angka1_3026 % angka2_3026
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3026)

#KASUS KALAU DIBAGI 0
else:
    print("\nOperator Pembagian")
    print("Angka kedua tidak boleh bernilai 0.")

#PANGKAT
hasil_3026 = angka1_3026 ** angka2_3026
print("\nOperator Pangkat")
print("Hasil =", hasil_3026)