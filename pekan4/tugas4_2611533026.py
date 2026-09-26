print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input data pengunjung
nama_pengunjung_3026 = input("Masukkan Nama Pengunjung : ")
umur_3026 = int(input("Input umur anda : "))
sim_3026 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0] .strip().lower()

# Pilihan paket wahana
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

pilihan_paket_3026 = int(input("Masukkan nomor paket (1-5) : "))

# Pemilihan wahana menggunakan match-case
match pilihan_paket_3026:
    case 1:
        nama_wahana_3026 = "Safari Rimba"
        harga_satuan_3026 = 50000

    case 2:
        nama_wahana_3026 = "Arung Jeram"
        harga_satuan_3026 = 75000

    case 3:
        nama_wahana_3026 = "Motor ATV Ekstrim"
        harga_satuan_3026 = 120000

    case 4:
        nama_wahana_3026 = "Roller Coaster Kilat"
        harga_satuan_3026 = 100000

    case 5:
        nama_wahana_3026 = "All-Access VIP"
        harga_satuan_3026 = 220000

    case _:
        print("Paket wahana tidak valid!")
        exit()

jumlah_tiket_3026 = int(input("Masukkan jumlah tiket           : "))
is_member_3026 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_3026 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Validasi jumlah tiket
if jumlah_tiket_3026 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")


# Validasi kelayakan pengendara wahana
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

# Khusus Paket 3 (Motor ATV Ekstrim)
if pilihan_paket_3026 == 3 and umur_3026 >= 17 and sim_3026 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")

elif pilihan_paket_3026 == 3 and umur_3026 >= 17 and sim_3026 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")

elif pilihan_paket_3026 == 3 and umur_3026 < 17 and sim_3026 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")

elif pilihan_paket_3026 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")

# Untuk paket selain 3
elif umur_3026 >= 10:
    print("Status Akses: Umur memenuhi syarat untuk wahana.")

else:
    print("Status Akses: Umur belum memenuhi syarat untuk wahana.")

# Menghitung subtotal
subtotal_3026 = harga_satuan_3026 * jumlah_tiket_3026

# Total diskon awal
total_diskon_persen_3026 = 0

# Multi-if terpisah untuk diskon akumulatif
#Diskon Belanja Besar
if subtotal_3026 >= 200000:
    total_diskon_persen_3026 += 10

#Diskon Member
if is_member_3026 in ['y', 'ya']:
    total_diskon_persen_3026 += 5

#Diskon Voucher Promo
if kode_promo_valid_3026 in ['y', 'ya']:
    total_diskon_persen_3026 += 15

#Diskon Tambahan Rombongan
if jumlah_tiket_3026 >= 5:
    total_diskon_persen_3026 += 5

# Menghitung nominal diskon
nominal_diskon_3026 = subtotal_3026 * (total_diskon_persen_3026 / 100)

# Menghitung total bayar
total_bayar_3026 = subtotal_3026 - nominal_diskon_3026

# Evaluasi bonus
if total_bayar_3026 > 300000:
    catatan_layanan_3026 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3026 = "Terima kasih telah berkunjung."

# Menampilkan rincian pembayaran
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3026:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3026}% (Rp {nominal_diskon_3026:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3026:,.0f}")
print("Catatan Layanan  :", catatan_layanan_3026)
print("Program Selesai")