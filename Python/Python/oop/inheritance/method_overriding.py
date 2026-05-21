# Method overriding: child class redefines a method from the parent

class Vehicle:
    def start(self):
        print("Vehicle starting...")

    def describe(self):
        print("I am a vehicle.")

class ElectricCar(Vehicle):
    def start(self):                  # overrides Vehicle.start
        print("Electric car starting silently...")

    def describe(self):               # overrides Vehicle.describe
        super().describe()            # still calls parent version
        print("I run on electricity.")

car = ElectricCar()
car.start()
car.describe()
