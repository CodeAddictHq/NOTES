# set: unordered collection of unique items

nums = {1, 2, 3, 3, 2}
print(nums)            # {1, 2, 3} — duplicates removed

nums.add(4)
nums.discard(1)
print(nums)

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)           # union → {1, 2, 3, 4}
print(a & b)           # intersection → {2, 3}
print(a - b)           # difference → {1}
