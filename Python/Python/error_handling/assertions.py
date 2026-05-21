# assert: check that a condition is True; raise AssertionError if not
# Use for debugging and testing assumptions in code

def divide(a, b):
    assert b != 0, "Denominator must not be zero"
    return a / b

print(divide(10, 2))   # 5.0

try:
    print(divide(10, 0))
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Assert a type
def greet(name):
    assert isinstance(name, str), "name must be a string"
    print(f"Hello, {name}!")

greet("Alice")
