#program menghitung diskon belanja

#input user
total_belanja_3026 = float(input("Masukkan total belanja (Rp) : "))

#input status member (mengecek apakah user mengetik 'y" atau 'ya')
input_member_3026 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_3026 = input_member_3026 in ["y", "ya"]

# input status kode promo (mengecek apakah user mengetik 'y' atau 'ya)
input_promo_3026 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3026 = input_promo_3026 in ["y", "ya"]

total_diskon_persen_3026 = 0

if total_belanja_3026 > 1000000 :
    total_diskon_persen_3026 += 10 # diskon belanja besar

    if is_member_3026 :
        total_diskon_persen_3026 += 5 #diskon member

        if kode_promo_valid_3026 :
            total_diskon_persen_3026 += 15 #diskon voucher

#menghitung nominal diskon dan total bayar
nominal_diskon_3026 = total_belanja_3026 * (total_diskon_persen_3026 / 100)
total_bayar_3026 = total_belanja_3026 - nominal_diskon_3026

#output hasil
print("\n---Rincian Pembayaran---")
print(f"total diskon :  {total_diskon_persen_3026}% (Rp {nominal_diskon_3026 :,0f})")
print(f"Total Bayar : Rp {total_bayar_3026:,0f}")

print(f"Total diskon yang anda dapatkan :  {total_diskon_persen_3026}%")
#output :total diskon yang anda dapatkan : 30% jika belanja > 1 juta, member, dan kode promo valid