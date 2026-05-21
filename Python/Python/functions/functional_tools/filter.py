# filter: keep only items where the function returns True

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8]

# Filter out empty strings
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, words))   # None keeps truthy values
print(non_empty)   # ['hello', 'world', 'python']

def is_adult(age):
    return age >= 18

ages = [15, 22, 17, 30, 12]
adults = list(filter(is_adult, ages))
print(adults)   # [22, 30]
