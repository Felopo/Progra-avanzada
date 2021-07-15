import socket
import threading
import json


class Server:
    def __init__(self, host, port):
        print("Creando servidor...")
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == "__main__":
    with open("parametros.json", "rb") as archivo:
        parametros = json.load(archivo)
        host = parametros["host"]
        port = parametros["port"]
    server = Server(host, port)