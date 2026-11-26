n = int(input())
kas = {}

# farras note : input & menjumlahkan setoran
for _ in range(n):
    data = input().split()
    nama = data[0]
    nominal = int(data[1])
    kas[nama] = kas.get(nama, 0) + nominal

# farras note : Menampilkan rekap setoran
for nama, total in kas.items():
    print(f"{nama}: {total}")

# farras note : Menghitung total kas dan mencari penyetor terbesar
print(f"Total cash: {sum(kas.values())}")

top_name = ""
top_amount = 0

for nama, total in kas.items():
    if total > top_amount:
        top_name = nama
        top_amount = total

print(f"Top contributor: {top_name} ({top_amount})")