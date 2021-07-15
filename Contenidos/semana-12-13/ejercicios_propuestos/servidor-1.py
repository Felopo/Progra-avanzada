import random
import socket


def deformador_string(string):
    string_deformado = ""
    for caracter in string:
        if random.random() <= 0.5:
            string_deformado += caracter.upper()
        else:
            string_deformado += caracter.lower()
    return string_deformado


# Así podemos obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9001

# Dejamos el socket esperando ("escuchando") por conexiones
print(f"El host es: {host}")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()
socket_cliente, address = sock.accept()
while True:
    datos_recibidos = socket_cliente.recv(4098)
    if not datos_recibidos:
        break
    string_a_enviar = deformador_string(datos_recibidos.decode("utf-8"))
    bytes_a_enviar = string_a_enviar.encode("utf-8")
    socket_cliente.sendall(bytes_a_enviar)
    print(f"Mensaje enviado: {bytes_a_enviar}")
socket_cliente.close()
sock.close()