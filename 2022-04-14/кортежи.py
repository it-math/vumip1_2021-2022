#tuple
t = (1, 6, (5, 8), 'hello', 'g', [0, 8, 9])
tt = 6, 'hello', 8, 2
t1 = ()
t2 = tuple()
t3 = (4)
print(type(t3))
t4 = (4, )
print(type(t4))
t5 = tuple('hello word')
print(t5)
#t5.append('a')
a = list(t5)
print(a)
print(type(a))
a.sort()
print(a)
tt5 = tuple(a)
print(tt5)
print(type(tt5))
print((1, 7, 9) + (0, 6, 5))
t = (1, 6, (5, 8), 'hello', 'g', [0, 8, 9])
t[5][0] = 'H'
print(t)

a = [1, 2, 3, 4, 5, 6]
t = (1, 2, 3, 4, 5, 6)
print(a.__sizeof__())
print(t.__sizeof__())
tt = ()
print(tt.__sizeof__())
aa = []
print(aa.__sizeof__())

import sys
tt = ()
print(tt.__sizeof__())
print(sys.getsizeof(tt))

aa = []
print(aa.__sizeof__())
print(sys.getsizeof(aa))

x = 12
print(x.__sizeof__())
print(sys.getsizeof(x))

xx = 12.5
print(xx.__sizeof__())
print(sys.getsizeof(xx))

s = ''
print(s.__sizeof__())
print(sys.getsizeof(s))

ss = 'hello 56757'
print(ss.__sizeof__())
print(sys.getsizeof(ss))

