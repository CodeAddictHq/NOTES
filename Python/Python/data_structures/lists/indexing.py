# Indexing: access individual list elements by position

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])    # apple (first)
print(fruits[2])    # cherry
print(fruits[-1])   # elderberry (last)
print(fruits[-2])   # date (second to last)

# Modify by index
fruits[1] = "blueberry"
print(fruits)

# IndexError if out of range
# print(fruits[10])
