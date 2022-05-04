s = 0
for i in range(1000):
    x = int(input())
    if x >= 0:
        s += x
    else:
        break
print(s)