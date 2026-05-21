# Inheritance: a child class inherits attributes and methods from a parent

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):            # override parent method
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()   # Rex says Woof!
cat.speak()   # Whiskers says Meow!
print(isinstance(dog, Animal))   # True
