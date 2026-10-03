ulang_3026 = int(input("Masukkan nilai batas: "))

jumlah_3026 = 0
for i_3026 in range(1, ulang_3026 + 1):
    if i_3026 % 2 == 0:
        print(i_3026, end=" " )
        jumlah_3026 += i_3026

        if i_3026 < ulang_3026:
            print("+", end=" ")

        else:
            print("=", jumlah_3026)

print()
print("Jumlah =", jumlah_3026)