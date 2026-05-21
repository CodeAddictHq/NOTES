# Iterators: objects that return elements one at a time
# Must implement __iter__() and __next__()

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = Counter(4)
for num in counter:
    print(num)   # 0 1 2 3

# Built-in iter() and next()
items = iter([10, 20, 30])
print(next(items))   # 10
print(next(items))   # 20
