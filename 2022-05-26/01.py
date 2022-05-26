# reduce
from functools import reduce

def mult(x, y):
    return x * y

a = range(1,6)
fact = reduce(mult, a)
print(fact)

# 1 2 3 4 5 -> 2 3 4 5 -> 6 4 5 -> 24 5 -> 120

def mn(x, y):
    if x > y:
        return x
    return y

a = [56, 89, 100, 0, -3, 10, -2]
print(reduce(mn, a))

print(reduce(lambda x, y: x if x > y else y, a))

