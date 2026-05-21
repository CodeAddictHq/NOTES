# dict: key-value pairs — like a real-world dictionary

person = {"name": "Alice", "age": 30, "city": "Paris"}

print(person["name"])          # Alice
print(person.get("age"))       # 30
print(person.get("email", "N/A"))  # N/A — default if missing

person["email"] = "alice@example.com"
del person["city"]
print(person)

# Iterate over a dict
for key, value in person.items():
    print(f"{key}: {value}")
