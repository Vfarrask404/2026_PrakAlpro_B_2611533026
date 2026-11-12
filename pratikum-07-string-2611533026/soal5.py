# Nama : Vania Farras Kalista
# NIM : 2611533026
# Question 5

#peringatan dari farras:
#kalau ingin menjalankan program ini,
#tambahkan atau hapus tanda pagar (#)
#pada bagian A atau B sesuai dengan kebutuhan.

#bagian A :
#program jawaban farras :
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

#bagian B :
#program jawaban farras
nim = input("Masukkan NIM: ")

if len(nim) == 10 and nim.isdigit():
    intake_year = "20" + nim[:2]
    print("Valid")
    print("Intake year:", intake_year)
else:
    print("Invalid NIM")