#Deklarasi variabel dengan tipe data boolean
is_lulus_3026 = True
is_cumlaude_3026 = True

#Menggunakan Boolean
nilai_3026 = 85
Batas_lulus_3026 = 75

#Menentukan nilai Boolean dari kondisi
status_kelulusan_3026 = nilai_3026 >= Batas_lulus_3026 #hasilnya True karena 85 lebih besar dari 75

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3026)
print("Apakah lulus?", status_kelulusan_3026)

if is_lulus_3026 and is_cumlaude_3026:
    print("Selamat, Anda lulus dengan predikat Cumlaude!!")