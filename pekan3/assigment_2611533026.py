#program operator assignment dalam python

angka1_3026 = int(input("Input angka-1: "))
angka2_3026 = int(input("Input angka-2: "))

print("\n Nilai awal angka-1 =", angka1_3026)
print("Nilai awal angka-2 =", angka2_3026)

# Assignment biasa
hasil_3026 = angka1_3026
print("\n Assignment biasa (=)")
print("Hasil =", hasil_3026)

# Assignment penjumlahan
hasil_3026 = angka1_3026
hasil_3026 += angka2_3026
print("\n Assignment penjumlahan (+=)")
print("Hasil =", hasil_3026)

# Assignment pengurangan
hasil_3026 = angka1_3026
hasil_3026 -= angka2_3026
print("\n Assignment pengurangan (-=)")
print("Hasil =", hasil_3026)

# Assignment perkalian
hasil_3026 = angka1_3026
hasil_3026 *= angka2_3026
print("\n Assignment perkalian (*=)")
print("Hasil =", hasil_3026)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3026 != 0:
    hasil_3026 = angka1_3026
    hasil_3026 /= angka2_3026
    print("\n Assignment pembagian (/=)")
    print("Hasil =", hasil_3026)

    #operator tambahan
    hasil_3026 = angka1_3026
    hasil_3026 //= angka2_3026
    print("\n Assignment pembagian bulat (//=)")
    print("Hasil =", hasil_3026)

    hasil_3026 = angka1_3026
    hasil_3026 %= angka2_3026
    print("\n Assignment sisa bagi (%=)")
    print("Hasil =", hasil_3026)

else:
    print("\n Pembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan : Assignment perpangkatan
hasil_3026 = angka1_3026
hasil_3026 **= angka2_3026
print("\n Assignment perpangkatan (**=)")
print("Hasil =", hasil_3026)