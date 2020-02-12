import sys


def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a dolares.')
    print('')
    print('Python Version')
    print(sys.version)
    amount = float(
        input('Ingresa la cantidad que quieres convertir: '))
    resultado = calculadora_divisa(amount)
    print('${} pesos mexicanos, son ${} dolares'.format(amount, resultado))


def calculadora_divisa(cantidad):
    valor = 18.45
    return cantidad / valor


if __name__ == '__main__':
    run()
