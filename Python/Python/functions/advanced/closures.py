# Closures: inner functions that remember variables from their enclosing scope

def make_multiplier(factor):
    def multiply(number):
        return number * factor   # 'factor' is captured from outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# Closure stores its own copy of the enclosed variable
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
