# Escribe aqui tus notas/posibles notas
ACS1 = 3  # Actividad sumativa 1 (AC02)
ACS2 = 3.1  # Actividad sumativa 2 (AC05)
ACS4 = 7  # Actividad sumativa 4 (AC10)
AR = 6.9  # Actividad recuperativa
DEC_ACF = 14  # Décimas actividades formativas

if __name__ == '__main__':
    # Promedio actividades
    XACS = round((ACS1 + ACS2 + ACS4) / 3, 2)

    # Nota de la actividad sumativa reemplazada (ACS3)
    ACS3 = max(XACS, AR)

    # Hacemos una lista con las notas que se tienen
    notas = [ACS1, ACS2, ACS3, ACS4]

    # Sumamos las décimas a la mejor nota
    # (después de haber calculado XACS)
    max_ac = max(notas)
    notas[notas.index(max_ac)] = max_ac + (DEC_ACF / 10)

    # Promedio eliminando la peor nota
    AC = round((sum(notas) - min(notas)) / 3, 2)

    print(f"Tu promedio de actividades es: {AC}")