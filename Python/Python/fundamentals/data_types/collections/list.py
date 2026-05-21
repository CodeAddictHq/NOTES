# list: ordered, mutable collection of items

fruits = ["apple", "banana", "cherry"]

print(fruits[0])       # apple
print(fruits[-1])      # cherry
print(len(fruits))     # 3

fruits.append("date")
fruits.remove("banana")
print(fruits)

# Lists can hold mixed types
mixed = [1, "hello", True, 3.14]
print(mixed)
