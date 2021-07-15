# Código cliente de EnZurg
import socket


def codificar(contenido):
    contenido_como_bytes = contenido.encode("utf-8")
    largo = len(contenido_como_bytes)
    largo_como_bytes = largo.to_bytes(4, byteorder="little")
    bloques = bytearray(largo_como_bytes)
    contador = 0
    for i in range(0, len(contenido_como_bytes), 80):
        posicion_como_bytes = contador.to_bytes(4, byteorder="big")
        chunk = contenido_como_bytes[i:i+80]
        chunk_como_bytes = bytes(chunk)
        bloques.extend(posicion_como_bytes)
        bloques.extend(chunk_como_bytes)
        contador += 1
    return bloques

# Creo un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así puedo obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9001

# Me conecto al socket del servidor de Enzo
sock.connect((host, port))

try:
    while True:
        # Escribo el mensaje a enviarle a Enzo
        mensaje = input("Yo a Enzo: ")
        # Si escribo "salir", se corta la conexión
        if mensaje.lower() == "salir":
            sock.sendall("salir".encode("utf-8"))
            break
        # Envio mi mensaje al servidor
        bytes_mensaje = codificar(mensaje)
        sock.sendall(bytes_mensaje)
        # Recibo la respuesta que me envíe
        data = sock.recv(4096)
        print("Mensaje recivido: ", data)
except ConnectionError as e:
    print("Ocurrió un error.")
finally:
    sock.close()