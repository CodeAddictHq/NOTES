# reduce: combine all items in an iterable into a single value
# Requires import from functools

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers)
print(total)   # 15

# Find maximum value
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)   # 5

# With initial value
product = reduce(lambda acc, x: acc * x, numbers, 1)
print(product)   # 120
