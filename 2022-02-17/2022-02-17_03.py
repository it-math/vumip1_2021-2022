a = 1
b = 2
h = 0.3

for i in range(int((b-a) / h) + 1):
    x = a + i * h
    y = 3 * x * x
    print(x, y)
