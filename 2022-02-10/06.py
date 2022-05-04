s = 0
for i in range(100):
    x = int(input())
    if x == 5:
        continue
    if x >= 0:
        s += x
    else:
        break
    print('s = ', s)
print(s)