# Ternary expression: a compact one-line if/else

age = 20

# Long form
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary (conditional expression)
status = "adult" if age >= 18 else "minor"
print(status)   # adult

# Useful in print statements or assignments
x = 10
print("positive" if x > 0 else "non-positive")
