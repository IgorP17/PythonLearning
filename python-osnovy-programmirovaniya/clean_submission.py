# Выведите эту последовательность в обратном порядке.


def revers():
    n = int(input())
    if n != 0:
        revers()
        print(n)
    else:
        print(n)


revers()
