# tuple: ordered, immutable collection of items

point = (3, 7)
colors = ("red", "green", "blue")

print(point[0])        # 3
print(len(colors))     # 3

# Tuples are immutable — this would raise an error:
# point[0] = 99

# Packing and unpacking
x, y = point
print(x, y)

# Single-element tuple needs a trailing comma
single = (42,)
print(type(single))    # <class 'tuple'>
