from datetime import datetime, timedelta
from qwe import Flight


flight1 = Flight("F1", "London","EasyJet","Airline23","TX",100, 500, "13:00")


flight1.flight_status_update(155550, 600, "14:00")




print(f"FLight to {flight1.flight_origin}")

text = ("Planess")


with open(testplane.txt','w'') as file:
    file.write(text)






def AirportMenu():
    print("Airport Flight Arrival Menu")
    print("[1] Check Flight Arrival Status")
    print("[2] ")
    print("[3] Exit ")

def SubMenu():
    print("Submenu")
    print("[1] Flights 1-3")
    print("[2] Flights 3-5")

while True:
    AirportMenu()
    option = int(input("Enter your choice (1/2/3:) "))

    if option == 1:
        while True:
            SubMenu()
            sub_choice = input("Enter your Choice:")
            
            if sub_choice == '1':
                print("'You have selected option 1.")
            elif sub_choice == '2':
                print("shussh")
            elif sub_choice == '3':
                print("invalid choice")
            elif sub_choice == '4':
                print("valid")
            break
        else:
            print("invlaid choice")
    elif option == 2:
        print("Aircraft Number")
    elif option == 3:
        print("Exiting the program")
        break
    else:
        print("Invalid Option")
    break
