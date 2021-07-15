# Código cliente de EnZurg
import socket


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
        sock.sendall(mensaje.encode("utf-8"))
        # Recibo la respuesta que me envíe
        data = sock.recv(4096)
        print("Enzo a mi:", data.decode("utf-8"))
except ConnectionError as e:
    print("Ocurrió un error.")
finally:
    sock.close()