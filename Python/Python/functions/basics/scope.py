# Scope: where a variable is accessible

x = "global"   # global scope

def show():
    y = "local"    # local scope — only inside this function
    print(x)       # can access global
    print(y)

show()
# print(y)   # NameError — y is not accessible here

# Modify global variable inside a function
count = 0

def increment():
    global count
    count += 1

increment()
print(count)   # 1
