
print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
print()

n_3026 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bingkai atas
print("#", end="")
for kolom_3026 in range(4 * n_3026 + 5):
    print("=", end="")
print("#")

# Fase 1: Jam pasir atas
for baris_3026 in range(n_3026, 0, -1):
    print("| ", end="")

    for spasi_3026 in range(2 * (n_3026 - baris_3026)):
        print(" ", end="")

    for angka_3026 in range(baris_3026, 0, -1):
        print(angka_3026, end=" ")

    print("<*>", end="")

    for angka_3026 in range(1, baris_3026 + 1):
        print(" " + str(angka_3026), end="")

    for spasi_3026 in range(2 * (n_3026 - baris_3026)):
        print(" ", end="")

    print(" |")

# Fase 2: Poros pusat
print("|", end="")

for spasi_3026 in range(2 * n_3026 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_3026 in range(2 * n_3026 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bawah
for baris_3026 in range(1, n_3026 + 1):
    print("| ", end="")

    for spasi_3026 in range(2 * (n_3026 - baris_3026)):
        print(" ", end="")

    for angka_3026 in range(baris_3026, 0, -1):
        print(angka_3026, end=" ")

    print("<*>", end="")

    for angka_3026 in range(1, baris_3026 + 1):
        print(" " + str(angka_3026), end="")

    for spasi_3026 in range(2 * (n_3026 - baris_3026)):
        print(" ", end="")

    print(" |")

# Bingkai bawah
print("#", end="")
for kolom_3026 in range(4 * n_3026 + 5):
    print("=", end="")
print("#")