def isprime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True


def run():
    number = int(input('Write a number: '))
    result = isprime(number)
    if result is True:
        print('Your number is prime')
    else:
        print('Your number is not prime')


if __name__ == '__main__':
    run()
