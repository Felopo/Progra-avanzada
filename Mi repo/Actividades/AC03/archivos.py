from yoNube import descargar
from decodificador import decodificar

from collections import namedtuple
import os


# ------ ESTRUCTURAS ------

Cancion = namedtuple("Cancion", ["id", "nombre", "id_artista", "duracion"])
Artista = namedtuple("Artista", ["id", "nombre", "genero", "ano_formacion"])
Usuario = namedtuple("Usuario", ["nombre", "username", "fecha_ingreso"])
Rating = namedtuple("Rating", ["username", "id_cancion", "rating"])

# ----- DECORADOR -------


def desencriptar(funcion_decodificadora, tipo_archivo):
    def decorador(funcion_a_decorar):
        def wrapper(*args, **kwargs):
            for linea in funcion_a_decorar:
                if tipo_archivo == "canciones":
                    funcion_decodificadora(linea)
                    gen_c = Cancion(id=linea[0], nombre=linea[1], id_artista=linea[2],
                                    duracion=linea[3])
                    yield gen_c
                elif tipo_archivo == "artistas":
                    funcion_decodificadora(linea)
                    gen_a = Artista(id=linea[0], nombre=linea[1], genero=linea[2],
                                    ano_formacion=linea[3])
                    yield gen_a
                elif tipo_archivo == "usuarios":
                    funcion_decodificadora(linea)
                    gen_u = Usuario(nombre=linea[0], username=linea[1], fecha_ingreso=linea[2])
                    yield gen_u
                elif tipo_archivo == "ratings":
                    funcion_decodificadora(linea)
                    gen_r = Rating(username=linea[0], id_cancion=linea[1], rating=linea[2])
                    yield gen_r
            return funcion_a_decorar(*args, **kwargs)
        return wrapper
    return decorador


# ------------------------------------------------------------

# --------- NO MODIFICAR LAS FUNCIONES, SOLO DECORAR ---------

# ------------------------------------------------------------


@desencriptar(decodificar, "canciones")
def leer_canciones(path):
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


@desencriptar(decodificar, "artistas")
def leer_artistas(path):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide por las comas, por lo tanto entrega
    4 elementos.

    Decorar para:
    =============
    - Desencriptar los datos.
    - Entregar las instancias correspondientes.
    """
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


@desencriptar(decodificar, "usuarios")
def leer_usuarios(path):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide por las comas, por lo tanto entrega
    3 elementos.

    Decorar para:
    =============
    - Desencriptar los datos.
    - Entregar las instancias correspondientes.
    """
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


@desencriptar(decodificar, "ratings")
def leer_ratings(path):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide por las comas, por lo tanto entrega
    3 elementos.

    Decorar para:
    =============
    - Desencriptar los datos.
    - Entregar las instancias correspondientes.
    """
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


if __name__ == "__main__":
    ruta_canciones = os.path.join("data_base", "canciones.csv")
    canciones = leer_canciones(ruta_canciones)
    ruta_artistas = os.path.join("data_base", "artistas.csv")
    artistas = leer_artistas(ruta_artistas)
    ruta_usuarios = os.path.join("data_base", "usuarios.csv")
    usuarios = leer_usuarios(ruta_usuarios)
    ruta_ratings = os.path.join("data_base", "ratings.csv")
    ratings = leer_ratings(ruta_ratings)

    generadores = [canciones, artistas, usuarios, ratings]

    for gen in generadores:
        print(f"\nProbando generador : ")
        print(next(gen))
        print(next(gen))
        print(next(gen))
        print(next(gen))
