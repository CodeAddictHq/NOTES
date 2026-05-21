# pass: a no-op placeholder that does nothing
# Used when a statement is required syntactically but no action is needed

for i in range(5):
    pass               # loop runs but does nothing

# Useful as a placeholder while writing code
class MyClass:
    pass               # empty class — fill in later

def my_function():
    pass               # empty function — fill in later

if True:
    pass               # empty block
else:
    print("else runs")
