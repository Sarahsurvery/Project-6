#assign 3
#Public Variable and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand            # Public variable

    def start(self):                 # Public method
        print(f"{self.brand} car is starting...")

my_car = Car("Toyota")                # Create object
print(my_car.brand)                  # Access public variable
my_car.start()                       # Call public method
# Explanation:
#	Variables and methods are public by default in Python.
