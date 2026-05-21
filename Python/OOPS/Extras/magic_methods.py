#magics methods let you define how objects behave with built-in operations 🔧
class Demo:
    def __init__(self, value):
        self.value = value

    def __str__(self):
      #what to done with print statemant
        return f"Demo object with value {self.value}"

    def __repr__(self):
        return f"Demo({self.value})"

    def __len__(self):
      #what to done with len statemant
        return len(str(self.value))

    def __add__(self, other):
      #what to done with + oparetor
        return Demo(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __call__(self):
        print("Object called like a function")

    def __getitem__(self, index):
        return str(self.value)[index]



a = Demo(123)
b = Demo(456)

print(a)          # __str__
print(repr(a))    # __repr__

print(len(a))     # __len__

c = a + b         # __add__
print(c.value)

print(a == b)     # __eq__

a()               # __call__

print(a[1])       # __getitem__