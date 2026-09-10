#Program ini menggunakan konstanta untuk menghitung luas lingkaran

from typing import Final
PI: Final[float] = 3.14  # konstanta phi
print("pi: %f" % (PI))
jari_3026 = float(input('Masukkan nilai jari-jari:'))
luas_3026 = PI * jari_3026* jari_3026
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3026, luas_3026))