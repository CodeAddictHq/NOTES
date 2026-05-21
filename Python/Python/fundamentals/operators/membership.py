# Membership operators: check if a value exists in a sequence

fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Works with strings, sets, and dicts (checks keys)
sentence = "Hello, World!"
print("World" in sentence)    # True

data = {"name": "Alice", "age": 30}
print("name" in data)         # True
print("Alice" in data)        # False — checks keys, not values
