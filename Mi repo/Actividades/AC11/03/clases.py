from bugterpie import Bugterpie
import json


indices_generaciones = {
    1: (1, 151),
    2: (152, 251),
    3: (252, 386),
    4: (387, 493),
    5: (494, 649)
}


class Programon:
    def __init__(self, id, nombre, tipo, generacion):
        self.id = int(id)
        self.nombre = nombre
        self.tipo = tipo
        self.generacion = int(generacion)

    def __repr__(self):
        return f'PROGRáMON N°{self.id:0>3}: {self.nombre}'


class Pydgey:
    def __init__(self, path_data):
        self.data = None
        self.cargar_data(path_data)

    def cargar_data(self, path_data):
        with open(path_data, 'r', encoding='utf-8') as file:
            self.data = json.load(file, object_hook=lambda x: Programon(**x))

    @staticmethod
    def aire_afilatipo(programon):
        lista_pokemon = []
        for pokemon in programon.tipo:
            if pokemon not in lista_pokemon:
                lista_pokemon.append(pokemon)
            elif pokemon in lista_pokemon:
                raise TypeError(
                        f"El PROGRáMOn N {programon.id}: "
                        f"{programon.nombre} tiene uno o más tipos repetidos {programon.tipo}")
            elif len(lista_pokemon) > 2:
                raise TypeError(f"El PROGRáMON N {programon.id}: {programon.nombre} "
                                f"tiene más de dos tipos: {programon.tipo}")

    @staticmethod
    def pico_taladraid(programon):
        if programon.id not in range(indices_generaciones[programon.generacion][0],
                                     indices_generaciones[programon.generacion][1] + 1):
            raise IndexError(f"El PROGRáMON N {programon.id}: {programon.nombre} "
                             f"no corresponde a la generación {programon.generacion}")

    @staticmethod
    def remolinombre(programon):
        if "bug" in programon.nombre or "Bug" in programon.nombre:
            raise Bugterpie(programon)

    def encontrar_errores(self):
        for programon in self.data:
            print(f'>> Se procesa {programon}')
            try:
                self.aire_afilatipo(programon)

            except TypeError as err:
                if len(programon.tipo) > 2:
                    print(err)
                    if programon.tipo[0] != programon.tipo[1]:
                        programon.tipo = programon.tipo[0:2]
                    else:
                        programon.tipo = programon.tipo[0]
                    print(f">>> Tipo corregido: PROGRáMON N {programon.id}: {programon.nombre} "
                          f"tipo {programon.tipo}")
                elif len(programon.tipo) == 2:
                    print(err)
                    programon.tipo = programon.tipo[0]
                    print(f">> Tipo corregido: PROGRáMON N {programon.id}: {programon.nombre} "
                          f"tipo {programon.tipo}")

            try:
                self.pico_taladraid(programon)

            except IndexError as err:
                print(err)
                for generacion in indices_generaciones:
                    if programon.id in range(
                            indices_generaciones[generacion][0],
                            indices_generaciones[generacion][1] + 1):
                        programon.generacion = generacion
                        print(f">> Generación corregida: PROGRáMON N {programon.id}: "
                              f"{programon.nombre} generación {programon.generacion}")

            try:
                self.remolinombre(programon)

            except Bugterpie as err:
                programon.nombre = programon.nombre.lower()
                programon.nombre = programon.nombre.replace("bug", "progra")
                programon.nombre = programon.nombre.capitalize()
                print(f">> Nombre corregido: PROGRáMON N {programon.id}: {programon.nombre}")
