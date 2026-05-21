# Unpacking with * and ** when calling functions

def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))   # unpacks list as positional args → 6

# ** unpacks a dict as keyword arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")

info = {"name": "Alice", "greeting": "Hello"}
greet(**info)

# Mix of both
def func(a, b, c, x, y):
    print(a, b, c, x, y)

func(*[1, 2, 3], **{"x": 4, "y": 5})
