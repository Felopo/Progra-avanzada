from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from parametros_generales import PATHS, MONEDAS_INICIALES
import sys
import os

nombre_ventana, clase = uic.loadUiType(os.path.join("interfaces", "ventana_lateral.ui"))


class VentanaLateral(nombre_ventana, clase):

    senal_dinero_actualizado_lateral = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(PATHS["logo"]))
        self.move(130, 70)
        self.boton_salir.clicked.connect(self.salir_del_juego)
        self.boton_pausa.clicked.connect(self.pausar)
        self.dinero_actual.setText(str(MONEDAS_INICIALES))
        self.show()

    def cambiar_dinero(self, dinero):
        self.dinero_actual.setText(str(dinero))

    def salir_del_juego(self):
        sys.exit()

    def pausar(self):
        self.boton_pausa.setText("Reaundar")
        self.boton_pausa.clicked.connect(self.reanudar)

    def reanudar(self):
        self.boton_pausa.setText("Pausar")
        self.boton_pausa.clicked.connect(self.pausar)
