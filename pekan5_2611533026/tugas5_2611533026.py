batas_3026 = int(input("Masukkan tinggi segitiga: "))
for i_3026 in range(1, batas_3026 + 1):
    for j_3026 in range(batas_3026 - i_3026):
        print(" ", end="")

    for k_3026 in range(i_3026):
        print("*", end=" ")
    print() #pindah ke baris berikutnya