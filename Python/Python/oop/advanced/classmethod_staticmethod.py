# @classmethod: receives the class (cls) as first argument
# @staticmethod: no implicit first argument — just a regular function in the class namespace

class MathHelper:
    pi = 3.14159

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.circle_area(5))   # 78.53975
print(MathHelper.add(3, 7))        # 10

# Also callable on instances
m = MathHelper()
print(m.circle_area(3))
print(m.add(1, 2))
