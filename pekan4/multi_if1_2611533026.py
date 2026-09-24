umur_3026 = int(input("input umur anda : "))
sim_3026 = input("Apakah anda udah punya SIM C (y/t): ") [0]

if umur_3026 >= 17 and sim_3026 == 'y' :
    print("anda sudah dewasa dan boleh bawa motor")

if umur_3026 >= 17 and sim_3026 != 'y' :
    print("anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3026 < 17 and sim_3026 == 'y' :
    print("anda belum cukup umur punya SIM")

if umur_3026 < 17 and sim_3026 != 'y' :
    print ("anda belum cukup umur bawa motor")