def print_max(a,b):
    if a > b:
        print(a, 'максимальное значение')
    elif a == b:
        print('==')
    else:
        print(b, 'максимальное')

print_max(1, 6)
print_max(1, 1)
x = 1
y = 2
print(print_max(x, y))
