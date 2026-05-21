# raise: manually trigger an exception

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range.")
    return age

try:
    print(set_age(25))
    print(set_age(-5))
except ValueError as e:
    print(f"ValueError: {e}")

# Re-raise an exception
try:
    int("bad")
except ValueError:
    print("Caught it, re-raising...")
    raise
