from abc import ABC, abstractmethod
import parametros
import funciones
import entidades
import juego
import menus_2
import os.path
import sys


class Menu(ABC):
    def __init__(self):
        self.no_ingresa_input_valido = True
        self.equivocacion_usuario = "Ingrese una opción válida..."
        self.nombre_usuario = None
        self.vehiculos = []
        self.pista = None
        self.vehiculo_carrera = None
        self.juego = None

    @abstractmethod
    def ingresar_input(self):
        pass

    def agregar_vehiculo(self, vehiculo):
        pass


class MenuDeSesion(Menu):
    def __init__(self):
        super().__init__()
        self.ruta_pil = parametros.PATHS["PILOTOS"]
        self.ruta_vehi = parametros.PATHS["VEHICULOS"]
        self.juego = None

    def ingresar_input(self):
        while self.no_ingresa_input_valido:
            print()
            print("Que desea hacer: ")
            opciones = input("[1] Crear nueva partida \n"
                             "[2] Cargar partida \n"
                             "Opciones(1,2): ").strip()
            if opciones == "1":
                self.no_ingresa_input_valido = False
                return "nueva_partida"
            elif opciones == "2":
                self.no_ingresa_input_valido = False
                return "carga_partida"
            else:
                print(self.equivocacion_usuario)
        self.no_ingresa_input_valido = True

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def crear_nueva_partida(self):
        lista_archivo_pil = []
        with open(self.ruta_pil[1], "r+", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip().split(",")
                lista_archivo_pil.append(linea)
        lista_nombres_archivo_pil = funciones.buscar_nombre(lista_archivo_pil)
        diccionario_ordenado_pil = funciones.ordenar_columnas_archivo(lista_archivo_pil)
        lista_archivo_vehi = []
        with open(self.ruta_vehi[1], "r+", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip().split(",")
                lista_archivo_vehi.append(linea)
        lista_nombres_archivo_vehi = funciones.buscar_nombre(lista_archivo_vehi)
        diccionario_ordenado_vehi = funciones.ordenar_columnas_archivo(lista_archivo_vehi)
        self.no_ingresa_input_valido = True
        while self.no_ingresa_input_valido:
            print()
            nom_nuevo_usuario = input("Nombre de usuario: ").strip()
            if all(caracter.isspace() or caracter.isalnum() for caracter in nom_nuevo_usuario) \
                    and nom_nuevo_usuario not in lista_nombres_archivo_pil:
                self.no_ingresa_input_valido = False
                input_valido_equipos = True
                while input_valido_equipos:
                    equipo = input("Elija un equipo: \n"
                                   "[1] Tareos \n"
                                   "[2] Hibridos \n"
                                   "[3] Docencios \n"
                                   "Opciones (1,2,3): ").strip()
                    if equipo == "1":
                        input_valido_equipos = False
                        piloto = entidades.Tareos(nom_nuevo_usuario)
                    elif equipo == "2":
                        input_valido_equipos = False
                        piloto = entidades.Hibridos(nom_nuevo_usuario)
                    elif equipo == "3":
                        input_valido_equipos = False
                        piloto = entidades.Docencios(nom_nuevo_usuario)
                    else:
                        print(self.equivocacion_usuario)
                input_valido_vehiculos = True
                piloto.guardar_piloto(diccionario_ordenado_pil)
                while input_valido_vehiculos:
                    print()
                    lista_op = ["1", "2", "3", "4"]
                    vehiculo_inicial = input("Seleccione un vehículo: \n"
                                             "[1] Automovil \n"
                                             "[2] Troncomovil \n"
                                             "[3] Bicicleta \n"
                                             "[4] Motocicleta \n" 
                                             "Opciones (1,2,3,4): ").strip()
                    if vehiculo_inicial in lista_op:
                        print()
                        nom_nuevo_vehiculo = input("Que nombre desea que tenga su Vehículo: "
                                                   "").strip()
                        if all(caracter.isspace() or caracter.isalnum() for caracter in
                               nom_nuevo_vehiculo) \
                                and nom_nuevo_vehiculo not in lista_nombres_archivo_vehi:
                            if vehiculo_inicial == "1":
                                input_valido_vehiculos = False
                                vehiculo_inicial = entidades.Automovil(nombre=nom_nuevo_vehiculo,
                                                                       dueno=nom_nuevo_usuario)
                            elif vehiculo_inicial == "2":
                                input_valido_vehiculos = False
                                vehiculo_inicial = entidades.Troncomovil(nombre=nom_nuevo_vehiculo,
                                                                         dueno=nom_nuevo_usuario)
                            elif vehiculo_inicial == "3":
                                input_valido_vehiculos = False
                                vehiculo_inicial = entidades.Bicicleta(nombre=nom_nuevo_vehiculo,
                                                                       dueno=nom_nuevo_usuario)
                            elif vehiculo_inicial == "4":
                                input_valido_vehiculos = False
                                vehiculo_inicial = entidades.Motocicleta(nombre=nom_nuevo_vehiculo,
                                                                         dueno=nom_nuevo_usuario)
                        else:
                            print()
                            print(self.equivocacion_usuario)
                    else:
                        print()
                        print(self.equivocacion_usuario)
                vehiculo_inicial.guardar_vehiculo(diccionario_ordenado_vehi)
                self.agregar_vehiculo(vehiculo_inicial)
                self.juego = juego.Juego(piloto, vehiculo_inicial)
                self.juego.agregar_vehiculo(vehiculo_inicial)
            elif nom_nuevo_usuario in lista_nombres_archivo_pil:
                print("Ese nombre de usuario ya existe, elija otro por favor...")
            else:
                print()
                print("Ingrese un nombre de usuario que solo contenga letras números y espacios...")
        self.nombre_usuario = nom_nuevo_usuario
        return self.juego

    def cargar_partida(self):
        lista_archivo_us = []
        with open(os.path.join(self.ruta_pil[1]), "a+", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip().split(",")
                lista_archivo_us.append(linea)
        lista_archivo_us = funciones.buscar_nombre(lista_archivo_us)
        input_valido = True
        while input_valido:
            print()
            nom_usuario_cargar = input("[1] Ingrese su Nombre de Usuario: \n"
                                       "[2] Volver \n"
                                       "Opciones (1,2): ").strip()
            if nom_usuario_cargar == "1" and (nom_usuario_cargar in lista_archivo_us):
                input_valido = False
                self.nombre_usuario = nom_usuario_cargar
                # Falta cargar bien
                print()
                print("Iniciando sesión.....")
                print()
                MenuPrincipal(self.juego).ingresar_input()
            elif nom_usuario_cargar == "2":
                input_valido = False
                self.ingresar_input()
            else:
                print()
                print("Ingrese un nombre usuario válido por favor...")


class MenuPrincipal(Menu):
    def __init__(self, juego):
        super().__init__()
        self.no_ingresa_input_valido = True
        self.juego = juego

    def ingresar_input(self):
        while self.no_ingresa_input_valido:
            print()
            print("----- Menú Principal ----- \n"
                  "\n"
                  "Qué desea hacer?: ")
            opciones = input("[1] Comprar vehículo \n"
                             "[2] Iniciar carrera \n"
                             "[3] Guardar partida \n"
                             "[4] Salir del juego \n"
                             "Opciones(1,2,3,4): ").strip()
            if opciones == "1":
                self.no_ingresa_input_valido = False
                return "comprar_vehiculo"
            elif opciones == "2":
                self.no_ingresa_input_valido = False
                return "iniciar_carrera"
            elif opciones == "3":
                self.no_ingresa_input_valido = False
                return "guardar_partida"
            elif opciones == "4":
                self.salir_del_juego()
            else:
                print(self.equivocacion_usuario)
        self.no_ingresa_input_valido = True

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def iniciar_carrera(self):
        carrera = menus_2.Carrera()
        sys.exit()

    def salir_del_juego(self):
        seguro = input("Estas seguro que deseas salir del juego?: \n"
                       "[1] SI \n"
                       "[2] NO ").strip()
        if seguro == "1":
            print("..........")
            print("Saliendo del juego...")
            print("..........")
            sys.exit()


class CompraDeVehiculos(Menu):
    def __init__(self, juego):
        super().__init__()
        self.juego = juego

    def ingresar_input(self):
        precio_auto = 400
        precio_tronco = 300
        precio_moto = 250
        precio_bici = 200
        while self.no_ingresa_input_valido:
            print()
            print(f"Dinero actual: ${self.juego.jugador.dinero}")
            print("Vehículos disponibles para comprar:")
            print("----------*----------")
            print(f"[1] Automóvil    {precio_auto} \n"
                  f"[2] Troncomóvil  {precio_tronco} \n"
                  f"[3] Motocicleta  {precio_moto} \n"
                  f"[4] Bicicleta    {precio_bici} \n"
                  f"----------*----------")
            opciones = input("Ingrese el número del vehículo que desea comprar "
                             "(ingrese 0 para regresar): ").strip()
            input_no_valido = True
            while input_no_valido:
                opcion = funciones.condiciones_compra_vehiculo(opciones, self.juego)
                if opcion == "1":
                    input_no_valido = False
                    self.comprar_vehiculo(opciones)
                    self.no_ingresa_input_valido = False
                    print("Compra realizada con éxito...")
                elif opcion == "0":
                    self.no_ingresa_input_valido = False
                    input_no_valido = False
                elif opcion == "2":
                    input_no_valido = False
        return self.juego

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def comprar_vehiculo(self, opcion):
        lista_archivo_vehiculos = []
        with open(os.path.join(parametros.PATHS["VEHICULOS"]), "a+", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip().split(",")
                lista_archivo_vehiculos.append(linea)
        lista_archivo_vehiculos = funciones.buscar_nombre(lista_archivo_vehiculos)
        self.no_ingresa_input_valido = True
        while self.no_ingresa_input_valido:
            nombre_vehiculo = input("Nombre del Vehículo: ").strip()
            if nombre_vehiculo not in lista_archivo_vehiculos:
                self.no_ingresa_input_valido = False
                if opcion == "1":
                    nuevo_vehiculo = entidades.Automovil(nombre=nombre_vehiculo,
                                                         dueno=juego.jugador)
                elif opcion == "2":
                    nuevo_vehiculo = entidades.Troncomovil(nombre=nombre_vehiculo,
                                                           dueno=juego.jugador)
                elif opcion == "3":
                    nuevo_vehiculo = entidades.Motocicleta(nombre=nombre_vehiculo,
                                                           dueno=juego.jugador)
                elif opcion == "4":
                    nuevo_vehiculo = entidades.Bicicleta(nombre=nombre_vehiculo,
                                                         dueno=juego.jugador)
            else:
                print(self.no_ingresa_input_valido)
        self.agregar_vehiculo(nuevo_vehiculo)
        self.juego.agregar_vehiculo(nuevo_vehiculo)
