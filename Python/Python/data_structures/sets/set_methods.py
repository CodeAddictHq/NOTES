# Set methods: built-in operations to modify and query sets

s = {1, 2, 3, 4}

s.add(5)
s.discard(2)        # remove if present, no error if missing
s.remove(3)         # remove — raises KeyError if missing
print(s)            # {1, 4, 5}

s.update([6, 7])    # add multiple items
print(s)

copy = s.copy()
copy.clear()
print(copy)         # set()
print(len(s))
print(5 in s)       # True
