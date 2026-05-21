# Custom context manager using a class with __enter__ and __exit__

class Timer:
    import time as _time

    def __enter__(self):
        self.start = self._time.time()
        print("Timer started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = self._time.time() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False   # don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))

# Using contextlib.contextmanager decorator
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    yield name
    print(f"Releasing {name}")

with managed_resource("database connection") as r:
    print(f"Using {r}")
