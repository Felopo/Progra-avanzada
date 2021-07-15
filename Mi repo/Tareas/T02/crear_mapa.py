import os
from PyQt5.QtCore import QObject, pyqtSignal


class CreadorMapa(QObject):

    senal_mapa = pyqtSignal(str)
    senal_mapa_enviar_datos_mapa = pyqtSignal(dict, list)

    def __init__(self):
        super().__init__()
        self.senal_mapa.connect(self.creador_de_mapa)

    def creador_de_mapa(self, nombre_mapa):
        lista_mapa = []
        nombre_mapa = nombre_mapa + ".txt"
        with open(os.path.join("mapas", nombre_mapa), "r+", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip().split(" ")
                lista_mapa.append(linea)
        dict_posiciones = {"rocas": [],
                           "casa": [],
                           "tienda": [],
                           "pasto": [],
                           "largo_mapa": 0,
                           "ancho_mapa": 0}
        lista_espacios_cultivables = []
        largo_mapa = 0
        ancho_mapa = 0
        for fila in range(len(lista_mapa)):
            largo_mapa += 1
            ancho_mapa = 0
            espacio_cultivable = []
            cantidad_espacio_cultivable = 0
            for columna in range(len(lista_mapa[0])):
                ancho_mapa += 1
                if lista_mapa[fila][columna] == "R":
                    dict_posiciones["rocas"].append([fila, columna])
                    lista_mapa[fila][columna] = "O"
                elif lista_mapa[fila][columna] == "H":
                    dict_posiciones["casa"].append([fila, columna])
                    dict_posiciones["casa"].append([fila + 1, columna])
                    lista_mapa[fila + 1][columna] = "N"
                    dict_posiciones["casa"].append([fila, columna + 1])
                    lista_mapa[fila][columna + 1] = "N"
                    dict_posiciones["casa"].append([fila + 1, columna + 1])
                    lista_mapa[fila + 1][columna + 1] = "N"
                    dict_posiciones["pasto"].append([fila, columna])
                    dict_posiciones["pasto"].append([fila + 1, columna])
                    dict_posiciones["pasto"].append([fila, columna + 1])
                    dict_posiciones["pasto"].append([fila + 1, columna + 1])
                elif lista_mapa[fila][columna] == "T":
                    dict_posiciones["tienda"].append([fila, columna])
                    dict_posiciones["tienda"].append([fila + 1, columna])
                    lista_mapa[fila + 1][columna] = "N"
                    dict_posiciones["tienda"].append([fila, columna + 1])
                    lista_mapa[fila][columna + 1] = "N"
                    dict_posiciones["tienda"].append([fila + 1, columna + 1])
                    lista_mapa[fila + 1][columna + 1] = "N"
                    dict_posiciones["pasto"].append([fila, columna])
                    dict_posiciones["pasto"].append([fila + 1, columna])
                    dict_posiciones["pasto"].append([fila, columna + 1])
                    dict_posiciones["pasto"].append([fila + 1, columna + 1])
                elif lista_mapa[fila][columna] == "C":
                    largo_cultivable = 1
                    ancho_cultivable = 1
                    lista_alrededores = []
                    if lista_mapa[fila - 1][columna] != "C" and \
                            lista_mapa[fila][columna - 1] != "C":
                        while True:
                            try:
                                if lista_mapa[fila][columna + largo_cultivable] == "C":
                                    largo_cultivable += 1
                                else:
                                    break
                            except IndexError:
                                break
                        while True:
                            try:
                                if lista_mapa[fila + ancho_cultivable][columna] == "C":
                                    ancho_cultivable += 1
                                else:
                                    break
                            except IndexError:
                                break
                        lista_espacios_cultivables.append([largo_cultivable, ancho_cultivable])
                        alrededor_f_u = -1
                        alrededor_c_u = -1
                        alrededor_f_d = ancho_cultivable
                        alrededor_c_d = -1
                        alrededor_f_r = 0
                        alrededor_c_r = largo_cultivable
                        alrededor_f_l = 0
                        alrededor_c_l = 1
                        fila_u = True
                        columna_r = False
                        fila_d = False
                        columna_l = False
                        for alrededores in range(2 * (largo_cultivable + ancho_cultivable) + 4):
                            if fila_u:
                                lista_alrededores.append(
                                    [fila + alrededor_f_u, columna + alrededor_c_u])
                                lista_mapa[fila + alrededor_f_u][columna + alrededor_c_u] = "N"
                                alrededor_c_u += 1
                                if alrededor_c_u == largo_cultivable + 1:
                                    columna_r = True
                                    fila_u = False
                            elif columna_r:
                                lista_alrededores.append(
                                    [fila + alrededor_f_r, columna + alrededor_c_r])
                                lista_mapa[fila + alrededor_f_r][columna + alrededor_c_r] = "N"
                                alrededor_f_r += 1
                                if alrededor_f_r == ancho_cultivable:
                                    fila_d = True
                                    columna_r = False
                            elif fila_d:
                                lista_alrededores.append(
                                    [fila + alrededor_f_d, columna + alrededor_c_d])
                                lista_mapa[fila + alrededor_f_d][columna + alrededor_c_d] = "N"
                                alrededor_c_d += 1
                                if alrededor_c_d == largo_cultivable + 1:
                                    columna_l = True
                                    fila_d = False
                            elif columna_l:
                                lista_alrededores.append(
                                    [fila + alrededor_f_l, columna - alrededor_c_l])
                                lista_mapa[fila + alrededor_f_l][columna - alrededor_c_l] = "N"
                                alrededor_f_l += 1
                                if alrededor_f_l == ancho_cultivable:
                                    columna_l = False
                        lista_espacios_cultivables.append(lista_alrededores)
                    espacio_cultivable.append((fila, columna))
                    bool_c_filas = True
                    cantidad_filas = 1
                    cantidad_espacio_cultivable += 1
                    if lista_mapa[fila][columna + 1] != "C" and \
                            lista_mapa[fila + 1][columna] == "C":
                        c_retroceder = cantidad_espacio_cultivable - 1
                        while bool_c_filas:
                            lista_mapa[
                                    fila + cantidad_filas][columna - c_retroceder] = "N"
                            espacio_cultivable.append((fila + cantidad_filas,
                                                       columna - c_retroceder))
                            if lista_mapa[fila + cantidad_filas][columna - c_retroceder + 1] != \
                                    "C" and \
                                    lista_mapa[fila + cantidad_filas + 1][columna - c_retroceder] \
                                    == "C":
                                cantidad_filas += 1
                                c_retroceder = cantidad_espacio_cultivable
                            if lista_mapa[fila
                                          + cantidad_filas + 1][columna - c_retroceder] != "C" and \
                                    lista_mapa[fila
                                               + cantidad_filas][columna - c_retroceder + 1] != "C":
                                lista_espacios_cultivables.append(espacio_cultivable)
                                break
                            c_retroceder -= 1
                elif lista_mapa[fila][columna] == "N":
                    lista_mapa[fila][columna] = "Nada"
        for fila in range(len(lista_mapa)):
            for columna in range(len(lista_mapa[0])):
                if lista_mapa[fila][columna] == "O":
                    dict_posiciones["pasto"].append([fila, columna])
        dict_posiciones["largo_mapa"] = largo_mapa
        dict_posiciones["ancho_mapa"] = ancho_mapa
        self.senal_mapa_enviar_datos_mapa.emit(dict_posiciones, lista_espacios_cultivables)
