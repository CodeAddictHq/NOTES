# float: numbers with a decimal point

pi = 3.14159
temp = -0.5
sci = 1.5e3       # scientific notation → 1500.0

print(pi)
print(type(pi))   # <class 'float'>

# Floating-point precision quirk
print(0.1 + 0.2)  # 0.30000000000000004 — normal in computing

# Round to avoid surprises
print(round(0.1 + 0.2, 2))  # 0.3
