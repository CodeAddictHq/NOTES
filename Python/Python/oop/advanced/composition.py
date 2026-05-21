# Composition: building complex objects by combining simpler ones
# Prefer composition over inheritance when the relationship is "has-a"

class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()   # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print(f"{self.model} is driving.")

    def park(self):
        self.engine.stop()
        print(f"{self.model} is parked.")

car = Car("Toyota")
car.drive()
car.park()
