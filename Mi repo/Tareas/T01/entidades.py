import parametros
from random import randint
import os.path


class Vehiculo:
    def __init__(self, nombre, dueno, CHASIS=None, CARROCERIA=None, RUEDAS=None, MOTOR=None,
                 ZAPATILLAS=None, PESO=None):
        self.dueno = dueno
        self.nombre = nombre
        self.categoria = None
        self._chasis = randint(CHASIS["MIN"], CHASIS["MAX"])
        self._carroceria = randint(CARROCERIA["MIN"], CARROCERIA["MAX"])
        self._ruedas = randint(RUEDAS["MIN"], RUEDAS["MAX"])
        self._motor = randint(MOTOR["MIN"], MOTOR["MAX"])
        self._zapatillas = randint(ZAPATILLAS["MIN"], ZAPATILLAS["MAX"])
        self.peso = randint(PESO["MIN"], PESO["MAX"])

    def guardar_vehiculo(self, diccionario_orden):
        lista_orden = []
        for i in range(len(diccionario_orden)):
            if diccionario_orden["Nombre"] == i:
                lista_orden.append(self.nombre)
            elif diccionario_orden["Dueño"] == i:
                lista_orden.append(self.dueno)
            elif diccionario_orden["Categoría"] == i:
                lista_orden.append(self.categoria)
            elif diccionario_orden["Chasis"] == i:
                lista_orden.append(self._chasis)
            elif diccionario_orden["Carrocería"] == i:
                lista_orden.append(self._carroceria)
            elif diccionario_orden["Ruedas"] == i:
                lista_orden.append(self._ruedas)
            elif diccionario_orden["Motor o Zapatillas"] == i:
                if self.categoria == "automovil" or self.categoria == "motocicleta":
                    lista_orden.append(self._motor)
                elif self.categoria == "troncomovil" or self.categoria == "bicicleta":
                    lista_orden.append(self._zapatillas)
            elif diccionario_orden["Peso"]:
                lista_orden.append(self.peso)
        lista_orden = map(lambda x: str(x), lista_orden)
        string_datos_vehiculo = ",".join(lista_orden)
        path = parametros.PATHS["VEHICULOS"]
        with open(os.path.join(path[1]), "a+") as archivo:
            archivo.write(string_datos_vehiculo + "\n")

    @property
    def mejorar_pieza(self):
        return self

    @mejorar_pieza.setter
    def mejorar_pieza(self, lista_pieza_jugador):
        print()
        if lista_pieza_jugador[0] == "chasis":
            if lista_pieza_jugador[1].dinero >= parametros.MEJORAS["CHASIS"]["COSTO"]:
                self._chasis += parametros.MEJORAS["CHASIS"]["EFECTO"]
                print("Mejora realizada...")
            else:
                print("No cuentas con el dinero necesario para realizar esta mejora...")
        elif lista_pieza_jugador[0] == "carrocería":
            if lista_pieza_jugador[1].dinero >= parametros.MEJORAS["CARROCERIA"]["COSTO"]:
                self._carroceria += parametros.MEJORAS["CARROCERIA"]["EFECTO"]
                print("Mejora realizada...")
            else:
                print("No cuentas con el dinero necesario para realizar esta mejora...")
        elif lista_pieza_jugador[0] == "ruedas":
            if lista_pieza_jugador[1].dinero >= parametros.MEJORAS["RUEDAS"]["COSTO"]:
                self._ruedas += parametros.MEJORAS["RUEDAS"]["EFECTO"]
                print("Mejora realizada...")
            else:
                print("No cuentas con el dinero necesario para realizar esta mejora...")
        elif lista_pieza_jugador[0] == "motor":
            if lista_pieza_jugador[1].dinero >= parametros.MEJORAS["MOTOR"]["COSTO"]:
                self._motor += parametros.MEJORAS["MOTOR"]["EFECTO"]
                print("Mejora realizada...")
            else:
                print("No cuentas con el dinero necesario para realizar esta mejora...")
        elif lista_pieza_jugador[0] == "zapatillas":
            if lista_pieza_jugador[1].dinero >= parametros.MEJORAS["ZAPATILLAS"]["COSTO"]:
                self._zapatillas += parametros.MEJORAS["ZAPATILLAS"]["EFECTO"]
                print("Mejora realizada...")
            else:
                print("No cuentas con el dinero necesario para realizar esta mejora...")
        print()


class Automovil(Vehiculo):
    def __init__(self, nombre, dueno):
        super().__init__(nombre, dueno, **parametros.AUTOMOVIL)
        self.num_ruedas = 4
        self.categoria = "automovil"


class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueno):
        super().__init__(nombre, dueno, **parametros.TRONCOMOVIL)
        self.num_ruedas = 4
        self.categoria = "troncomovil"


class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueno):
        super().__init__(nombre, dueno, **parametros.BICICLETA)
        self.num_ruedas = 2
        self.categoria = "bicicleta"


class Motocicleta(Vehiculo):
    def __init__(self, nombre, dueno):
        super().__init__(nombre, dueno, **parametros.MOTOCICLETA)
        self.num_ruedas = 2
        self.categoria = "motocicleta"


class Pistas:
    def __init__(self, nombre, tipo, hielo, rocas, dificultad, num_vueltas, contrincantes, l_pista):
        self.nombre = nombre
        self.tipo = tipo
        self.hielo = hielo
        self.rocas = rocas
        self.dificultad = dificultad
        self.numero_vueltas = num_vueltas
        self.contrincantes = contrincantes
        self.largo_pista = l_pista


class PistaHielo(Pistas):
    def __init__(self, nombre, tipo, hielo, rocas, dificultad, num_vueltas, contrincantes, l_pista):
        super().__init__(nombre, tipo, hielo, rocas, dificultad, num_vueltas, contrincantes,
                         l_pista)


class PistaRoca(Pistas):
    def __init__(self, nombre, tipo, hielo, rocas, dificultad, num_vueltas, contrincantes, l_pista):
        super().__init__(nombre, tipo, hielo, rocas, dificultad, num_vueltas, contrincantes,
                         l_pista)


class PistaSuprema(PistaHielo, PistaRoca):
    def __init__(self, nombre, tipo, hielo, rocas, dificultad, num_vueltas, contrincantes, l_pista):
        super().__init__(nombre, tipo, hielo, rocas, dificultad, num_vueltas, contrincantes,
                         l_pista)


class Piloto:
    def __init__(self, nombre, CONTEXTURA=None, EQUILIBRIO=None,
                 PERSONALIDAD=None):
        self.contextura = randint(CONTEXTURA["MIN"], CONTEXTURA["MAX"])
        self.equilibrio = randint(EQUILIBRIO["MIN"], EQUILIBRIO["MAX"])
        self.personalidad = PERSONALIDAD
        self.nombre = nombre
        self.dinero = 0
        self.experiencia = 0
        self.tiempo = None
        self.equipo = None

    def guardar_piloto(self, diccionario_orden):
        lista_orden = []
        for i in range(len(diccionario_orden)):
            if diccionario_orden["Nombre"] == i:
                lista_orden.append(self.nombre)
            elif diccionario_orden["Dinero"] == i:
                lista_orden.append(self.dinero)
            elif diccionario_orden["Personalidad"] == i:
                lista_orden.append(self.personalidad)
            elif diccionario_orden["Contextura"] == i:
                lista_orden.append(self.contextura)
            elif diccionario_orden["Equilibrio"] == i:
                lista_orden.append(self.equilibrio)
            elif diccionario_orden["Experiencia"] == i:
                lista_orden.append(self.experiencia)
            elif diccionario_orden["Equipo"] == i:
                lista_orden.append(self.equipo)
        lista_orden = map(lambda x: str(x), lista_orden)
        string_datos_piloto = ",".join(lista_orden)
        path = parametros.PATHS["PILOTOS"]
        with open(os.path.join(path[1]), "a+") as archivo:
            archivo.write(string_datos_piloto + "\n")


class Tareos(Piloto):
    def __init__(self, nombre):
        super().__init__(nombre, **parametros.EQUIPOS["TAREOS"])
        self.equipo = "Tareos"


class Hibridos(Piloto):
    def __init__(self, nombre):
        super().__init__(nombre, **parametros.EQUIPOS["HIBRIDOS"])
        self.equipo = "Hibridos"


class Docencios(Piloto):
    def __init__(self, nombre):
        super().__init__(nombre, **parametros.EQUIPOS["DOCENCIOS"])
        self.equipo = "Docencios"

