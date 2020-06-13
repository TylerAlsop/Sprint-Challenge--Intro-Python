# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# BASE CLASS:
class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle

################################################
class GroundVehicle(Vehicle):
    def __init__(self, vehicle, ground_vehicle):
        super().__init__(vehicle)
        self.ground_vehicle = ground_vehicle


class Car(GroundVehicle):
    def __init__(self, vehicle, ground_vehicle, car):
        super().__init__(vehicle, ground_vehicle)
        self.car = car

class Motorcycle(GroundVehicle):
    def __init__(self, vehicle, ground_vehicle, motorcycle):
        super().__init__(vehicle, ground_vehicle)
        self.motorcycle = motorcycle



################################################
class FlightVehicle(Vehicle):
    def __init__(self, vehicle, flight_vehicle):
        super().__init__(vehicle)
        self.flight_vehicle = flight_vehicle
        

class Airplane(FlightVehicle):
    def __init__(self, vehicle, flight_vehicle, airplane):
        super().__init__(vehicle, flight_vehicle)
        self.airplane = airplane

class Starship(FlightVehicle):
    def __init__(self, flight_vehicle, starship):
        super().__init__(flight_vehicle)
        self.starship = starship

