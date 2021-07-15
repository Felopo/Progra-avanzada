import pickle
import re


class Piloto:
    def __init__(self, nombre, alma, edad, *args, **kwargs):
        self.nombre = nombre
        self.alma = alma
        self.edad = edad

    def __setstate__(self, state):
        state.update(aumentar_sincronizacion(state))
        self.__dict__ = state


def cargar_almas(ruta):
    with open(ruta, "rb") as archivo:
        datos = pickle.load(archivo)
        return datos


def aumentar_sincronizacion(estado):
    nueva_alma = re.sub("(E).*(G+).*(O)", "", estado["alma"])
    estado["alma"] = nueva_alma
    if estado["nombre"] == "Shinji Gonzalez":
        print(nueva_alma)
    return estado


if __name__ == '__main__':
    try:
        pilotos = cargar_almas('pilotos.magi')
        if pilotos:
            print("ENZOHOR200: Sincronizacion de los pilotos ESTABLE.")
            
    except Exception as error:
        print(f'Error: {error}')
        print("ENZOHOR501: CRITICO Sincronizacion de los pilotos INESTABLE")
