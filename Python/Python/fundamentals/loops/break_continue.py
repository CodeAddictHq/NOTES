# break: exit the loop early
# continue: skip to the next iteration

# break example
for i in range(10):
    if i == 5:
        break          # stop when i reaches 5
    print(i)           # prints 0 1 2 3 4

print("---")

# continue example
for i in range(10):
    if i % 2 == 0:
        continue       # skip even numbers
    print(i)           # prints 1 3 5 7 9
