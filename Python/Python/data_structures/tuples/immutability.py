# Immutability: tuples cannot be changed after creation

point = (3, 7)

# This would raise a TypeError:
# point[0] = 99

# But if a tuple contains a mutable object, that object can change
data = ([1, 2], [3, 4])
data[0].append(99)      # OK — the list inside can change
print(data)             # ([1, 2, 99], [3, 4])

# Tuples are hashable (can be dict keys) when they contain only immutable items
locations = {(40.7, -74.0): "New York", (51.5, -0.1): "London"}
print(locations[(40.7, -74.0)])
