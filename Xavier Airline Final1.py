from datetime import datetime, timedelta

class Flight:
    def __init__(self, flight_number, flight_origin, aircraft_number, airline_name, airline_code, current_distance=0, current_speed=0, scheduled_arrival_time=None):
        self.flight_number = flight_number
        self.flight_origin = flight_origin
        self.aircraft_number = aircraft_number
        self.airline_name = airline_name
        self.airline_code = airline_code
        self.current_distance = current_distance
        self.current_speed = current_speed
        self.scheduled_arrival_time = scheduled_arrival_time

 
    def calculate_estimated_arrival_time(self):
        if self.current_speed == 0:
            return "Cannot calculate estimated arrival time when the speed is 0."
        
        current_time = datetime.strptime(self.scheduled_arrival_time, "%H:%M")
        time_to_arrival = timedelta(hours=self.current_distance / self.current_speed)
        estimated_arrival_time = current_time + time_to_arrival
        return estimated_arrival_time.strftime("%H:%M")
    
def AirportMenu():
    print("Airport Flight Arrival Menu")
    print("[1] Check Flight Arrival Status")
    print("[2] Exit")


def SubMenu():
    print("Submenu")
    print("[1] Flights 1-2")
    print("[2] Flights 3-5")
    print("[3] All Scheduled Flights")
    print("[4] Estimated Arrival Times")
    print("[5] Display Airlines")


def FlightMenu(flight):
    print(f"Flight {flight.flight_number} to {flight.flight_origin} at {flight.scheduled_arrival_time}")
    print("Flight Status:")
    print(f"  - Distance: {flight.current_distance} km")
    print(f"  - Speed: {flight.current_speed} km/h")
    print(f"  - Scheduled Arrival Time: {flight.scheduled_arrival_time}")
    print(f"  - Estimated Arrival Time: {flight.calculate_estimated_arrival_time()}")
    

flight1 = Flight("F1", "London", "EasyJet", "Airline 1", "TX", 250, 200, "13:00")
flight2 = Flight("F2", "Germany", "United Airline ", "Airline 2", "TX", 350, 600, "14:00")
flight3 = Flight("F3", "Iran", "Fly Ones", "Airline 3", "TX", 225, 500, "15:30")
flight4 = Flight("F4", "Dubai", "Qantas Airways", "Airline 4", "TX", 100, 500, "18:00")
flight5 = Flight("F5", "France", "SAS", "Airline 5", "TX", 200, 300, "17:00")


while True:
    AirportMenu()
    option = int(input("Enter your choice (1/2): "))

    if option == 1:
        while True:
            SubMenu()
            sub_choice = input("Enter your Choice (1/2): ")

            if sub_choice == '1':
                FlightMenu(flight1)
                FlightMenu(flight2)
            elif sub_choice == '2':
                FlightMenu(flight3)
                FlightMenu(flight4)
                FlightMenu(flight5)
            elif sub_choice == '3':
                print(f"Flight {flight1.flight_number} to {flight1.flight_origin} at {flight1.scheduled_arrival_time}")
                print(f"Flight {flight2.flight_number} to {flight2.flight_origin} at {flight2.scheduled_arrival_time}")
                print(f"Flight {flight3.flight_number} to {flight3.flight_origin} at {flight3.scheduled_arrival_time}")
                print(f"Flight {flight4.flight_number} to {flight4.flight_origin} at {flight4.scheduled_arrival_time}")
                print(f"Flight {flight5.flight_number} to {flight5.flight_origin} at {flight5.scheduled_arrival_time}")
            elif sub_choice == '4':
                print(f"Flight {flight1.flight_number} to {flight1.flight_origin} at {flight1.calculate_estimated_arrival_time()}")
                print(f"Flight {flight2.flight_number} to {flight2.flight_origin} at {flight2.calculate_estimated_arrival_time()}")
                print(f"Flight {flight3.flight_number} to {flight3.flight_origin} at {flight3.calculate_estimated_arrival_time()}")
                print(f"Flight {flight4.flight_number} to {flight4.flight_origin} at {flight4.calculate_estimated_arrival_time()}")
                print(f"Flight {flight5.flight_number} to {flight5.flight_origin} at {flight5.calculate_estimated_arrival_time()}")
            elif sub_choice == '5':
               f = open("Fly.txt", "r")
               print(f.readline())
            else:
                print("Invalid choice")
            break
    elif option == 2:
        print("Exiting the program")
        break
    else:
        print("Invalid Option")


    
