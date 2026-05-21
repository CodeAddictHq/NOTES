#Polymorphism is  where the same interface or method name can behave differently depending on the object or context.

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

a1 = Dog()
a2 = Cat()

a1.sound()  # Bark
a2.sound()  # Meow


#method overriding 
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Bark")

class Cat(Animal):
    def sound(self):   # overriding
        print("Meow")

d = Dog()
c = Cat()

d.sound()  # Bark
c.sound()  # Meow