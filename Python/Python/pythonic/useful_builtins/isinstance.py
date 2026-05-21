# isinstance(): check if an object is an instance of a class or type

print(isinstance(42, int))        # True
print(isinstance(3.14, float))    # True
print(isinstance("hi", str))      # True
print(isinstance([], list))       # True

# Check against multiple types
print(isinstance(42, (int, float)))   # True

# Useful in functions to validate input
def double(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Expected a number.")
    return value * 2

print(double(5))     # 10
print(double(2.5))   # 5.0
