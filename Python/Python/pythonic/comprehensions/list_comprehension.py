# List comprehension: build lists concisely
# [expression for item in iterable if condition]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)   # [4, 16, 36, 64, 100]

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]
print(flat)           # [1, 2, 3, 4, 5, 6]

# Conditional expression inside comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)
