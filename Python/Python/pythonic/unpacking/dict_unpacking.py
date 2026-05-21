# Dictionary unpacking with **

defaults = {"color": "blue", "size": "medium"}
overrides = {"size": "large", "weight": "light"}

# Merge dicts (Python 3.9+ can use | operator)
merged = {**defaults, **overrides}
print(merged)   # {'color': 'blue', 'size': 'large', 'weight': 'light'}

# Spread into a new dict with extra keys
config = {**defaults, "opacity": 0.9}
print(config)

# Python 3.9+ merge operator
# combined = defaults | overrides
