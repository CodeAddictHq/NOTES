# Dictionary methods

data = {"a": 1, "b": 2, "c": 3}

print(data.keys())     # dict_keys(['a', 'b', 'c'])
print(data.values())   # dict_values([1, 2, 3])
print(data.items())    # dict_items([('a', 1), ('b', 2), ('c', 3)])

# setdefault: set key only if it doesn't exist
data.setdefault("d", 99)
print(data["d"])       # 99

# Copy
copy = data.copy()
copy["a"] = 999
print(data["a"])       # 1 — original unchanged
