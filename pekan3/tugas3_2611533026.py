print("=== SISTEM TRANSAKSI TOKO ===")
print()

# Input data pelanggan
nama_3026 = input("Masukkan Nama Pelanggan : ")
status_3026 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_3026 = int(input("Masukkan Total Belanja : "))
jumlah_barang_3026 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3026 = input("Masukkan Kode Promo : ")


# ==========================================
# OPERATOR PERBANDINGAN
# ==========================================

# Membandingkan total belanja dengan batas minimum
syarat_belanja_3026 = total_belanja_3026 >= 200000

# Membandingkan jumlah barang dengan batas minimum
syarat_barang_3026 = jumlah_barang_3026 >= 3

# Membandingkan status pelanggan
status_member_3026 = status_3026 == "member"


# ==========================================
# OPERATOR KEANGGOTAAN
# ==========================================

# List kode promo yang tersedia
daftar_promo_3026 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# Operator IN
promo_tersedia_3026 = kode_promo_3026 in daftar_promo_3026

# Operator NOT IN
promo_tidak_tersedia_3026 = kode_promo_3026 not in daftar_promo_3026


# ==========================================
# OPERATOR IDENTITAS
# ==========================================

# Mengikuti pola dari materi praktikum
objek1_3026 = daftar_promo_3026
objek2_3026 = objek1_3026
objek3_3026 = daftar_promo_3026.copy()

# Operator IS
identitas_sama_3026 = objek1_3026 is objek2_3026

# Operator IS NOT
identitas_berbeda_3026 = objek1_3026 is not objek3_3026


# ==========================================
# OPERATOR LOGIKA
# ==========================================

# AND: member dan belanja minimal Rp200.000
diskon_member_3026 = status_member_3026 and syarat_belanja_3026

# AND: jumlah barang minimal 3 dan kode promo tersedia
mendapatkan_promo_3026 = syarat_barang_3026 and promo_tersedia_3026

# OR: member atau memiliki promo
akses_pelanggan_3026 = status_member_3026 or promo_tersedia_3026

# NOT: bukan member
bukan_member_3026 = not status_member_3026


# ==========================================
# OPERATOR ARITMATIKA
# ==========================================

# Menghitung diskon 10% untuk member
if diskon_member_3026:
    diskon_3026 = total_belanja_3026 * 10 / 100
else:
    diskon_3026 = 0

# Menghitung total pembayaran
total_pembayaran_3026 = total_belanja_3026 - diskon_3026

# Menghitung rata-rata harga barang
rata_rata_3026 = total_belanja_3026 / jumlah_barang_3026

# Operator modulus
sisa_barang_3026 = jumlah_barang_3026 % 2


# ==========================================
# OPERATOR PENUGASAN
# ==========================================

poin_3026 = 0

# Augmented assignment +=
if diskon_member_3026:
    poin_3026 += 10

# Augmented assignment -=
total_pembayaran_3026 -= 0


# ==========================================
# OPERATOR BITWISE
# ==========================================

# 0001 = Member
# 0010 = Belanja >= Rp200.000
# 0100 = Jumlah Barang >= 3
# 1000 = Kode Promo Tersedia

kode_member_3026 = 1
kode_belanja_3026 = 2
kode_barang_3026 = 4
kode_promo_bit_3026 = 8

# Nilai awal kode status
kode_status_3026 = 0

# Operator OR (|) untuk menggabungkan kondisi
if status_member_3026:
    kode_status_3026 = kode_status_3026 | kode_member_3026

if syarat_belanja_3026:
    kode_status_3026 = kode_status_3026 | kode_belanja_3026

if syarat_barang_3026:
    kode_status_3026 = kode_status_3026 | kode_barang_3026

if promo_tersedia_3026:
    kode_status_3026 = kode_status_3026 | kode_promo_bit_3026


# Operator AND (&)
cek_member_3026 = kode_status_3026 & kode_member_3026
cek_promo_3026 = kode_status_3026 & kode_promo_bit_3026

# Operator XOR (^)
kode_referensi_3026 = 11
perbedaan_status_3026 = kode_status_3026 ^ kode_referensi_3026

# Operator shift <<
kode_shift_3026 = kode_status_3026 << 1


# ==========================================
# HAK AKSES
# ==========================================

member_access_3026 = cek_member_3026 != 0
promo_access_3026 = cek_promo_3026 != 0

# Hak free shipping jika member dan promo tersedia
free_shipping_access_3026 = status_member_3026 and promo_tersedia_3026


# ==========================================
# OUTPUT DATA TRANSAKSI
# ==========================================

print()
print()
print("=== DATA TRANSAKSI ===")

print("Nama Pelanggan       :", nama_3026)
print("Status Pelanggan     :", status_3026)
print("Total Belanja        : Rp" + str(total_belanja_3026))
print("Jumlah Barang        :", jumlah_barang_3026)
print("Kode Promo           :", kode_promo_3026)


# ==========================================
# HASIL VALIDASI
# ==========================================

print()
print()
print("=== HASIL VALIDASI ===")

print("Belanja >= Rp200000        :", syarat_belanja_3026)
print("Jumlah Barang >= 3         :", syarat_barang_3026)
print("Status Member              :", status_member_3026)
print("Kode Promo Tersedia        :", promo_tersedia_3026)
print("Mendapatkan Diskon         :", diskon_member_3026)
print("Mendapatkan Promo          :", mendapatkan_promo_3026)


# ==========================================
# HASIL PERHITUNGAN
# ==========================================

print()
print()
print("=== HASIL PERHITUNGAN ===")

print("Diskon                     : Rp" + str(int(diskon_3026)))
print("Total Pembayaran           : Rp" + str(int(total_pembayaran_3026)))
print("Rata-rata Harga Barang     : Rp" + str(int(rata_rata_3026)))


# ==========================================
# HAK AKSES PELANGGAN
# ==========================================

print()
print()
print("=== HAK AKSES PELANGGAN ===")

print("Kode Hak Akses             :", kode_status_3026)
print("Member Access              :", member_access_3026)
print("Promo Access               :", promo_access_3026)
print("Free Shipping Access       :", free_shipping_access_3026)


# ==========================================
# OPERASI BITWISE
# ==========================================

print()
print()
print("=== OPERASI BITWISE ===")

print("=== Kode Status Transaksi ===")
print()
print("0001 | 0010 | 0100 | 1000")
print()
print("Kode Biner   :", format(kode_status_3026, "b"))
print("Kode Desimal :", kode_status_3026)


# ==========================================
# PEMERIKSAAN STATUS
# ==========================================

print()
print("=== Pemeriksaan Status ===")

print()
print("Cek Member")
print()
print(format(kode_status_3026, "b"), "&", format(kode_member_3026, "04b"))
print()
print("Hasil Biner   :", format(cek_member_3026, "04b"))
print("Hasil Desimal :", cek_member_3026)


print()
print()
print("Cek Promo")
print()
print(format(kode_status_3026, "b"), "&", format(kode_promo_bit_3026, "04b"))
print()
print("Hasil Biner   :", format(cek_promo_3026, "04b"))
print("Hasil Desimal :", cek_promo_3026)


# ==========================================
# PERBANDINGAN STATUS
# ==========================================

print()
print("=== Perbandingan Status ===")
print()
print("Kode Transaksi :", format(kode_status_3026, "b"))
print()
print("Kode Referensi :", format(kode_referensi_3026, "04b"))
print()
print(format(kode_status_3026, "b"), "^", format(kode_referensi_3026, "04b"))
print()
print("Hasil Biner   :", format(perbedaan_status_3026, "04b"))
print("Hasil Desimal :", perbedaan_status_3026)


# ==========================================
# SHIFT
# ==========================================

print()
print("=== Shift ===")
print()
print(format(kode_status_3026, "b"), "<< 1")
print()
print("Hasil Biner   :", format(kode_shift_3026, "b"))
print("Hasil Desimal :", kode_shift_3026)


# ==========================================
# SELESAI
# ==========================================

print()
print("=== SELESAI ===")