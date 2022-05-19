a = [3, 6, 7, 5, 8, 2, 6, 1, 11, 12]
b = []
# for x in a:
#     if x % 2 == 0:
#         b.append(x)
# print(b)

# def is_even(i):
#     return i % 2 == 0

# for x in a:
#     if is_even(x):
#         b.append(x)
# print(b)

# c = list(filter(is_even, a))
# print(c)
#
# def big10(i):
#     return i > 10
#
# c1 = list(filter(big10, a))
# print(c1)
#
# c2 = []
# for x in a:
#     if is_even(x) and big10(x):
#         c2.append(x)
# print(c2)

# c3 = list(filter(is_even, filter(big10, a)))
# print(c3)

a = [3, 6, 7, 5, 8, 2, 6, 1, 11, 12]

# def is_even(i):
#     return i % 2 == 0
# c = list(filter(is_even, a))
# print(c)

c1 = list(filter(lambda x: x % 2 == 0, a))
print(c1)
c2 = list(filter(lambda x: x > 10, a))
print(c2)

c3 = list(filter(lambda x: x > 10, filter(lambda x: x % 2 == 0, a)))
print(c3)


c4 = list(filter(lambda x: x > 10 and x % 2 == 0, a))
print(c4)


