# Nama : Vania Farras Kalista
# NIM : 2611533026
# Question bonus
text = input("Masukkan kata atau kalimat: ")
text = text.replace(" ", "").lower() #farras note : biar bisa dibandingkan, semua huruf diubah menjadi huruf kecil dan spasi dihapus

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")