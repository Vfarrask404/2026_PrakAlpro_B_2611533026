#program operator assignment dalam python

#TEMPAT INPUT ANGKA
angka1_3026 = int(input("Input angka-1: "))
angka2_3026 = int(input("Input angka-2: "))

print("\nNilai awal angka-1 =", angka1_3026)
print("Nilai awal angka-2 =", angka2_3026)

#Assignment biasa
hasil_3026 = angka1_3026
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3026)

#Assignment penjumlahan
hasil_3026 = angka1_3026
hasil_3026 += angka2_3026
print("\nAssignment penjumlahan (+=)")
print("Hasil =", hasil_3026)

#Assignment pengurangan
hasil_3026 = angka1_3026
hasil_3026 -= angka2_3026
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3026)

#Assignment perkalian
hasil_3026 = angka1_3026
hasil_3026 *= angka2_3026
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3026)

#Assignment pembagian
if angka2_3026 != 0:
    hasil_3026 = angka1_3026
    hasil_3026 /= angka2_3026
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3026)

    #Assignment pembagian bulat
    hasil_3026 = angka1_3026
    hasil_3026 //= angka2_3026
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3026)

#Assignment sisa bagi
    hasil_3026 = angka1_3026
    hasil_3026 %= angka2_3026
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3026)

#Assignment kasus jika di bagi 0 atau angka kedua 0
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

#Assignment perpangkatan
hasil_3026 = angka1_3026
hasil_3026 **= angka2_3026
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3026)