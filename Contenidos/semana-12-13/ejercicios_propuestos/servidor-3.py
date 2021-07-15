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
    print(f"Mensaje recibido: {datos_recibidos}")
    string_a_enviar = input("Yo a Enzorg: ")
    bytes_a_enviar = codificar(string_a_enviar)
    socket_cliente.sendall(bytes_a_enviar)
socket_cliente.close()
sock.close()


