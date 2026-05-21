# super(): call a method from the parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"I am {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call Animal.__init__
        self.breed = breed

    def describe(self):
        super().describe()       # call Animal.describe
        print(f"Breed: {self.breed}")

dog = Dog("Rex", "Labrador")
dog.describe()
# I am Rex.
# Breed: Labrador
