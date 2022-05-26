import time
a = range(1, 10000)

t1 = time.time()
a1 = [str(x) for x in a if x % 2 == 0]
print(time.time() - t1)
print(a1)
t1 = time.time()
a2 = list(map(str, filter(lambda x: x % 2 == 0, a)))
print(time.time() - t1)
print(a2)