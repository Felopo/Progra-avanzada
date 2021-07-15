import os
from PyQt5.QtCore import QObject, pyqtSignal


class Revisar(QObject):

    senal_procesar = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.senal_actualizar = None
        self.senal_procesar.connect(self.revisar_input)

    def revisar_input(self, texto):
        texto = texto.strip()
        lista_mapas = os.listdir("mapas")
        if texto + ".txt" in lista_mapas or texto in lista_mapas:
            self.actualizar_interfaz(texto)
        else:
            self.actualizar_interfaz("Input no válido")

    def actualizar_interfaz(self, texto):
        if self.senal_actualizar:
            self.senal_actualizar.emit(texto)
