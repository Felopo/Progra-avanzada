# Código cliente de EnZurg
import socket

# Creo un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así puedo obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9002

# Me conecto al socket del servidor de Enzo
sock.connect((host, port))

try:
    while True:
        # Voy a ir recibiendo sus mensajes
        data = sock.recv(4096)
        # Y ahora los voy a ir imprimiendo
        print("Enzo a mi:", data.decode("utf-8"))
except ConnectionError as e:
    print("Ocurrió un error.")
finally:
    sock.close()
