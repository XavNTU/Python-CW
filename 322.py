def AirportMenu():
    print("Airport Flight Arrival Menu")
    print("[1] Check Flight Arrival Status")
    print("[2] ")
    print("[3] ")

def SubMenu():
    print("Submenu")

while True:
    AirportMenu()
    option = int(input("Enter your choice (1/2/3:) "))

    if option == 1:
        print("Your Flight number is 5.")
        while True:
            SubMenu()
            sub_choice = input("eNTER YOUR CHOICE")
    elif option == 2:
        print("Aircraft Number")
    elif option == 3:
        print("Exiting the program")
        break
    else:
        print("Invalid Option")
    break
