def func1(a, n):
    for i in range(n):
        #a.append(i)
        a += [i]
    return a

def func2(a,n):
    for i in range(n):
        a = a + [i]
    return a

x = [1, 2, 3]
bb = func2(x, 5)
print(bb)
print(x)
b = func1(x, 5)
print(b)
print(x)