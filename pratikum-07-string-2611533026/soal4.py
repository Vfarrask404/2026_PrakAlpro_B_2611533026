# Nama : Vania Farras Kalista
# NIM : 2611533026
# Question 4

phone = "082611533026"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:] # farras note : kenapa dikurang 7? krn ada 7 digit yang ditampilkan, jadinya jumlah bintang sesuai dengan panjang digit angkanya
print(masked)