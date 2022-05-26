# zip
a1 = [1, 2, 3, 4]
a2 = [5, 6, 7]
a3 = [8, 9, 10, 11, 12]
a = list(zip(a1, a2))
print(a)

b = list(map(lambda x: x[0] * x[1], zip(a1, a2)))
print(b)

bb = list(zip(a1, a2, a3))
print(bb)
b = list(map(lambda x: x[0] * x[1] + x[2], zip(a1, a2, a3)))
print(b)