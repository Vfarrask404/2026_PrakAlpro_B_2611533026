from typing import Final

# Konstanta batas kelulusan
BATAS_LULUS: Final[float] = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# Input data praktikan
nama_3026 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3026 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3026 = int(input("Masukkan Umur : "))
nilai_3026 = float(input("Masukkan Skor Tes Awal : "))

# Alamat domisili multiline
alamat_3026 = "Griya insani, Jl Durian tarung,Padang"

# Token identifikasi berupa bilangan kompleks
token_3026 = 100 + 3j

# Evaluasi status kelulusan
lulus_3026 = nilai_3026 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print("Nama Mahasiswa :", nama_3026, "| Tipe:", type(nama_3026))

print("Alamat Domisili:")
print(alamat_3026, "| Tipe:", type(alamat_3026))

print("Umur :", umur_3026, "tahun | Tipe:", type(umur_3026))
print("Skor Tes Awal :", nilai_3026, "| Tipe:", type(nilai_3026))
print("ID Token Sinyal:", token_3026, "| Tipe:", type(token_3026))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", lulus_3026, "| Tipe:", type(lulus_3026))