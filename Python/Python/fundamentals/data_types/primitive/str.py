# str: a sequence of characters enclosed in quotes

greeting = "Hello, World!"
name = 'Alice'
multiline = """Line one
Line two"""

print(greeting)
print(len(greeting))          # 13

# Common string operations
print(greeting.upper())
print(greeting.lower())
print(greeting.replace("World", "Python"))

# f-string formatting
age = 30
print(f"{name} is {age} years old.")

# Indexing
print(greeting[0])   # H
print(greeting[-1])  # !
