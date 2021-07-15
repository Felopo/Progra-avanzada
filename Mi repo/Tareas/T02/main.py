import ventana_juego
import ventana_inicio
import sys
from PyQt5.QtWidgets import QApplication
from revisar_inputs import Revisar
from crear_mapa import CreadorMapa


def hook(type, value, traceback):
    print(type)
    print(traceback)


sys.__excepthook__ = hook
app = QApplication([])
# Ventana Inicio
ventana_inicio = ventana_inicio.VentanaInicio()
revisar_input = Revisar()
crear_mapa = CreadorMapa()
# Ventana Juego
ventana_juego = ventana_juego.VentanaJuego()
revisar_input.senal_actualizar = ventana_inicio.senal_actualizar
ventana_inicio.senal_procesar = revisar_input.senal_procesar
ventana_inicio.senal_mapa = crear_mapa.senal_mapa
crear_mapa.senal_mapa_enviar_datos_mapa.connect(ventana_juego.datos_recibidos)
ventana_inicio.show()
sys.exit(app.exec_())
