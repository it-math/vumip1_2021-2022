def func1(a, n):
    '''
    Функция изменяет список
    :param a: исходный список
    :param n: кол-во добавляемых элементов
    :return: измененный список
    '''

    for i in range(n):
        #a.append(i)
        a += [i]
    return a

def func2(a,n):
    '''
    Функция не изменяет список
    :param a: исходный список
    :param n: кол-во добавляемых элементов
    :return: измененный список
    '''

    for i in range(n):
        a = a + [i]
    return a

print(func1([1,2,3], 3))
print(func1.__doc__)

print(sum.__doc__)
print(len.__doc__)