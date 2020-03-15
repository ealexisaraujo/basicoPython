# -*- coding: utf-8 -*-
def sumrec(number):
    if number == 1:
        return 1

    return number + sumrec(number-1)


def run():
    number = int(input('Ingresa el número a sumar: '))

    res = sumrec(number)

    print('El resultado de la suma recursiva, tomando como base el {} es :{}'.format(
        number, res))


if __name__ == '__main__':
    run()
