import time

n = 1000000
a = range(1, n)

t1 = time.time()
a1 = []
for x in a:
    a1.append(x ** 2)
print(time.time() - t1)

t1 = time.time()
a2 = list(map(lambda x: x ** 2, a))
print(time.time() - t1)

t1 = time.time()
a3 = [x ** 2 for x in a]
print(time.time() - t1)

