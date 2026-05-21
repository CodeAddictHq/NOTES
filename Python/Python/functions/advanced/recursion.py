# Recursion: a function that calls itself to solve a smaller sub-problem

def factorial(n):
    if n == 0:        # base case — stops recursion
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))   # 120

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")   # 0 1 1 2 3 5 8 13
