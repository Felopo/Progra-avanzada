from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from parametros_generales import PATHS_OTROS, PATHS, PATHS_CHOCLO
from parametros_precios import PRECIO_AZADA, PRECIO_HACHA, PRECIO_SEMILLA_ALCACHOFAS, \
    PRECIO_SEMILLA_CHOCLOS, PRECIO_TICKET
import sys
import os

nombre_ventana, clase = uic.loadUiType(os.path.join("interfaces", "ventana_tienda.ui"))


class VentanaTienda(nombre_ventana, clase):

    senal_dinero = pyqtSignal(int)
    senal_dinero_actualizado = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(450, 330)
        self.setWindowTitle("Tienda")
        self.setWindowIcon(QIcon(PATHS["logo"]))
        self.boton_comprar_azada.clicked.connect(self.comprar_azada)
        self.boton_comprar_hacha.clicked.connect(self.comprar_hacha)
        self.boton_comprar_s_choclo.clicked.connect(self.comprar_s_choclo)
        self.boton_comprar_s_alcachofa.clicked.connect(self.comprar_s_alcachofa)
        self.boton_ticket.clicked.connect(self.comprar_ticket)
        self.ganador = Ganar()
        self.senal_ganar = self.ganador.senal_ganar
        self.ganador.senal_ganar.connect(self.ganador.ganar)
        self.senal_compra = None

    def comprable_inicial(self, jugador_dinero):
        if jugador_dinero < PRECIO_TICKET:
            self.boton_ticket.setEnabled(False)
        else:
            self.boton_ticket.setEnabled(True)
        if jugador_dinero < PRECIO_HACHA:
            self.boton_comprar_hacha.setEnabled(False)
        else:
            self.boton_comprar_hacha.setEnabled(True)
        if jugador_dinero < PRECIO_AZADA:
            self.boton_comprar_azada.setEnabled(False)
        else:
            self.boton_comprar_azada.setEnabled(True)
        if jugador_dinero < PRECIO_SEMILLA_CHOCLOS:
            self.boton_comprar_s_choclo.setEnabled(False)
        else:
            self.boton_comprar_s_choclo.setEnabled(True)
        if jugador_dinero < PRECIO_SEMILLA_ALCACHOFAS:
            self.boton_comprar_s_alcachofa.setEnabled(False)
        else:
            self.boton_comprar_s_alcachofa.setEnabled(True)

    def comprable(self, jugador_dinero):
        if jugador_dinero < PRECIO_TICKET:
            self.boton_ticket.setEnabled(False)
        else:
            self.boton_ticket.setEnabled(True)
        if jugador_dinero < PRECIO_HACHA:
            self.boton_comprar_hacha.setEnabled(False)
        else:
            self.boton_comprar_hacha.setEnabled(True)
        if jugador_dinero < PRECIO_AZADA:
            self.boton_comprar_azada.setEnabled(False)
        else:
            self.boton_comprar_azada.setEnabled(True)
        if jugador_dinero < PRECIO_SEMILLA_CHOCLOS:
            self.boton_comprar_s_choclo.setEnabled(False)
        else:
            self.boton_comprar_s_choclo.setEnabled(True)
        if jugador_dinero < PRECIO_SEMILLA_ALCACHOFAS:
            self.boton_comprar_s_alcachofa.setEnabled(False)
        else:
            self.boton_comprar_s_alcachofa.setEnabled(True)

    def comprar_azada(self):
        self.senal_compra.emit("azada")

    def comprar_hacha(self):
        self.senal_compra.emit("hacha")

    def comprar_s_choclo(self):
        self.senal_compra.emit("semillas_choclo")

    def comprar_s_alcachofa(self):
        self.senal_compra.emit("semillas_alcachofa")

    def comprar_ticket(self):
        self.senal_ganar.emit()

    def abrir_ventana(self):
        self.show()


class Ganar(QWidget):

    senal_ganar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(500, 500, 500, 300)
        self.ganaste = QPushButton("HAS GANADO :D,\n"
                                   "Presione para salir", self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.ganaste)
        self.setLayout(vbox)
        self.ganaste.clicked.connect(self.cerrar_juego)

    def ganar(self):
        self.show()

    def cerrar_juego(self):
        sys.exit()
