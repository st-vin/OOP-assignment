# Base class
class Vehicle:
    def move(self):
        # method (to be overridden)
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water!")

# Create objects
vehicle_1 = Car()
vehicle_1.move()

vehicle_2 = Plane()
vehicle_2.move()

vehicle_3 = Boat()
vehicle_3.move()

