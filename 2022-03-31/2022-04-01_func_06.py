def func():
    global x
    x = 10000
    return x


x = 2
y = func()
print(x)
print(y)