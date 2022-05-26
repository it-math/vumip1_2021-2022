n = [range(5), range(8, 11)]
print(n)

a = [x for i in n for x in i]
print(a)

a1 = [i + 1 for i in range(5)]
print(a1)
a2 = [(i + 1) * 10 for i in range(5)]
print(a2)
a12 = [i * j for i in a1 for j in a2 if i <= 2]
print(a12)

d1 = {x: x ** 2 for x in range(10)}
print(d1)
d2 = {x % 7 for x in [4, 9, 2, 5, 9, -10]}
print(d2)