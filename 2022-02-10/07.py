s = 0
for i in range(100):
    x = int(input())
    if x >= 0 and x != 5:
        s += x
    else:
        break
    print('s = ', s)
print(s)