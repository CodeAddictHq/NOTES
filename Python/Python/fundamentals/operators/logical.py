# Logical operators: combine boolean expressions

x = True
y = False

print(x and y)   # both must be True → False
print(x or y)    # at least one True → True
print(not x)     # inverts → False

# Short-circuit evaluation
a = 0
b = 10
print(a and b)   # 0 — stops at a (falsy)
print(a or b)    # 10 — returns first truthy value
