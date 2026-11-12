# Nama : Vania Farras Kalista
# NIM : 2611533026
# Question 7

name = "vania farras kalista"
nim = "2610511023"

clean_name = name.strip()
space = clean_name.find(" ")

if space == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space]

#farras note : Membuat username
username = first_name.lower() + nim[-3:]

# farras note : Mengambil angkatan dari NIM
intake = "20" + nim[:2]

# farras note : Menampilkan kartu mahasiswa
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)

print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")

print("=" * 30)