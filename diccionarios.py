mi_diccionario = {}

mi_diccionario['primer_elemento'] = 'Hola'
mi_diccionario['segundo_elemento'] = 'Adios'

print(mi_diccionario['primer_elemento'])

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['programacion web'] = 10
calificaciones['bases de datos'] = 9

for key in calificaciones:
    print(key)
for value in calificaciones.values():
    print(value)
for key, value in calificaciones.items():
    print('llave: {}, valor: {}'.format(key, value))
