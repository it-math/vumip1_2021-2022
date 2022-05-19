# s = input()
# a = s.split()
# print(a)
# b = list(map(int, s.split()))
# print(b)
# c = list(map(str, b))
# print(c)
#
# def square(x):
#     return x ** 2

a = [3, 6, 7, 5, 8, 2, 6, 1, 11, 12]
# b = []
# for x in a:
#     b.append(square(x))
# print(b)
#
# c = list(map(square, a))
# print(c)

c1 = list(map(lambda x: x ** 2, a))
print(c1)

def is_even(i):
    return i % 2 == 0

c2 = list(map(str, filter(is_even, a)))
print(c2)
