def average_califaciones(calificaciones):
    total_calificaciones = 0
    for key, value in calificaciones.items():
        total_calificaciones = total_calificaciones + value
    numero_materias = len(calificaciones)
    prom = total_calificaciones / numero_materias
    return prom


if __name__ == "__main__":
    calificaciones = {}
    calificaciones['algoritmos'] = 9
    calificaciones['matematicas'] = 10
    calificaciones['programacion web'] = 10
    calificaciones['bases de datos'] = 9
    print('Tu promedio es de:')
    print(average_califaciones(calificaciones))
