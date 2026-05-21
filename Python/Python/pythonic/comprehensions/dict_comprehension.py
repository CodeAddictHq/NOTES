# Dictionary comprehension: build dicts concisely
# {key: value for item in iterable if condition}

words = ["apple", "banana", "cherry"]

# Map word to its length
lengths = {word: len(word) for word in words}
print(lengths)   # {'apple': 5, 'banana': 6, 'cherry': 6}

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)

# Filter entries
prices = {"apple": 1.5, "banana": 0.5, "cherry": 2.5}
cheap = {k: v for k, v in prices.items() if v < 2}
print(cheap)
