print("================================")
print("3. OPERATOR BITWISE")
print("================================")

angka1_3026 = int(input("Input angka bitwise-1: "))
angka2_3026 = int(input("Input angka bitwise-2: "))

print("\n Angka dalam bentuk desimal dan biner ")
print("angka1 =", angka1_3026, "| biner", bin(angka1_3026))
print("angka2 =", angka2_3026, "| biner", bin(angka2_3026))

#Bitwise AND
hasil_3026 = angka1_3026 & angka2_3026
print("\n Operator Bitwise AND (&)")
print(angka1_3026, "&", angka2_3026, "=", hasil_3026)
print("Biner hasil =", bin(hasil_3026))
print("Biner hasil (8 bit) =", format(hasil_3026, "08b"))

#Bitwise OR
hasil_3026 = angka1_3026 | angka2_3026
print("\n Bitwise OR (|)")
print(angka1_3026, "|", angka2_3026, "=", hasil_3026)
print("biner hasil =", bin(hasil_3026))
print("Biner hasil (8 bit) =", format(hasil_3026, "08b"))

#Bitwise XOR
hasil_3026 = angka1_3026 ^ angka2_3026
print("\n Bitwise XOR (^)")
print(angka1_3026, "^", angka2_3026, "=", hasil_3026)
print("biner hasil =", bin(hasil_3026))
print("Biner hasil (8 bit) =", format(hasil_3026, "08b"))

#Bitwise NOT
hasil_3026 = ~angka1_3026
print("\n Bitwise NOT (~)")
print("~", angka1_3026,"=", hasil_3026)
print("biner hasil =", bin(hasil_3026))
print("Biner hasil (8 bit) =", format(hasil_3026, "08b"))

#Bitwise geser kiri
jumlah_geser_3026 = int(input("\n Masukkan jumlah pergeseran bit: "))

hasil_3026 = angka1_3026 << jumlah_geser_3026
print("\n Bitwise geser kiri (<<)")
print(angka1_3026, "<<", jumlah_geser_3026, "=", hasil_3026)
print("biner hasil =", bin(hasil_3026))
print("Biner hasil (8 bit) =", format(hasil_3026, "08b"))

#Bitwise geser kanan
hasil_3026 = angka1_3026 >> jumlah_geser_3026
print("\n Bitwise geser kanan (>>)")
print(angka1_3026, ">>", jumlah_geser_3026, "=", hasil_3026)
print("biner hasil =", bin(hasil_3026))
print("Biner hasil (8 bit) =", format(hasil_3026, "08b"))