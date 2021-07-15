import random
import tablero
import parametros
import math
import sys
import os.path
import os

def menu_inicio():
    inicio = input("Seleccione una opción: [1] Comenzar Nueva Partida \n"
                   "                       [2] Cargar Partida \n"
                   "                       [3] Ver Ranking \n"
                   "                       [4] Salir Del Juego \n"
                   "                       Indique su opción (1, 2, 3, 4): ").strip()
    return inicio


def crear_tablero():
    tablero = []
    posiciones_para_poner_legos = []
    lista_anchos = []
    largo_tablero_n = input("Qué largo quiere que tenga el tablero? (Entre 3 y 15): ").strip()
    ancho_tablero_m = input("Qué ancho quiere que tenga el tablero? (Entre 3 y 15): ").strip()
    if not(largo_tablero_n.isdigit()) or not(ancho_tablero_m.isdigit()):
        print("Ingrese dimensiones del tablero entre 3 y 15 por favor")
        return ""
    elif largo_tablero_n.isdigit() and ancho_tablero_m.isdigit():
        largo_tablero_n = int(largo_tablero_n)
        ancho_tablero_m = int(ancho_tablero_m)
    if largo_tablero_n not in range(3, 16) or ancho_tablero_m not in range(3, 16):
        print("Ingrese dimensiones del tablero entre 3 y 15 por favor")
        return ""
    elif largo_tablero_n in range(3, 16) and ancho_tablero_m in range(3, 16):
        cantidad_de_legos = math.ceil(largo_tablero_n * ancho_tablero_m * parametros.PROB_LEGO)
        n = largo_tablero_n
        m = ancho_tablero_m
        for i in range(cantidad_de_legos):
            posicion_lego = random.randint(0, (n * m) - 1)
            no_se_ponga_lego = True
            while no_se_ponga_lego:
                if posicion_lego not in posiciones_para_poner_legos:
                    posiciones_para_poner_legos.append(posicion_lego)
                    no_se_ponga_lego = False
                posicion_lego = random.randint(0, (n * m) - 1)
        donde_poner_legos = 0
        se_puso_lego = False
        for ancho in range(n):
            for largo in range(m):
                for k in range(len(posiciones_para_poner_legos)):
                    if donde_poner_legos == posiciones_para_poner_legos[k]:
                        posiciones_para_poner_legos[k] = " "
                        lista_anchos.append("L")
                        se_puso_lego = True
                if not se_puso_lego:
                    lista_anchos.append(" ")
                donde_poner_legos += 1
                se_puso_lego = False
            tablero.append(lista_anchos)
            lista_anchos = []
        return tablero


def menu_juego(tablero_legos, tablero_jugador, nombre_usuario):
    print("Estado actual del Tablero: ")
    tablero.print_tablero(tablero_jugador)
    opciones_menu_juego = ["1", "2", "3", "4"]
    sigue_jugando = True
    while sigue_jugando:
        print("Seleccione una opción: ")
        pregunta_menu_juego = input("[1] Descubrir Una Baldosa \n"
                                    "[2] Guardar Partida \n"
                                    "[3] Guardar y Salir \n"
                                    "[4] Salir Sin Guardar \n"
                                    "Indique su Opción (1, 2, 3, 4): ").strip()
        if pregunta_menu_juego == "1" and pregunta_menu_juego in opciones_menu_juego:
            lista_numeros_filas = []
            lista_letras_columnas = []
            abecedario = "ABCDEFGHIJKLMNO"
            for numero in range(len(tablero_legos)):
                lista_numeros_filas.append(str(numero))
            for letra in range(len(tablero_legos[0])):
                lista_letras_columnas.append(abecedario[letra])
            print("Qué Fila de Baldosa quiere descubrir?")
            fila_bal_a_des = input("Opciones: (" + ",".join(lista_numeros_filas) + "): ").strip()
            print("Qué Columna de Baldosa quiere descubrir?")
            col_bal_a_des = input("Opciones: (" + ",".join(lista_letras_columnas) + "): ").strip()
            col_bal_a_des = col_bal_a_des.capitalize()
            if (fila_bal_a_des in lista_numeros_filas) and (col_bal_a_des in abecedario):
                for numero in range(len(abecedario)):
                    if col_bal_a_des == abecedario[numero]:
                        col_bal_a_des = numero
                result_bal = descubrir_baldosa(fila_bal_a_des, col_bal_a_des, tablero_legos)
                legos_tablero = 0
                for i in range(len(tablero_legos)):
                    for j in range(len(tablero_legos[0])):
                        if tablero_legos[i][j] == "L":
                            legos_tablero += 1
                if result_bal != tablero_legos:
                    print("Juego Terminado!, Has Perdido :c")
                    tablero.print_tablero(tablero_legos)
                    celdas_descubiertas = 0
                    for i in range(len(tablero_legos)):
                        for j in range(len(tablero_legos[0])):
                            if str(tablero_legos[i][j]).isdigit():
                                celdas_descubiertas += 1
                    puntaje = str(legos_tablero * celdas_descubiertas * parametros.POND_PUNT)
                    print("Tu Puntaje final es: " + puntaje)
                    archivo_puntajes = open("puntajes.txt", "a")
                    archivo_puntajes.write(nombre_usuario + ": " + puntaje + "\n")
                    archivo_puntajes.close()
                    sys.exit()
                else:
                    print("\nBuena Jugada!!!")
                    print("Asi quedó el tablero: \n")
                    fila_bal_a_des = int(fila_bal_a_des)
                    col_bal_a_des = int(col_bal_a_des)
                    pieza_descubierta_tab_legos = tablero_legos[fila_bal_a_des][col_bal_a_des]
                    tablero_jugador[fila_bal_a_des][col_bal_a_des] = pieza_descubierta_tab_legos
                    tablero.print_tablero(tablero_jugador)
                    todas_descubiertas = True
                    for i in range(len(tablero_jugador)):
                        for j in range(len(tablero_jugador[i])):
                            if tablero_legos[i][j] == " ":
                                todas_descubiertas = False
                    if todas_descubiertas:
                        print("Partida Terminada")
                        celdas_descubiertas = 0
                        for i in range(len(tablero_jugador)):
                            for j in range(len(tablero_jugador[0])):
                                if str(tablero_legos[i][j]).isdigit():
                                    celdas_descubiertas += 1
                        p_final = str(legos_tablero * celdas_descubiertas * parametros.POND_PUNT)
                        print("Tu Puntaje final es: " + p_final)
                        archivo_puntajes_finales = open("puntajes.txt", "a")
                        archivo_puntajes_finales.write(nombre_usuario + ": " + p_final + "\n")
                        archivo_puntajes_finales.close()
                        sys.exit()
            else:
                print("")
                print("Ingrese dimensiones del Tablero válidas por favor...")
                print("")
        elif pregunta_menu_juego == "2" and pregunta_menu_juego in opciones_menu_juego:
            guardar_tableros(tablero_legos, tablero_jugador, nombre_usuario)
            print("\nPartida Guardada con éxito\n")
        elif pregunta_menu_juego == "3" and pregunta_menu_juego in opciones_menu_juego:
            guardar_tableros(tablero_legos, tablero_jugador, nombre_usuario)
            print("\nPartida Guardada con éxito\n")
            print("Saliendo del Juego...")
            sys.exit()
        elif pregunta_menu_juego == "4" and pregunta_menu_juego in opciones_menu_juego:
            celdas_descubiertas = 0
            for i in range(len(tablero_legos)):
                for j in range(len(tablero_legos[0])):
                    if str(tablero_legos[i][j]).isdigit():
                        celdas_descubiertas += 1
            legos_tablero = 0
            for i in range(len(tablero_legos)):
                for j in range(len(tablero_legos[0])):
                    if tablero_legos[i][j] == "L":
                        legos_tablero += 1
            puntaje = str(legos_tablero * celdas_descubiertas * parametros.POND_PUNT)
            print("Su Puntaje era: " + puntaje)
            print("Saliendo del Juego...")
            sys.exit()
        else:
            print("")
            print("Ingrese una opción válida...")
            print("")


def guardar_tableros(lista_leg, lista_jug, nombre):
    for i in range(len(lista_leg)):
        for j in range(len(lista_leg[0])):
            if lista_leg[i][j] == " ":
                lista_leg[i][j] = "!"
    for i in range(len(lista_jug)):
        for j in range(len(lista_jug[0])):
            if lista_jug[i][j] == " ":
                lista_jug[i][j] = "!"
    with open(os.path.join("partidas", f"{nombre}.txt"), "w") as archivo:
        for lista in lista_leg:
            archivo.write(";".join(str(v) for v in lista) + "\n")
        for lista in lista_jug:
            archivo.write(";".join(str(v) for v in lista) + "\n")


def cargar_lista(nombre):
    with open(os.path.join("partidas", f"{nombre}.txt")) as archivo:
        lineas = archivo.readlines()
        tablero = []
        for linea in lineas:
            tablero.append(linea.strip().split(";"))
        return tablero


def descubrir_baldosa(fila, columna, tablero):
    largo_tablero = len(tablero) - 1
    ancho_tablero = len(tablero[0]) - 1
    fila = int(fila)
    columna = int(columna)
    contador_de_legos = 0
    if (fila == 0) and (columna == 0):
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            if tablero[fila][columna + 1] == "L":
                contador_de_legos += 1
            if tablero[fila + 1][columna] == "L":
                contador_de_legos += 1
            if tablero[fila + 1][columna + 1] == "L":
                contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    elif (fila == 0) and (columna == ancho_tablero):
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            if tablero[fila][columna - 1] == "L":
                contador_de_legos += 1
            if tablero[fila + 1][columna - 1] == "L":
                contador_de_legos += 1
            if tablero[fila + 1][columna] == "L":
                contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    elif (fila == largo_tablero) and (columna == 0):
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            if tablero[fila - 1][columna] == "L":
                contador_de_legos += 1
            if tablero[fila - 1][columna + 1] == "L":
                contador_de_legos += 1
            if tablero[fila][columna + 1] == "L":
                contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    elif (fila == largo_tablero) and (columna == ancho_tablero):
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            if tablero[fila][columna - 1] == "L":
                contador_de_legos += 1
            if tablero[fila - 1][columna - 1] == "L":
                contador_de_legos += 1
            if tablero[fila - 1][columna] == "L":
                contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    elif fila == 0:
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            for i in range(1, ancho_tablero):
                if columna == i:
                    if tablero[fila][i - 1] == "L":
                        contador_de_legos += 1
                    if tablero[fila + 1][i - 1] == "L":
                        contador_de_legos += 1
                    if tablero[fila + 1][i] == "L":
                        contador_de_legos += 1
                    if tablero[fila + 1][i + 1] == "L":
                        contador_de_legos += 1
                    if tablero[fila][i + 1] == "L":
                        contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    elif columna == 0:
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            for j in range(1, largo_tablero):
                if fila == j:
                    if tablero[j - 1][columna] == "L":
                        contador_de_legos += 1
                    if tablero[j - 1][columna + 1] == "L":
                        contador_de_legos += 1
                    if tablero[j][columna + 1] == "L":
                        contador_de_legos += 1
                    if tablero[j + 1][columna + 1] == "L":
                        contador_de_legos += 1
                    if tablero[j + 1][columna] == "L":
                        contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    elif fila == largo_tablero:
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            for i in range(1, ancho_tablero):
                if columna == i:
                    if tablero[fila][i - 1] == "L":
                        contador_de_legos += 1
                    if tablero[fila - 1][i - 1] == "L":
                        contador_de_legos += 1
                    if tablero[fila - 1][i] == "L":
                        contador_de_legos += 1
                    if tablero[fila - 1][i + 1] == "L":
                        contador_de_legos += 1
                    if tablero[fila][i + 1] == "L":
                        contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    elif columna == ancho_tablero:
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            for j in range(1, largo_tablero):
                if fila == j:
                    if tablero[j - 1][columna] == "L":
                        contador_de_legos += 1
                    if tablero[j - 1][columna - 1] == "L":
                        contador_de_legos += 1
                    if tablero[j][columna - 1] == "L":
                        contador_de_legos += 1
                    if tablero[j + 1][columna - 1] == "L":
                        contador_de_legos += 1
                    if tablero[j + 1][columna] == "L":
                        contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    else:
        if tablero[fila][columna] == "L":
            pierde = True
            return pierde
        else:
            for i in range(1, largo_tablero):
                for j in range(1, ancho_tablero):
                    if (fila == i) and (columna == j):
                        if tablero[i - 1][j - 1] == "L":
                            contador_de_legos += 1
                        if tablero[i - 1][j] == "L":
                            contador_de_legos += 1
                        if tablero[i - 1][j + 1] == "L":
                            contador_de_legos += 1
                        if tablero[i][j + 1] == "L":
                            contador_de_legos += 1
                        if tablero[i + 1][j + 1] == "L":
                            contador_de_legos += 1
                        if tablero[i + 1][j] == "L":
                            contador_de_legos += 1
                        if tablero[i + 1][j - 1] == "L":
                            contador_de_legos += 1
                        if tablero[i][j - 1] == "L":
                            contador_de_legos += 1
            tablero[fila][columna] = contador_de_legos
    return tablero


opciones_menu_inicio = ["1", "2", "3", "4"]
tablero_legos = ""
sigue_juego = True
while sigue_juego:
    pregunta_menu_inicio = menu_inicio()
    if pregunta_menu_inicio in opciones_menu_inicio:
        if pregunta_menu_inicio == "1":
            while tablero_legos == "":
                tablero_legos = crear_tablero()
            nombre_usuario = str(input("Ingrese un nombre de usuario: ")).strip()
            tablero_jugador = []
            filas_tablero_juego = []
            for i in range(len(tablero_legos)):
                for j in range(len(tablero_legos[i])):
                    filas_tablero_juego.append(" ")
                tablero_jugador.append(filas_tablero_juego)
                filas_tablero_juego = []
            menu_juego(tablero_legos, tablero_jugador, nombre_usuario)
        elif pregunta_menu_inicio == "2":
            nombre_de_usuario = input("Ingrese su Nombre de Usuario: ").strip()
            path_1 = "partidas/"
            path_a_cargar = path_1 + nombre_de_usuario + ".txt"
            if os.path.isfile(path_a_cargar):
                dos_tableros = cargar_lista(nombre_de_usuario)
                for i in range(len(dos_tableros)):
                    for j in range(len(dos_tableros[0])):
                        if dos_tableros[i][j] == "!":
                            dos_tableros[i][j] = " "
                tablero_legos = dos_tableros[0: int(len(dos_tableros) / 2)]
                tablero_jugador = dos_tableros[int(len(dos_tableros) / 2):]
                menu_juego(tablero_legos, tablero_jugador, nombre_de_usuario)
                print("Partida Cargada con éxito...\n")
            else:
                print("\nIngrese un Nombre de Usuario válido por favor...\n")

        elif pregunta_menu_inicio == "3":
            archivo_visualizador_de_puntajes = open("puntajes.txt", "r")
            lineas_del_archivo = archivo_visualizador_de_puntajes.readlines()
            lineas_del_archivo_verdaderas = []
            for linea in lineas_del_archivo:
                linea = linea.split()
                lineas_del_archivo_verdaderas.append(linea)
            lineas_del_archivo_verdaderas.sort(key=lambda x: int(x[1]), reverse=True)
            contador_puntajes = 1
            print("\nLos 10 Puntajes más altos son: ")
            for i in range(len(lineas_del_archivo_verdaderas)):
                for j in range(len(lineas_del_archivo_verdaderas[0])):
                    if j == 1:
                        linea = lineas_del_archivo_verdaderas[i][j]
                        n_usuario = lineas_del_archivo_verdaderas[i][j - 1]
                print(str(contador_puntajes) + "- " + n_usuario + str(linea))
                contador_puntajes += 1
                if contador_puntajes == 11:
                    break
            print("Hay " + str(contador_puntajes - 1) + " Puntajes\n")
            archivo_visualizador_de_puntajes.close()
        elif pregunta_menu_inicio == "4":
            print("Saliendo del Juego...")
            sys.exit()
    else:
        print("")
        print("Ingrese una opción válida...")
        print("")
