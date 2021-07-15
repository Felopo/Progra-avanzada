import socket
import json
import pickle
from juego import Juego


class Servidor:

    def __init__(self):
        '''Inicializador de servidor.

        Crea socket de servidor, lo vincula a un puerto.'''
        self.host = socket.gethostname()
        self.port = 12345
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen(0)
        print("Servidor iniciado.")
        self.juego = None  # Juego comienza nulo.
        self.socket_cliente = None  # Aún no hay cliente.

    def esperar_conexion(self):
        '''Espera a la conectarse con un cliente y obtiene su socket.'''
        print("Esperando cliente...")
        self.socket_cliente, (self.host_cliente, self.port_cliente) = self.socket_servidor.accept()
        print("¡Servidor conectado a cliente!")
        self.interactuar_con_cliente()

    def interactuar_con_cliente(self):
        '''Comienza ciclo de interacción con cliente.

        Recibe un acción y responde apropiadamente.'''
        self.enviar_estado('', True)
        while self.socket_cliente:
            accion = self.recibir_accion()
            self.manejar_accion(accion)

    def enviar_estado(self, mensaje, continuar):
        '''Envia estado del juego en el servidor.'''
        if continuar:
            if self.juego is not None:
                mensaje = f'{self.juego.tablero_string()}\n{mensaje}\n'
            acciones = ("¿Qué deseas hacer?\n"
                        "Para jugar nuevo juego: \\juego_nuevo\n"
                        "Para jugar en una columna: \\jugada columna\n"
                        "Para salir: \\salir\n")
            mensaje = mensaje + "\n" + acciones
        if continuar:
            continuar = "True"
        else:
            continuar = "Fals"
        mensaje_a_enviar = continuar + mensaje
        mensaje_a_enviar = mensaje_a_enviar.encode()
        self.socket_cliente.sendall(len(mensaje_a_enviar).to_bytes(4, byteorder="big"))
        self.socket_cliente.sendall(mensaje_a_enviar)

    def recibir_accion(self):
        '''Recibe mensaje desde el cliente y lo decodifica.'''
        largo_datos = int.from_bytes(self.socket_cliente.recv(4), byteorder="big")
        accion = bytearray()
        while len(accion) < largo_datos:
            bytes_a_ver = min(4086, largo_datos - len(accion))
            bytes_recibidos = self.socket_cliente.recv(bytes_a_ver)
            accion.extend(bytes_recibidos)
        accion = accion.decode("utf-8")
        return accion

    def manejar_accion(self, accion):
        '''Maneja la acción recibida del cliente.'''
        print(f'Acción recibida: {accion}')
        if accion == "juego_nuevo":
            tipo = "\\juego_nuevo"
        elif accion == "salir":
            tipo = "\\salir"
        else:
            tipo = None
        try:
            if accion[0:6] == "jugada":
                if int(accion[7]) in range(0, 7):
                    tipo = "\\jugada"
        except IndexError:
            tipo = None
        if tipo == '\\juego_nuevo':
            self.juego = Juego()
            self.juego.crear_tablero()
            self.enviar_estado('', True)
        elif tipo == '\\salir':
            self.enviar_estado('¡Adios!', False)
            self.juego = None
            self.socket_cliente.close()
            print('Cliente desconectado.\n')
            self.socket_cliente = None
        elif tipo == '\\jugada':
            if self.juego is None:
                self.enviar_estado('Ningún juego ha iniciado.', True)
            else:
                jugada = int(accion[7])
                if not self.juego.es_jugada_valida(jugada):
                    self.enviar_estado('Jugada inválida.', True)
                else:
                    gano = self.juego.turno_jugador(jugada)
                    if gano:
                        self.enviar_estado('¡Ganaste! Se acabó el juego.', True)
                        self.juego = None
                    else:
                        perdio = self.juego.turno_cpu()
                        if perdio or self.juego.empate():
                            self.enviar_estado('No ganaste :( Se acabó el juego.', True)
                            self.juego = None
                        else:
                            self.enviar_estado('', True)


if __name__ == "__main__":
    servidor = Servidor()
    while True:
        try:
            servidor.esperar_conexion()
        except KeyboardInterrupt:
            print("\nServidor interrumpido")
            break
