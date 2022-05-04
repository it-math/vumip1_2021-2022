try:
    x = int(input('x = '))
    z = input('z = ')
    y = 1 / (x - 2)
    print(y)
    f = open('1.txt')
    b = a + y
    a = x // z
except ZeroDivisionError:
    print('деление на 0')
    # print('положим y = 0')
    #y = 0
except ValueError:
    print('str в int')
except TypeError:
    print('operation')
except NameError:
    print('a?')
except:
    print('какая-то ошибка')
else:
    y = 0