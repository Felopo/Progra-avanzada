# Código servidor de Enzo
import random
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9002

# Dejamos el socket esperando ("escuchando") por conexiones
sock.bind((host, port))
sock.listen()

# Aqui aceptamos la conexión de EnZurg
socket_cliente, address = sock.accept()


MENSAJES_SPAM = [
    "SPAM!! SPAM!! SPAM!! SPAM!! SPAM!!",
    "lalalalalalalalalalalalala",
    "Intentando sobrecargar el cliente de EnZurg",
    "La respuesta a la Vida, el Universo, y Todo lo Demás es... 42",
]

# COMPLETAR AQUI
# Cada 5 segundos debes enviar un mensaje
# de la lista MENSAJES_SPAM a EnZurg
while True:
    mensaje = random.choice(MENSAJES_SPAM)
    mensaje_a_enviar = mensaje.encode("utf-8")
    socket_cliente.sendall(mensaje_a_enviar)
    time.sleep(5)