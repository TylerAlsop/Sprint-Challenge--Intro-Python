# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels
    
    def drive(self):
        return "vroooom"

four_wheeler = GroundVehicle()
print(four_wheeler.num_wheels)
print(four_wheeler.drive())

    # TODO

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels, brand):
        super().__init__(num_wheels = 2) 
        self.brand = brand
    
    def drive(self):
        return "BRAAAP!!"


honda = Motorcycle( None, "honda")

print(honda.num_wheels)
print(honda.drive())


# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(None, "Honda"),
    GroundVehicle(),
    Motorcycle(None, "Harley Davidson"),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for item in vehicles:
    print(item.drive())
