batas_3026 = int(input("Masukkan nilai batas: "))
for line_3026 in range(1, batas_3026 + 1):
    for column_3026 in range(1, (-1 * line_3026 + batas_3026 )+ 1):
        print(column_3026, end=" ")
    print(line_3026)