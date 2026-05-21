# Attributes: data stored on a class or instance

class Circle:
    pi = 3.14159   # class attribute — shared by all

    def __init__(self, radius):
        self.radius = radius   # instance attribute — unique per object

    def area(self):
        return Circle.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)   # 5
print(c2.radius)   # 10
print(Circle.pi)   # 3.14159
print(c1.area())   # 78.53975
