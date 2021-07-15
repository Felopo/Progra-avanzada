from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
import sys


"""
Debes completar la clase VentanaJuego con los elementos que
estimes necesarios.

Eres libre de agregar otras clases si lo crees conveniente.
"""


class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.

    Recuerda que eviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que 
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE 
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.se_clickeo = False
        self.init_gui()

    def init_gui(self):
        self.vbox = QVBoxLayout()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("DCColgado 51")
        self.etiqueta_imagen = QLabel(self)
        self.etiqueta_imagen.setGeometry(280, 50, 200, 200)
        self.ruta_imagen = QLabel(self)
        self.mensaje = QLabel(self)
        self.usadas = QLabel(self)
        self.disponibles = QLabel(self)
        self.palabra = QLabel(self)
        self.sel_letra = QPushButton("Seleccionar letra", self)
        self.sel_letra.resize(self.sel_letra.sizeHint())
        self.sel_letra.clicked.connect(self.boton_clickeado_1)
        self.nuevo_juego = QPushButton("Nuevo juego", self)
        self.nuevo_juego.resize(self.nuevo_juego.sizeHint())
        self.nuevo_juego.clicked.connect(self.boton_clickeado_2)
        self.vbox.addWidget(self.palabra)
        self.vbox.addWidget(self.etiqueta_imagen)
        self.vbox.addWidget(self.usadas)
        self.vbox.addWidget(self.disponibles)
        self.vbox.addWidget(self.mensaje)
        self.vbox.addWidget(self.sel_letra)
        self.vbox.addWidget(self.nuevo_juego)
        self.setLayout(self.vbox)

    def recibir_senal(self, diccionario):
        self.diccionario = diccionario
        self.ruta_imagen = self.diccionario["imagen"]
        pixeles = QPixmap(self.ruta_imagen)
        self.etiqueta_imagen.setPixmap(pixeles)
        self.etiqueta_imagen.setScaledContents(True)
        self.mensaje.setText(self.diccionario["msg"])
        self.usadas.setText("USADAS: " + self.diccionario["usadas"])
        self.disponibles.setText("DISPONIBLES: " + self.diccionario["disponibles"])
        self.palabra.setText(self.diccionario["palabra"])

    def boton_clickeado_1(self):
        self.se_clickeo = True
        self.sel_letra.setText("Presione tecla")

    def boton_clickeado_2(self):
        self.reiniciar_signal.emit()

    def keyPressEvent(self, event):
        self.sel_letra.setText("Seleccionar letra")
        if self.se_clickeo:
            self.se_clickeo = False
            letra = event.text()
            dic_letra = {"letra": letra}
            self.enviar_letra_signal.emit(dic_letra)


