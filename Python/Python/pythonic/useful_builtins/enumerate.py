# enumerate(): loop with automatic index counter

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Start counting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Convert to list of tuples
indexed = list(enumerate(fruits))
print(indexed)   # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
