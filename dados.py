import random


class dado():

    FORMAS = ['''
    
        ||<><><>||
        ||      ||
        ||   0  ||
        ||      ||
        ||<><><>|| ''', '''

        ||<><><>||
        ||   0  ||
        ||      ||
        ||   0  ||
        ||<><><>|| ''', '''

        ||<><><>||
        || 0  0 ||
        ||   0  ||
        ||      ||
        ||<><><>|| ''', '''

        ||<><><>||
        || 0  0 ||
        ||      ||
        || 0  0 ||
        ||<><><>|| ''', '''

        ||<><><>||
        || 0  0 ||
        ||   0  ||
        || 0  0 ||
        ||<><><>|| ''', '''

        ||<><><>||
        || 0  0 ||
        || 0  0 ||
        || 0  0 ||
        ||<><><>|| '''
              ]

    def__init__(self, numero_aleatorio):
        self.inicio_aleatorio = numero_aleatorio
        print(self.FORMAS[self.inicio_aleatorio])

    def tirar(self):
        numero_aleatorio = random.randint(0, 5)
        print(self.FORMAS[numero_aleatorio])

    def seleccionar(self, numero_elegido):
        print(self.FORMAS[numero_elegido-1])


def run():

    dado_d = dado(numero_aleatorio)

    while True:
        desicion = str(input('''
        ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---
        ¿Que deseas hacer?, tirar el dado o ¿seleccionar un numero?
            [T]irar el dado, al azar
            [S]eleccionar el numero.
            [N]ada, salir
        
        ---*---*---*---*---*---*---*---*---*---*---*---*---*---*---
            '''))

        if desicion.upper() == 'T':
            dado_d.tirar()
        elif desicion.upper() == 'S':
            numero_elegido = int(
                input('Ingrese el numero de cara a elegir del 1 al 6: '))
            dado_d.seleccionar(numero_elegido)
        else:
            print('Gracias, por jugar')
            break


if __name__ == '__main__':
    numero_aleatorio = random.randint(0, 5)
    run()
