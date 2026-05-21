# return: send a value back from a function

def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8

# Return multiple values (as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2])
print(low, high)   # 1 7

# No return → returns None
def say_hi():
    print("Hi!")

val = say_hi()
print(val)   # None
