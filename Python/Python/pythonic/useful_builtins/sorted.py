# sorted(): return a new sorted list from any iterable

nums = [3, 1, 4, 1, 5, 9, 2]

print(sorted(nums))           # ascending: [1, 1, 2, 3, 4, 5, 9]
print(sorted(nums, reverse=True))  # descending

# Sort by a key function
words = ["banana", "apple", "cherry", "date"]
print(sorted(words))                          # alphabetical
print(sorted(words, key=len))                 # by length
print(sorted(words, key=lambda w: w[-1]))     # by last character

# Sort list of dicts
people = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
print(sorted(people, key=lambda p: p["age"]))
