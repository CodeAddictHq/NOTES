# Parameters: values passed into a function

# Positional parameters
def add(a, b):
    print(a + b)

add(3, 5)   # 8

# Default parameter values
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!

# Keyword arguments
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe(age=25, city="Paris", name="Alice")
