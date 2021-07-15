import socket
import json
import pickle


class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        self.host = socket.gethostname()
        self.port = 12345
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        largo_datos = int.from_bytes(self.socket_cliente.recv(4), byteorder="big")
        mensaje = bytearray()
        while len(mensaje) < largo_datos:
            bytes_a_ver = min(4086, largo_datos - len(mensaje))
            datos = self.socket_cliente.recv(bytes_a_ver)
            mensaje.extend(datos)
        continuar = mensaje[0:4].decode("utf-8")
        if continuar == "True":
            continuar = True
        elif continuar == "Fals":
            continuar = False
        mensaje = mensaje[4:].decode("utf-8")
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('Ingrese un comando: ')
        print("--------*--------")
        input_usuario = input_usuario + "\n"
        if input_usuario == "\\juego_nuevo\n":
            return "juego_nuevo"
        elif input_usuario == "\\salir\n":
            return "salir"
        try:
            if input_usuario[8].isnumeric() and int(input_usuario[8]) in range(0, 7) and \
                input_usuario[0:7] == "\\jugada":
                return f"jugada {input_usuario[8]}"
        except IndexError:
            return None
        else:
            return None

    def enviar_accion(self, accion):
        """ Envia accion asociada a comando ya procesado al servidor."""
        mensaje_codificado = accion.encode()
        self.socket_cliente.sendall(len(mensaje_codificado).to_bytes(4, byteorder="big"))
        self.socket_cliente.sendall(mensaje_codificado)

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
