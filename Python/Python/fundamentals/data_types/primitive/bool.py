# bool: True or False — a subtype of int in Python

is_active = True
is_done = False

print(is_active)
print(type(is_active))  # <class 'bool'>

# Booleans are integers under the hood
print(True + True)   # 2
print(False + 1)     # 1

# Truthy and falsy values
print(bool(0))       # False
print(bool(""))      # False
print(bool(42))      # True
print(bool("hi"))    # True
