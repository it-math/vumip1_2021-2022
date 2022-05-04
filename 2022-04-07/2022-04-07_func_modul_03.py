def func(x):
    global s
    s += x
    return s

s = 10
print(func(2))
print(s)
print(func(3))
print(s)
print(func(3))
print(s)