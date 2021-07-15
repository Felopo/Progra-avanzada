from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QMimeData)
from PyQt5.QtGui import (QPixmap, QIcon, QDrag, QPainter)
from client import parametros


class VentanaInicio(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(500, 100, 900, 600)
        self.setWindowTitle("DCClub")
        self.etiqueta_imagen = QLabel(self)
        self.ruta_imagen = parametros["logo"]
        pixeles = QPixmap(self.ruta_imagen)
        self.etiqueta_imagen.setPixmap(pixeles)
        self.etiqueta_imagen.setScaledContents(True)
        self.etiqueta = QLabel("Ingrese un nombre de usuario:", self)
        self.ingrese_datos = QLineEdit("", self)
        self.ingrese_datos.setGeometry(45, 15, 100, 20)
        self.etiqueta_error = QLabel("", self)
        self.boton_jugar = QPushButton("&Iniciar Sesión", self)
        self.boton_jugar.resize(self.boton_jugar.sizeHint())
        self.boton_jugar.clicked.connect(self.boton_clickeado)
        vbox = QVBoxLayout()
        vbox.addStretch(2)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.etiqueta_imagen)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.etiqueta)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.ingrese_datos)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.etiqueta_error)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton_jugar)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(2)
        self.setLayout(vbox)

    def boton_clickeado(self):
        if self.senal_procesar:
            self.senal_procesar.emit(self.ingrese_datos.text())

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.boton_clickeado()

    def actualizar_resultado(self, texto):
        self.datos_mapa = texto
        if self.datos_mapa != "Input no válido":
            self.mapa_valido = True
            self.hide()
            self.senal_mapa.emit(self.datos_mapa)
        else:
            self.etiqueta_error.setText("Ese mapa no existe... ")
            self.ingrese_datos.clear()

