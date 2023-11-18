

class Flight:
    def __innit__(self, flight_number, flight_origin, aircraft_number, airline_name,airline_code, current_distance=0, current_speeed=0, scheduled _arrival_time=None):
    self.flight_number = flight_number
    self.flight_origin = flight_origin
    self.aircraft_number = airline_name
    self.airline_code = airline_code
    self.current_distance = current_distance
    self.current_speed = current_speed
    self.scheduled_arrival_time = scheduled_arrival_time

def flight_status_update(self, distance, speed):
    self.current_distance = distance
    self.current_speed = speed

def flight_time_arrival(self):
    if self.current_speed > 0:
        time_arrival = self.current_distance / self.current_speed
        return time_arrival
    else:
        return "N/A"

























def AirportMenu():
    print("Airport Flight Arrival Menu")
    print("[1] Check Flight Arrival Status")
    print("[2] ")
    print("[3] ")

def SubMenu():
    print("Submenu")
    print("[1] Flights 1-3")
    print("[2] Flights 3-5")

while True:
    AirportMenu()
    option = int(input("Enter your choice (1/2/3:) "))

    if option == 1:
        print("Your Flight number is 5.")
        while True:
            SubMenu()
                sub_choice = input("Enter your Choice:")
            if sub_choice == 1:
                print("'You have selected option 1.")
    elif option == 2:
        print("Aircraft Number")
    elif option == 3:
        print("Exiting the program")
        break
    else:
        print("Invalid Option")
    break

