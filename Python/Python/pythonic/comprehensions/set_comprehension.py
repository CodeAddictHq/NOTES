# Set comprehension: build sets concisely
# {expression for item in iterable if condition}

nums = [1, 2, 2, 3, 3, 3, 4]

unique_squares = {x ** 2 for x in nums}
print(unique_squares)   # {1, 4, 9, 16} — no duplicates

words = ["Hello", "world", "hello", "Python"]
lower_unique = {w.lower() for w in words}
print(lower_unique)     # {'hello', 'world', 'python'}
