# None: represents the absence of a value (like null in other languages)

result = None

print(result)           # None
print(type(result))     # <class 'NoneType'>

# Check for None with 'is', not '=='
if result is None:
    print("No value assigned")

# Functions return None by default
def do_nothing():
    pass

print(do_nothing())     # None
