a = 1
b = 2
h = 0.25
x = a

for i in range(int((b-a) / h) + 1):
    y = 3 * x * x
    print(x, y)
    x += h


