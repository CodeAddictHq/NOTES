# Packing: putting values into a tuple
# Unpacking: extracting values from a tuple

# Packing
coordinates = (40.7128, -74.0060)

# Unpacking
lat, lon = coordinates
print(lat)   # 40.7128
print(lon)   # -74.0060

# Swap values (uses tuple packing/unpacking under the hood)
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]
