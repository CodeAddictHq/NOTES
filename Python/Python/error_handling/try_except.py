# try/except: catch and handle errors gracefully

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch multiple exception types
try:
    num = int("abc")
except ValueError:
    print("Invalid number format.")
except TypeError:
    print("Wrong type.")

# Catch any exception
try:
    items = [1, 2, 3]
    print(items[10])
except Exception as e:
    print(f"Error: {e}")
