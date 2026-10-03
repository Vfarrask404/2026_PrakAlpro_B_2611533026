tinggi_3026 = int(input("masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3026 % 2 != 0:
    print("Masukkan bilangan genap!!")
else:
    a_3026 = tinggi_3026 
    c_3026 = a_3026
    lebar_3026 = (2*tinggi_3026) - 2

    for i_3026 in range(1, tinggi_3026 + 1):
        b_3026 = c_3026 + 1

        for j_3026 in range(1, tinggi_3026 + 1):
            b_3026 = c_3026 + 1

            for j_3026 in range(1, lebar_3026 + 1):

                #Baris atas dan bawah
                if i_3026 == 1 or i_3026 == tinggi_3026:
                    if j_3026 == 1 or j_3026 == lebar_3026:
                        print("#", end="")
                else:
                    print("=", end="")

                #Baris isi
            else :
                if j_3026 == 1 or j_3026 == lebar_3026:
                    print("|", end="")
                else:
                    if j_3026 == c_3026 :
                        print("<", end="")
                    elif j_3026 == b_3026 :
                        print(">", end="")
                    elif j_3026 == (lebar_3026 - c_3026) :
                        print("<", end="")
                    elif j_3026 == (lebar_3026 - c_3026 + 1) :
                        print(">", end="")
                    elif j_3026 > b_3026 and j_3026 < (lebar_3026 - c_3026) :
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        #logika asli java
        a_3026 -= 2

        if a_3026 <= 0:
            c_3026 = (-a_3026) + 2
        else:
            c_3026 = a_3026