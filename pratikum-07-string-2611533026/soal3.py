# Nama : Vania Farras Kalista
# NIM : 2611533026
# Question 3

#Bagian A (kode perbaikannya)
text = "Informatika"
print(text[-1])
print(text.upper())
print(text[0:20])

#Bagian B (kode perbaikannya)
text = "Vania Farras Kalista"
count = 0
for char in text:
    if char in "AIUEOaiueo" :
        count += 1
print("Vowels:", count)