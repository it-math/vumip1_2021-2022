def f_out():
    x = 2
    y = 10
    print('1', x)

    def f_in():
        nonlocal y
        x = 20
        y = 11

    f_in()
    print(y)
    print('2', x)

x = 1000
f_out()
print(x)
#f_in()