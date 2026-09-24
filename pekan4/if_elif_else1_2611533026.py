umur_3026 = int(input("input umur anda : "))
sim_3026 = input("Apakah anda udah punya SIM C: ") [0] # guna [0] -> array -> liat diawal aja sehingga selama "y" diawal akan tetap benar

if umur_3026 >= 17 and sim_3026 == 'y' :
    print("anda sudah dewasa dan boleh bawa motor")

elif umur_3026 >= 17 and sim_3026 != 'y' :
    print("anda sudah dewasa tetapi tidak boleh bawa motor")

elif umur_3026 < 17 and sim_3026 == 'y' :
    print("anda belum cukup umur punya SIM")

else :
    print ("anda belum cukup umur bawa motor")