from PyQt5.QtCore import QObject, pyqtSignal, QRect
from parametros_generales import (PATHS_PERSONAJE, N, VEL_MOVIMIENTO,
                                  POSICION_VENTANA_JUEGO, MONEDAS_INICIALES, DINERO_TRAMPA)
from parametros_precios import PRECIO_AZADA, PRECIO_HACHA, PRECIO_SEMILLA_ALCACHOFAS, \
    PRECIO_SEMILLA_CHOCLOS


class Personaje(QObject):

    mover_personaje_senal = pyqtSignal(str)
    senal_compra = pyqtSignal(str)
    senal_dinero_trampa = pyqtSignal()

    def __init__(self, x, y, largo, ancho, rocas, pasto):
        super().__init__()
        self._x = x
        self._y = y
        self.largo = largo
        self.ancho = ancho
        self.posiciones_rocas = rocas
        for i in range(len(pasto)):
            pasto[i] = pasto[i].reverse()
        self._posicion_pastos = pasto
        self.direccion = "D"
        self.avanzar_rocas = [True, True, True, True]
        self.posicion_personaje = None
        self.actualizar_senal_ventana = None
        self.senal_dinero = None
        self.senal_dinero_actualizado = None
        self.senal_dinero_actualizado_lateral = None
        self.senal_agregar_objeto_inventario = None
        self.mover_personaje_senal.connect(self.mover)
        self.azada = False
        self.hacha = False
        self._dinero = MONEDAS_INICIALES
        self.inventario = []
        self.items_inventario = 0

    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, valor):
        if valor <= 0:
            self._dinero = 0
        else:
            self._dinero -= valor

    def agregar_objeto(self, nombre_objeto):
        if nombre_objeto == "azada":
            self._dinero -= PRECIO_AZADA
            self.azada = True
            self.inventario.append("azada")
            self.items_inventario += 1
        elif nombre_objeto == "hacha":
            self._dinero -= PRECIO_HACHA
            self.hacha = True
            self.inventario.append("hacha")
            self.items_inventario += 1
        elif nombre_objeto == "semillas_choclo":
            self._dinero -= PRECIO_SEMILLA_CHOCLOS
            self.inventario.append("semillas_choclo")
            self.items_inventario += 1
        elif nombre_objeto == "semillas_alcachofa":
            self._dinero -= PRECIO_SEMILLA_ALCACHOFAS
            self.inventario.append("semillas_alcachofa")
            self.items_inventario += 1
        self.senal_dinero_actualizado.emit(self.dinero)
        self.senal_dinero_actualizado_lateral.emit(self.dinero)
        self.senal_agregar_objeto_inventario.emit(nombre_objeto, self.items_inventario)

    def dinero_trampa(self):
        self._dinero += DINERO_TRAMPA
        self.senal_dinero_actualizado.emit(self.dinero)
        self.senal_dinero_actualizado_lateral.emit(self.dinero)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        if 0 <= valor < self.largo - 1:
            self._y = valor
            self.actualizar_ventana_personaje()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if 0 <= valor < self.ancho - 1:
            self._x = valor
            self.actualizar_ventana_personaje()

    def actualizar_ventana_personaje(self):
        if self.actualizar_senal_ventana:
            self.actualizar_senal_ventana.emit({"x": self.x,
                                                "y": self.y,
                                                "direccion": self.direccion,
                                                })

    def posicion_rocas(self, valor):
        self.posicion_personaje = QRect(int(self._x), int(self._y), N, N)
        valor[0] = int(valor[0])
        valor[1] = int(valor[1])
        if valor[0:2] in self.posiciones_rocas:
            self.posicion_roca = QRect(valor[0], valor[1], N, N)
            if self.posicion_personaje.intersects(self.posicion_roca):
                if valor[2] == "R":
                    self.avanzar_rocas[0] = False
                elif valor[2] == "D":
                    self.avanzar_rocas[1] = False
                elif valor[2] == "L":
                    self.avanzar_rocas[2] = False
                elif valor[2] == "U":
                    self.avanzar_rocas[3] = False
        else:
            self.avanzar_rocas = [True, True, True, True]

    def mover(self, direccion):
        if direccion == "R":
            self.posicion_rocas([self.y + 1, self.x + 1, "R"])
            self.direccion = "R"
            if self.avanzar_rocas[0]:
                self.x += VEL_MOVIMIENTO
            else:
                self.x = self.x
        elif direccion == "D":
            self.posicion_rocas([self.y + 1.1, self.x, "D"])
            self.direccion = "D"
            if self.avanzar_rocas[1]:
                self.y += VEL_MOVIMIENTO
            else:
                self.y = self.y
        elif direccion == "L":
            self.posicion_rocas([self.y + 1, self.x - 0.1, "L"])
            self.direccion = "L"
            if self.avanzar_rocas[2]:
                self.x -= VEL_MOVIMIENTO
            else:
                self.x = self.x
        elif direccion == "U":
            self.posicion_rocas([self.y, self.x, "U"])
            self.direccion = "U"
            if self.avanzar_rocas[3]:
                self.y -= VEL_MOVIMIENTO
            else:
                self.y = self.y
