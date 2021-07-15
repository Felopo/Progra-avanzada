from cargar import cargar_archivos
from os import path


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = []
        # self.seguidores = [] # almacenar a los seguidores es opcional.


class Pintogram:
    def __init__(self):
        self.lista_usuarios = []

    def nuevo_usuario(self, id_usuario, nombre):
        usuario_nuevo = Usuario(id_usuario, nombre)
        self.lista_usuarios.append(usuario_nuevo)

    def follow(self, id_seguidor, id_seguido):
        # Método que permite a un usuario seguir a otro
        for i in range(len(self.lista_usuarios)):
            if self.lista_usuarios[i].id == id_seguidor:
                self.lista_usuarios[i].seguidos.append(id_seguido)

    def cargar_red(self, ruta_red):
        # Método que se encarga de generar la red social, cargando y
        # guardando cada uno de los usuarios. Quizás otras funciones de
        # Pintogram sean útiles.
        datos_simple = list(cargar_archivos(path.join(ruta_red)))
        for i in range(len(datos_simple)):
            self.nuevo_usuario(datos_simple[i][0], datos_simple[i][1])
            for id_seguido in datos_simple[i][2]:
                self.follow(datos_simple[i][0], id_seguido)

    def unfollow(self, id_seguidor, id_seguido):
        for i in range(len(self.lista_usuarios)):
            if self.lista_usuarios[i].id == id_seguidor:
                for j in range(len(self.lista_usuarios[i].seguidos)):
                    if self.lista_usuarios[i].seguidos[j] == id_seguido:
                        self.lista_usuarios[i].seguidos.pop(j)

    def mis_seguidos(self, id_usuario):
        for i in range(len(self.lista_usuarios)):
            if self.lista_usuarios[i].id == id_usuario:
                return len(self.lista_usuarios[i].seguidos)

    def distancia_social(self, id_usuario_1, id_usuario_2, camino=None):
        camino = 0 if camino is None else camino
        usuario_origen = self.lista_usuarios
        camino = camino + 1
        if id_usuario_1 == id_usuario_2:
            return camino
        camino_corto = None
        for i in range(len(usuario_origen)):
            if i != camino:
                camino_recursion = self.distancia_social(usuario_origen[i].id
                                                         , id_usuario_2, camino)
                if camino_recursion:
                    if not camino_corto or camino_recursion < camino_corto:
                        camino_corto = camino_recursion
                else:
                    return float("inf")
        return camino_corto


if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "simple.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
    print(pintogram.distancia_social("3", "5"))
# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
