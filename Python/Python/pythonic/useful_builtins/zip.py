# zip(): combine multiple iterables element-by-element

names = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
grades = ["A", "B", "A"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")

# zip stops at the shortest iterable
a = [1, 2, 3]
b = [10, 20]
print(list(zip(a, b)))   # [(1, 10), (2, 20)]

# Unzip with *
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums)      # (1, 2, 3)
print(letters)   # ('a', 'b', 'c')
