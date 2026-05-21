# List comprehension: concise way to create lists
# Syntax: [expression for item in iterable if condition]

squares = [x ** 2 for x in range(6)]
print(squares)   # [0, 1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8]

words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)     # ['HELLO', 'WORLD', 'PYTHON']

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in matrix:
    print(row)
