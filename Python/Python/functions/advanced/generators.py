# Generators: functions that yield values one at a time, saving memory

def count_up(limit):
    n = 0
    while n < limit:
        yield n       # pause and return value, resume on next call
        n += 1

gen = count_up(5)
print(next(gen))   # 0
print(next(gen))   # 1

# Use in a for loop
for value in count_up(5):
    print(value)

# Generator expression (like list comprehension but lazy)
squares = (x ** 2 for x in range(5))
print(list(squares))   # [0, 1, 4, 9, 16]
