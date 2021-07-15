from collections import deque
from collections import namedtuple


DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    lista_alumnos = []
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    with open(ruta_archivo_alumnos, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip().split(";")
            registrar = namedtuple("Alumno", ["habilidades"])
            alumno = registrar(linea[1])
            lista_alumnos.append(alumno)
    return lista_alumnos


def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    dict_ayudantes = {"Piso -1": deque(),
                      "Piso -2": deque(),
                      "Piso -3": deque(),
                      "Piso -4": deque()}
    with open(ruta_archivo_ayudantes, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip().split(";")
            if linea[1] == "Chief Tamburini":
                dict_ayudantes["Piso -4"].append(linea)
            elif linea[1] == "Jefe":
                dict_ayudantes["Piso -3"].append(linea)
            elif linea[1] == "Mentor":
                dict_ayudantes["Piso -2"].append(linea)
            elif linea[1] == "Nuevo":
                dict_ayudantes["Piso -1"].append(linea)
    return dict_ayudantes
