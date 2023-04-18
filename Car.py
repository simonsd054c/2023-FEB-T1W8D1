# Access modifiers - public, protected and private

# Car class - class is a blueprint4
class Car:
    # Constructor method
    def __init__(self, color, make):
        self._color = color
        self._make = make

    # getter method - accessors
    def get_color(self):
        return self._color
    
    # Setter method - mutators
    def set_color(self, color):
        self._color = color

    def run(self):
        print(f"{self._make} is running!!! Vroomm Vrrooomm!!!")

class PetrolCar(Car):
    def __init__(self, color, make, capacity):
        super().__init__(color, make)
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity
    
class ElectricCar(Car):
    # Override
    def run(self):
        print("I run silently")
    
    # Overloading - not supported by python
    # def run(self, sound):
    #     print(f"I run with this sound {sound}")


my_petrol_car = PetrolCar("white", "honda", 70)
print(my_petrol_car.get_capacity())
my_petrol_car.run()

ev_car = ElectricCar("black", "tesla")
ev_car.run()

# # my_car Object
# my_car = Car("white", "honda")
# print(my_car.get_color())
# my_car.set_color("blue")
# print(my_car.get_color())
# my_car.run()

# # Another object
# your_car = Car("black", "bmw")
# print(your_car.get_color())
# your_car.run()