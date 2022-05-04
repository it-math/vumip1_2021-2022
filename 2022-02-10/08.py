x = int(input())
s = 0
while x != 0:
    if x < 0:
        break
    s += x
    x = int(input())
else:
    print('нет отр чисел')
print(s)