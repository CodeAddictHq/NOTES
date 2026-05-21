# Indentation: Python uses whitespace to define code blocks
# Standard convention is 4 spaces per level

age = 20

if age >= 18:
    print("Adult")       # inside the if block
    print("Can vote")    # still inside
print("Outside block")   # outside the if block

# Nested indentation
for i in range(3):
    for j in range(3):
        print(i, j)      # two levels deep
