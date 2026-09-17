#Program operator keanggotaan dan idetitas dalam python

print("=====================================")
print("1. OPERATOR KEANGGOTAAN")
print("=====================================")

#input beberapa data yang dipisahkan dengan koma
input_data_3026 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

#Mengubah input menjadi list integer
data_3026 = [int(angka.strip()) for angka in input_data_3026.split(",")]

nilai_dicari_3026 = int(input("Masukkan nilai yang ingin dicari: "))

# Operator in
hasil_3026 = nilai_dicari_3026 in data_3026
print("\nOperator keanggotaan IN")
print(nilai_dicari_3026, "in", data_3026, "=", hasil_3026)

#operator not in
hasil_3026 = nilai_dicari_3026 not in data_3026
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3026, "not in", data_3026, "=", hasil_3026)

print("\n=====================================")
print("2. OPERATOR IDENTITAS")
print("=====================================")

#objek1 menggunakan list dari input pengguna
objek1_3026 = data_3026

#objek2 merujuk pada objek yang sama dengan objek1
objek2_3026 = objek1_3026

#objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3026 = data_3026.copy()

print("objek1 =", objek1_3026)
print("objek2 =", objek2_3026)
print("objek3 =", objek3_3026)

# Operator is
hasil_3026 = objek1_3026 is objek2_3026
print("\n Operator identitas IS")
print("objek1 is objek2 =", hasil_3026)

# Operator is not
hasil_3026 = objek1_3026 is not objek3_3026
print("\n Operator identitas IS NOT")
print("objek1 is not objek3 =", hasil_3026)

#Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai:")
print("objek1 is objek3:", objek1_3026 is objek3_3026)
print("objek1 == objek3:", objek1_3026 == objek3_3026)