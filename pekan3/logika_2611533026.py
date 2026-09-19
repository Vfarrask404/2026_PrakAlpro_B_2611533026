#program operator 

#memasukkan nilai boolean
#input tidak peka terhadap huruf besar dan kecil
a1_3026 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3026 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"
# .strip(): Menghapus spasi atau karakter kosong di awal dan akhir teks -> "  true  " menjadi "true"
# .lower(): Mengubah semua huruf dalam teks menjadi huruf kecil -> "TRUE" atau "True" menjadi "true"
# == "true": Ini adalah proses evaluasi (perbandingan). Python akan memeriksa apakah teks yang sudah 
# dibersihkan tadi sama persis dengan kata "true" Jika sama, bagian ini menghasilkan nilai Boolean True.
# Jika berbeda (misalnya pengguna mengetik "false", "bukan", atau mengosongkannya), bagian ini menghasilkan nilai Boolean False.

print("\nA1 =", a1_3026)
print("A2 =", a2_3026)

#Kongjungsi : bernilai True jika keduanya True
hasil_3026 = a1_3026 and a2_3026
print("\nKongjungsi (AND)")
print("A1 and A2 =", hasil_3026)

#Disjungsi : bernilai True jika salah satu True
hasil_3026 = a1_3026 or a2_3026
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3026)

#Negasi A1 : membalikkan nilai A1
hasil_3026 = not a1_3026
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3026)

#Negasi A2 : membalikkan nilai A2
hasil_3026 = not a2_3026
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3026)

#XOR : bernilai True jika kedua nilai berbeda
hasil_3026 = a1_3026 != a2_3026
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3026)