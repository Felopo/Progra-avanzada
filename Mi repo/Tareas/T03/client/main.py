import socket
from PyQt5.QtWidgets import QApplication
import sys
from frontend import VentanaInicio
import threading
import json


class Client:
    def __init__(self, host, port):
        print("Creando cliente...")
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    ventana_inicio = VentanaInicio()
    with open("parametros.json", "rb") as archivo:
        parametros = json.load(archivo)
        host = parametros["host"]
        port = parametros["port"]
    client = Client(host, port)
    sys.exit(app.exec_())