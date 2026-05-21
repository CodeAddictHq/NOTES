# map: apply a function to every item in an iterable

numbers = [1, 2, 3, 4, 5]

# Square each number
squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25]

# Convert strings to ints
strings = ["1", "2", "3"]
ints = list(map(int, strings))
print(ints)   # [1, 2, 3]

# Map with a named function
def double(x):
    return x * 2

print(list(map(double, numbers)))   # [2, 4, 6, 8, 10]
