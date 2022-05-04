d = {'bnf':67, 'asd': 78, 'zx':7, 'cf':9}
a = list(d.keys())
a.sort()
print(a)
for x in a:
    print(x, d[x])

d = {'bnf':67, 'asd': 78, 'zx':7, 'cf':9}
for x in sorted(list(d.keys())):
    print(x, d[x])