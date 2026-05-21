# Set operations: mathematical set theory in Python

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)            # union → {1, 2, 3, 4, 5, 6, 7}
print(a & b)            # intersection → {3, 4, 5}
print(a - b)            # difference (in a, not b) → {1, 2}
print(a ^ b)            # symmetric difference → {1, 2, 6, 7}

# Subset / superset checks
x = {1, 2}
print(x.issubset(a))    # True
print(a.issuperset(x))  # True
print(a.isdisjoint({8, 9}))  # True — no common elements
