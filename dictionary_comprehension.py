# -*- coding: utf-8 -*-


def listComprehension():
    pares = []

    for num in range(1, 31):
        if num % 2 == 0:
            pares.append(num)
            print(pares)


def comprehension():
    even = [num for num in range(1, 31) if num % 2 == 0]
    print(even)


def cuaddrados():
    cuadrados = {}
    for num in range(1, 11):
        cuadrados[num] = num**2


def squares():
    square = {num: num**2 for num in range(1, 11)}
    print(square)


if __name__ == '__main__':
    # print(listComprehension())
    # print(comprehension())
    # print(cuaddrados())
    print(squares())
