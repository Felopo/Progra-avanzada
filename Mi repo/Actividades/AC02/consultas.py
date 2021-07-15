from collections import deque


def resumen_actual(ayudantes, alumnos):
    alumnos_restantes = len(alumnos)
    print("-"*20)
    print(f"Alumnos restantes: {alumnos_restantes}")
    ayudantes_rest = len(ayudantes["Piso -1"]) + len(ayudantes["Piso -2"]) \
                      + len(ayudantes["Piso -3"]) + len(ayudantes["Piso -4"])
    print("-"*20)
    print(f"Ayudantes restantes: {ayudantes_rest}")
    contador_pisos = -1
    for i in range(len(ayudantes)):
        largo_pisos = len(ayudantes["Piso " + str(contador_pisos)])
        print("Ayudantes Piso " + str(contador_pisos) + ": " + str(largo_pisos))
        contador_pisos -= 1
    print("-"*20)


def stock_comida(alumnos):
    pass



