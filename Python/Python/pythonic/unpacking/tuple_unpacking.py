# Tuple unpacking: assign multiple values from a sequence at once

point = (10, 20)
x, y = point
print(x, y)   # 10 20

# Swap variables
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1

# Extended unpacking with *
first, *middle, last = [1, 2, 3, 4, 5]
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# Nested unpacking
(a, b), c = (1, 2), 3
print(a, b, c)  # 1 2 3
