import parametros
import entidades
import funciones
from abc import ABC, abstractmethod
import time


class Menu(ABC):
    def __init__(self):
        self.no_ingresa_input_valido = True
        self.equivocacion_usuario = "Ingrese una opción válida..."
        self.nombre_usuario = None
        self.vehiculos = []
        self.pista = None
        self.juego = None

    @abstractmethod
    def ingresar_input(self):
        pass

    def agregar_vehiculo(self, vehiculo):
        pass


class MenuPreparacionCarrera(Menu):
    def __init__(self, juego):
        super().__init__()
        self.juego = juego

    def ingresar_input(self):
        pistas = []
        with open(parametros.PATHS["PISTAS"][1], "r+", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip().split(",")
                pistas.append(linea)
        nombre_pistas = funciones.buscar_nombre(pistas)
        vueltas_pistas = funciones.buscar_num_vueltas(pistas)
        tipo_pistas = funciones.buscar_tipo_pista(pistas)
        dict_pistas_ord = funciones.ordenar_columnas_archivo(pistas)
        while self.no_ingresa_input_valido:
            print()
            print("En que pista desea paricipar? ")
            print()
            print("*-----Pistas disponibles-----*")
            cantidad_pistas = 0
            lista_pistas = []
            for i in range(1, 7):
                print(f"{i}) *Nombre Pista*: {nombre_pistas[i]}  *Pista*: {tipo_pistas[i]} "
                      f"*Núm vueltas*: {vueltas_pistas[i]}")
                cantidad_pistas += 1
                lista_pistas.append(str(cantidad_pistas))
            eleccion = input(f"Opciones: (" + ",".join(lista_pistas) + "): ").strip()
            if eleccion in lista_pistas:
                nombre_p = pistas[int(eleccion)][dict_pistas_ord["Nombre"]]
                tipo_p = pistas[int(eleccion)][dict_pistas_ord["Tipo"]]
                hielo_p = pistas[int(eleccion)][dict_pistas_ord["Hielo"]]
                rocas_p = pistas[int(eleccion)][dict_pistas_ord["Rocas"]]
                dificultad_p = pistas[int(eleccion)][dict_pistas_ord["Dificultad"]]
                num_vueltas_p = pistas[int(eleccion)][dict_pistas_ord["NúmeroVueltas"]]
                contrincantes_p = pistas[int(eleccion)][dict_pistas_ord["Contrincantes"]].split(";")
                largo_p = pistas[int(eleccion)][dict_pistas_ord["LargoPista"]]
                if tipo_pistas[int(eleccion)] == "pista hielo":
                    pista = entidades.PistaHielo(nombre_p, tipo_p, hielo_p, rocas_p, dificultad_p,
                                                 num_vueltas_p, contrincantes_p, largo_p)
                    self.juego.pista = pista
                elif tipo_pistas[int(eleccion)] == "pista rocosa":
                    pista = entidades.PistaRoca(nombre_p, tipo_p, hielo_p, rocas_p, dificultad_p,
                                                num_vueltas_p, contrincantes_p, largo_p)
                    self.juego.pista = pista
                elif tipo_pistas[int(eleccion)] == "pista suprema":
                    pista = entidades.PistaSuprema(nombre_p, tipo_p, hielo_p, rocas_p, dificultad_p,
                                                   num_vueltas_p, contrincantes_p, largo_p)
                    self.juego.pista = pista
                self.no_ingresa_input_valido = False
                self.elegir_vehiculo()
                MenuCarrera()
            else:
                print()
                print(self.equivocacion_usuario)
        return self.juego

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def elegir_vehiculo(self):
        self.no_ingresa_input_valido = True
        while self.no_ingresa_input_valido:
            print()
            print("Qué vehículo desea usar para esta carrera: ")
            cantidad_vehiculos = 0
            lista_vehiculos = []
            for i, vehiculo in enumerate(self.juego.vehiculos):
                print(f"{i}) -Nombre Vehículo: {vehiculo.nombre}  "
                      f"-Tipo Vehículo: {vehiculo.categoria}")
                lista_vehiculos.append(str(cantidad_vehiculos))
                cantidad_vehiculos += 1
            opciones = input(f"Opciones: (" + ",".join(lista_vehiculos) + "): ").strip()
            if opciones in lista_vehiculos:
                self.juego.vehiculo = self.juego.vehiculos[int(opciones)]
                print()
                print("Vehículo elegido...")
                print()
                print("................................................")
                print("Cargando Preparativos para iniciar la carrera...")
                print("................................................")
                time.sleep(5)
                print("-"*10)
                print("La Carrera ha Comenzado!!!!")
                print("-"*10)
                self.no_ingresa_input_valido = False
            else:
                print(self.equivocacion_usuario)


class MenuCarrera(Menu):
    def ingresar_input(self):
        while self.no_ingresa_input_valido:
            ingresar_a_los_pits = input("Quiere entrar a los pits?: \n"
                                        "[1] SI \n"
                                        "[2] NO \n"
                                        "Opciones(1,2): ").strip()
            print()
            if ingresar_a_los_pits == "1":
                self.no_ingresa_input_valido = False
                return "ir_a_los_pits"
            elif ingresar_a_los_pits == "2":
                self.no_ingresa_input_valido = False
                return "continuar_carrera"
            else:
                print(self.equivocacion_usuario)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)


class MenuPits(Menu):
    def __init__(self, juego):
        super().__init__()
        self.juego = juego

    def ingresar_input(self):
        costo_mejora_chasis = parametros.MEJORAS["CHASIS"]["COSTO"]
        costo_mejora_carroceria = parametros.MEJORAS["CARROCERIA"]["COSTO"]
        costo_mejora_ruedas = parametros.MEJORAS["RUEDAS"]["COSTO"]
        costo_mejora_motor = parametros.MEJORAS["MOTOR"]["COSTO"]
        costo_mejora_zapatillas = parametros.MEJORAS["ZAPATILLAS"]["COSTO"]
        self.no_ingresa_input_valido = True
        while self.no_ingresa_input_valido:
            print("-------Los Pits-------")
            if self.juego.vehiculo.num_ruedas == 4:
                print(f"Dinero actual del Usuario: ${self.juego.jugador.dinero}")
                print(f"Partes a mejorar: \n"
                      f"1) Chasis         ${costo_mejora_chasis} \n"
                      f"2) Carrocería     ${costo_mejora_carroceria} \n"
                      f"3) Ruedas         ${costo_mejora_ruedas} \n"
                      f"4) Motor          ${costo_mejora_motor}")
            elif self.juego.vehiculo.num_ruedas == 2:
                print(f"Dinero actual del Usuario: ${self.juego.jugador.dinero}")
                print(f"Partes a mejorar: \n"
                      f"1) Chasis         ${costo_mejora_chasis} \n"
                      f"2) Carrocería     ${costo_mejora_carroceria} \n"
                      f"3) Ruedas         ${costo_mejora_ruedas} \n"
                      f"4) Zapatillas     ${costo_mejora_zapatillas}")
            opciones = input("Ingrese el número de la parte a mejorar "
                             "(ingrese 0 para regresar): ").strip()
            if opciones == "1" or opciones == "2" or opciones == "3" or opciones == "4":
                self.no_ingresa_input_valido = False
                self.mejorar_parte(opciones, self.juego.vehiculo.num_ruedas)
                return self.juego
            elif opciones == "0":
                return self.juego
            else:
                print(self.equivocacion_usuario)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mejorar_parte(self, parte, cantidad_ruedas):
        if parte == "1":
            lista_para_setter = ["chasis", self.juego.jugador]
            self.juego.vehiculo.mejorar_pieza = lista_para_setter
        elif parte == "2":
            lista_para_setter = ["carrocería", self.juego.jugador]
            self.juego.vehiculo.mejorar_pieza = lista_para_setter
        elif parte == "3":
            lista_para_setter = ["ruedas", self.juego.jugador]
            self.juego.vehiculo.mejorar_pieza = lista_para_setter
        elif parte == "4" and cantidad_ruedas == 4:
            lista_para_setter = ["motor", self.juego.jugador]
            self.juego.vehiculo.mejorar_pieza = lista_para_setter
        elif parte == "4" and cantidad_ruedas == 2:
            lista_para_setter = ["zapatillas", self.juego.jugador]
            self.juego.vehiculo.mejorar_pieza = lista_para_setter

