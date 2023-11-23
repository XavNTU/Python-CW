class Flight:
    def __init__(self, flight_number, flight_origin, aircraft_number, airline_name,airline_code, current_distance=0, current_speed=0, scheduled_arrival_time=None):
        self.flight_number = flight_number
        self.flight_origin = flight_origin
        self.aircraft_number = airline_name
        self.airline_code = airline_code
        self.current_distance = current_distance
        self.current_speed = current_speed
        self.scheduled_arrival_time = scheduled_arrival_time

    def flight_status_update(self,distance, speed, new_time):
        self.distance = distance
        self.speed = speed
        self.new_time = new_time

