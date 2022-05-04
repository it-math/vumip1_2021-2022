n = int(input('n = '))
a1 = 2
a2 = 4

for i in range(3, n + 1):
    an = a1 + 2 * a2
    print(i, an)
    a1 = a2
    a2 = an

