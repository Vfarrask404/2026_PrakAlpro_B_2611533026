<<<<<<< HEAD
correct_pin = "1234"
pin = input("Enter PIN: ")

if pin == correct_pin: 
        print("Access granted")
else:
    attempt = 1
    MAX_ATTEMPTS = 3
    while pin != correct_pin and attempt < MAX_ATTEMPTS:
        print("Incorrect PIN.")
        pin = input("Enter PIN: ")
        attempt += 1
=======
correct_pin = "1234"
pin = input("Enter PIN: ")

if pin == correct_pin: 
        print("Access granted")
else:
    attempt = 1
    MAX_ATTEMPTS = 3
    while pin != correct_pin and attempt < MAX_ATTEMPTS:
        print("Incorrect PIN.")
        pin = input("Enter PIN: ")
        attempt += 1
>>>>>>> d513a3c7d3c481cf73fbdd8f20342f85fe658638
    print("Account locked")