from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import (QPixmap, QIcon)
from parametros_generales import (N, PATHS, PATHS_CHOCLO, PATHS_ALCACHOFA, PATHS_RECURSOS,
                                  PATHS_OTROS, POSICION_VENTANA_JUEGO)


class VentanaInicio(QWidget):

    senal_actualizar = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.personaje = None
        self.senal_actualizar.connect(self.actualizar_resultado)
        self.senal_procesar = None
        self.mapa_valido = False
        self.datos_mapa = None
        self.init_gui()

    def init_gui(self):
        self.setGeometry(500, 100, 900, 600)
        self.setWindowTitle("DCCampo")
        self.setWindowIcon(QIcon(PATHS["logo"]))
        # Imagen fondo
        self.imagen_fondo = QLabel(self)
        self.imagen_fondo.setGeometry(0, 0, 900, 600)
        self.ruta_imagen_fondo = PATHS["imagen_fondo"]
        pixeles_imagen_fondo = QPixmap(self.ruta_imagen_fondo)
        self.imagen_fondo.setPixmap(pixeles_imagen_fondo)
        self.imagen_fondo.setScaledContents(True)
        #   Imagen
        self.etiqueta_imagen = QLabel(self)
        self.ruta_imagen = PATHS["logo"]
        pixeles = QPixmap(self.ruta_imagen)
        self.etiqueta_imagen.setPixmap(pixeles)
        self.etiqueta_imagen.setScaledContents(True)
        #   Etiqueta
        self.etiqueta = QLabel("Ingresa el nombre del mapa a cargar:", self)
        #   Cuadro de texto
        self.ingrese_datos = QLineEdit("", self)
        self.ingrese_datos.setGeometry(45, 15, 100, 20)
        # Etiqueta error
        self.etiqueta_error = QLabel("", self)
        # Botón Jugar
        self.boton_jugar = QPushButton("&Jugar", self)
        self.boton_jugar.resize(self.boton_jugar.sizeHint())
        self.boton_jugar.clicked.connect(self.boton_clickeado)
        # Agregar los Layouts a la ventana
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

    def entregar_mapa(self):
        return self.datos_mapa
