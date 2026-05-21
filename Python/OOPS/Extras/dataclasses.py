class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int