# type(): return the type of an object, or create new types dynamically

print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>
print(type(None))        # <class 'NoneType'>

# Use type() for exact type checking (isinstance is usually preferred)
x = True
print(type(x) is bool)     # True
print(type(x) is int)      # False — even though bool is a subclass of int

# Inspect class name as a string
print(type(42).__name__)   # int
