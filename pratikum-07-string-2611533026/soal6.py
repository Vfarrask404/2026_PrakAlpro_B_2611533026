# Nama : Vania Farras Kalista
# NIM : 2611533026
# Question 6

#pemanasan
# first_name = " muhammad"
# last_name = "rafi "
# full_name = first_name.strip() + " " + last_name.strip()
# print(full_name)
# print(full_name.title())

#program jawaban masalah
full_name = "Vania Farras Kalista"
nim = "2611533026"

clean_name = full_name.strip()
space = clean_name.find(" ") # Mencari posisi spasi pertama

# Mengambil nama depan
if space == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space]

username = first_name.lower() + nim[-3:]
print(username)