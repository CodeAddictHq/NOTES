# Identity operators: check if two variables point to the same object

a = [1, 2, 3]
b = a           # b references the same list
c = [1, 2, 3]  # c is a new list with same values

print(a is b)    # True — same object in memory
print(a is c)    # False — different objects
print(a == c)    # True — same values

# None comparison should always use 'is'
x = None
print(x is None)     # True (correct)
print(x == None)     # True (works but not recommended)
