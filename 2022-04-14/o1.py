import sys
print(sys.path)

def f(x):
    return x ** 2

if __name__ == "__main__":
    x = int(input())
    print(f(2))

import paket.modul_a
a = paket.modul_a.func(3)

from paket import *
a = modul_a.func(3)