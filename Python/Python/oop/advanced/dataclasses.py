# dataclasses: auto-generate __init__, __repr__, __eq__ for simple classes

from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
print(p1)           # Point(x=1.0, y=2.0)
print(p1 == p2)     # True (auto-generated __eq__)

@dataclass
class Student:
    name: str
    grade: float = 0.0
    courses: list = field(default_factory=list)

s = Student("Alice", 95.0)
s.courses.append("Math")
print(s)
