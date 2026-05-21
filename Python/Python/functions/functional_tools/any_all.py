# any(): True if at least one item is truthy
# all(): True if every item is truthy

numbers = [1, 2, 3, 4, 5]

print(any(x > 4 for x in numbers))    # True (5 > 4)
print(all(x > 0 for x in numbers))    # True (all positive)
print(all(x > 3 for x in numbers))    # False (1, 2, 3 are not > 3)

# With boolean lists
flags = [True, True, False]
print(any(flags))   # True
print(all(flags))   # False

# Empty iterables
print(any([]))   # False
print(all([]))   # True (vacuously true)
