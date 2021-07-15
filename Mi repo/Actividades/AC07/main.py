from leer_archivos import read_file
from collections import deque


class Ayudante:

    hijos = {"Coordinador": "Jefe",
             "Jefe": "Mentor",
             "Mentor": "Novato",
             "Novato": None}

    def __init__(self, nombre, rango, tipo, afinidad, eficiencia):
        self.nombre = nombre
        self.rango = rango
        self.tipo = tipo
        self.afinidad = afinidad
        self.eficiencia = eficiencia
        self.hijos_tareos = []
        self.hijos_docencios = []
        self.coordinador_padre = None

    def agregar_ayudante(self, ayudante):
        if ayudante.rango == "Coordinador" and ayudante.tipo == "Coordinador":
            self.coordinador_padre = ayudante
            return
        if ayudante.rango == Ayudante.hijos[self.rango] and ayudante.tipo == "Tareo":
            self.hijos_tareos.append(ayudante)
        elif ayudante.rango == Ayudante.hijos[self.rango] and ayudante.tipo == "Docencio":
            self.hijos_docencios.append(ayudante)
        else:
            if ayudante.rango == "Jefe" and ayudante.tipo == "Tareo":
                for hijo in self.hijos_tareos:
                    if hijo.tipo == ayudante.tipo:
                        hijo.agregar_ayudante(ayudante)
                        break
            elif ayudante.rango == "Jefe" and ayudante.tipo == "Docencio":
                for hijo in self.hijos_tareos:
                    if hijo.tipo == ayudante.tipo:
                        hijo.agregar_ayudante(ayudante)
                        break
            elif ayudante.rango == "Mentor" and ayudante.tipo == "Tareo":
                for hijo in self.hijos_tareos:
                    if hijo.tipo == ayudante.tipo:
                        hijo.agregar_ayudante(ayudante)
                        break
            elif ayudante.rango == "Mentor" and ayudante.tipo == "Docencio":
                for hijo in self.hijos_tareos:
                    if hijo.tipo == ayudante.tipo:
                        hijo.agregar_ayudante(ayudante)
                        break


class BFS(Ayudante):

    def __iter__(self):
        cola = deque()
        cola.append(self)
        while len(cola) > 0:
            nodo_actual = cola.popleft()
            yield nodo_actual
            for ayudante in self.hijos_tareos:
                if ayudante.tipo == "Tareo":
                    for hijo in ayudante.hijos_tareos:
                        cola.append(hijo)
            for ayudante in self.hijos_docencios:
                if ayudante.tipo == "Docencio":
                    for hijo in ayudante.hijos_docencios:
                        cola.append(hijo)


def grupo_mayor_eficiencia(sistema):
    for ayudante in sistema.hijos_tareos:
        print(imprimir_grupo(ayudante))
    for ayudante in sistema.hijos_docencios:
        print(imprimir_grupo(ayudante))


def imprimir_grupo(ayudante):
    arbol = BFS(ayudante.nombre, ayudante.rango, ayudante.tipo,
                ayudante.afinidad, ayudante.eficiencia)
    for nodo in arbol.hijos_tareos:
        print(f"{nodo.nombre}")


def instanciar_cuerpo_ayudantes(ayudantes):
    # No modificar
    enzini = Ayudante(**ayudantes[0])
    for data in ayudantes[1:]:
        enzini.agregar_ayudante(Ayudante(**data))
    return enzini


if __name__ == "__main__":
    # No modificar
    ayudantes = read_file()
    cuerpo_ayudantes = instanciar_cuerpo_ayudantes(ayudantes)
    grupo_mayor_eficiencia(cuerpo_ayudantes)
