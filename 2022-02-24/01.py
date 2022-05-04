import math


x = float(input('x = '))
s = 0
n = 10
for k in range(1, n + 1):
    s += x ** k / math.factorial(k)
print(s)
