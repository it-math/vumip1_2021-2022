#set
s = {1}
print(type(s))

s1 = {5, 0, 'hello', 'g', 7}
print(s1)
ss = {} # это не множество
print(type(ss))

ss = set()
a1 = list(s1)
print(a1)

s1 = {5, 0, 1000000000000000, -100000000000000000000000000, 7}
print(s1)
for x in s1:
    print(x)

import sys
s = set()
print(s.__sizeof__())
print(sys.getsizeof(s))

ss = {1,2,3, 'hello'}
print(ss.__sizeof__())
print(sys.getsizeof(ss))

s = {1, 2, 3}
s.add(5)
print(s)

s.update({3, 5, 6, 7})
print(s)

s.update({13, 15}, {34, 67})
print(s)

s.update('hello')
print(s)

s.update({'hello'})
print(s)

s.discard(34)
print(s)

s.discard(14)
print(s)

s.remove(67)
print(s)

s.remove(67)
print(s)

if 67 in s:
    s.remove(67)
else:
    s.add(56)

s.pop()