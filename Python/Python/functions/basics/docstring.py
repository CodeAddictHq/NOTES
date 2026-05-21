# Docstring: a string literal that documents a function

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def describe_person(name, age):
    """
    Print a description of a person.

    Args:
        name (str): The person's name.
        age (int): The person's age.
    """
    print(f"{name} is {age} years old.")

# Access docstrings
print(add.__doc__)
help(describe_person)
