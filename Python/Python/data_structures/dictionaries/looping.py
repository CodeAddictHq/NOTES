# Different ways to loop over a dictionary

person = {"name": "Alice", "age": 30, "city": "Paris"}

# Loop over keys (default)
for key in person:
    print(key)

# Loop over values
for value in person.values():
    print(value)

# Loop over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Build new dict while looping
upper_keys = {k.upper(): v for k, v in person.items()}
print(upper_keys)
