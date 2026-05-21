# with statement: automatically manage setup and teardown (e.g. file closing)

# File handling — file is closed automatically even if an error occurs
with open("/tmp/example.txt", "w") as f:
    f.write("Hello, World!\n")

with open("/tmp/example.txt", "r") as f:
    content = f.read()
    print(content)

# Multiple context managers in one line
with open("/tmp/a.txt", "w") as a, open("/tmp/b.txt", "w") as b:
    a.write("File A")
    b.write("File B")
