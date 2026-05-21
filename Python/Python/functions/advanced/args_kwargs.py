# *args: accept any number of positional arguments (as a tuple)
# **kwargs: accept any number of keyword arguments (as a dict)

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30, city="Paris")

# Combining: positional, *args, keyword, **kwargs
def demo(a, b, *args, key="default", **kwargs):
    print(a, b, args, key, kwargs)

demo(1, 2, 3, 4, key="custom", x=9)
