# Accessing and updating dictionary values

person = {"name": "Alice", "age": 30}

# Access
print(person["name"])              # Alice
print(person.get("email", "N/A")) # N/A — safe access with default

# Update
person["age"] = 31                 # update existing key
person["email"] = "alice@ex.com"  # add new key
person.update({"city": "Paris", "age": 32})

del person["email"]
popped = person.pop("city", None)  # remove and return

print(person)
