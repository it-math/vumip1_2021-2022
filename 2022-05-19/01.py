# def
# lambda-функции

# lambda arg: expression
# def lambda (arg):
#     return expession

# def func(x, y, z):
#     return x + y + z
# print(func(1, 2, 3))
#
# f = lambda x, y, z: x + y + z
# print(f(1, 2, 3))

def getfunc(a):
    if a > 0:
        return lambda x: x ** 2
    if a < 0:
        return lambda x: x * 3
    return lambda x: x + 1

f = getfunc(5)
print(f)
print(f(10))
g = getfunc(-5)
print(g)
print(g(10))
h = getfunc(0)
print(h)
print(h(10))