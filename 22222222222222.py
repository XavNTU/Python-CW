def AirportMenu():
    print("Airport Flight Arrival Menu")
    print("[1] Flight Number")
    print("[2] Aircraft Number")
    print("[3] ddddddddddddd")
    print("[0] Exit the Program.")

AirportMenu()
option = int(input("Enter your option: "))

while True:
    if option == 1:
        print("Your Flight number is 5.")
    elif option == 2:
        print("Aircraft Number")
    elif option == 3:
        print("Your ddfdd")
    else:
        print("Invalid Option")
    break

