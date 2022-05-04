import math


x = float(input('x = '))
s = 0
n1, n2 = 10, 5
print('k m')
for k in range(1, n1 + 1):
    for m in range(n2 + 1):
        print(k, m)
        s += x ** (k + m) / (2 * (k + m) + math.sin(m * x))
print(s)