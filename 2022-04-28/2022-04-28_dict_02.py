d = {}
s = 'bhjgcvhjdsvfb jfdhjjdkdx fh\djc hfjkd fhfjdnx'
print(s)
for x in s:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)

d = {}
s = 'bhjgcvhjdsvfb jfdhjjdkdx fh\djc hfjkd fhfjdnx'
for x in s:
    d[x] = d.get(x,0) + 1
print(d)

if 'b' in d:
    del d['b']
print(d)

try:
    del d['a']
except KeyError:
    print('error')

k = d.pop('h')
print(d)
print(k)
k = d.pop('a', None)
print(k)

print(list(d.keys()))
print(list(d.items()))
print(list(d.values()))

k = d.popitem()
print(k[0],k[1])

d.setdefault('a')
d.setdefault('b', 1000)
d.setdefault('b', 50)
print(d)