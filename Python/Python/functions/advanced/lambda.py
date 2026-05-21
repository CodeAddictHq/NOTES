# lambda: a small anonymous function written in one line
# Syntax: lambda arguments: expression

square = lambda x: x ** 2
print(square(5))   # 25

add = lambda a, b: a + b
print(add(3, 4))   # 7

# Commonly used with sorted, map, filter
names = ["Charlie", "Alice", "Bob"]
names.sort(key=lambda name: name.lower())
print(names)   # ['Alice', 'Bob', 'Charlie']
