#program operator 

#memasukkan niali boolean
#input tidak peka terhadap huruf besar dan kecil
a1_3026 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3026 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\n A1 =", a1_3026)
print(" A2 =", a2_3026)

#Kongjungsi : bernilai True jika keduanya True
hasil_3026 = a1_3026 and a2_3026
print("\n Kongjungsi (AND)")
print("A1 and A2 =", hasil_3026)

#Disjungsi : bernilai True jika salah satu True
hasil_3026 = a1_3026 or a2_3026
print("\n Disjungsi (OR)")
print("A1 or A2 =", hasil_3026)

#Negasi A1 : membalikkan nilai A1
hasil_3026 = not a1_3026
print("\n Negasi A1 (NOT)")
print("not A1 =", hasil_3026)

#Negasi A2 : membalikkan nilai A2
hasil_3026 = not a2_3026
print("\n Negasi A2 (NOT)")
print("not A2 =", hasil_3026)

#XOR : bernilai True jika kedua nilai berbeda
hasil_3026 = a1_3026 != a2_3026
print("\n Disjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3026)