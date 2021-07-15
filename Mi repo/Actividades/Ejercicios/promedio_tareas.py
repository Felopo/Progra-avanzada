# Escribe aqui tus notas/posibles notas con dos decimales
T0 = 5.4
T1 = 2.63
T2 = 3.66
T3 = 1

# Calculo de la nota
notas = [T0, T1, T2, T3]
pesos = [1, 2, 4, 5]

if __name__ == '__main__':
    # Promedios posibles
    opciones = list()

    # Suma con pesos de las notas de tareas
    total = 0
    for nota, peso in zip(notas, pesos):
        total += nota * peso

    # Promedio sin eliminar ninguna tarea
    opciones.append(round(total / 12, 2))

    # Calculo de promedios eliminando cada nota
    for i in range(4):
        nueva_nota = round((total - notas[i] * pesos[i]) / (12 - pesos[i]), 2)
        opciones.append(nueva_nota)

    # Calculo antes de la actualización
    print(f"Tu promedio antiguo hubiera sido: {round(total / 12, 2)}")
    # Calculo con la actualización (mejor nota posible eliminando una tarea)
    print(f"Tu nuevo promedio de tareas es: {round(max(opciones), 2)}")