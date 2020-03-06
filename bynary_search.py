# -*- coding: utf-8 -*-
import random


def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

    mid = int((low + high) / 2)

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for i in range(20)]
    numbers.sort()

    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número sí está en la lista.')
    else:
        print('El número NO está en la lista.')
