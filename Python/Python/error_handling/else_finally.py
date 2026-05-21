# else: runs if no exception occurred
# finally: always runs, regardless of exception

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print(f"Result: {result}")   # only if no exception
    finally:
        print("Division attempted.") # always runs

divide(10, 2)
print("---")
divide(10, 0)
