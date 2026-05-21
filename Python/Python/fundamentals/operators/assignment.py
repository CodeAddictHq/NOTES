# Assignment operators: assign and update variable values

x = 10       # basic assignment
x += 5       # x = x + 5  → 15
x -= 3       # x = x - 3  → 12
x *= 2       # x = x * 2  → 24
x //= 5      # x = x // 5 → 4
x **= 3      # x = x ** 3 → 64
x %= 10      # x = x % 10 → 4

print(x)     # 4

# Walrus operator (Python 3.8+): assign inside expressions
numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:
    print(f"List has {n} items")
