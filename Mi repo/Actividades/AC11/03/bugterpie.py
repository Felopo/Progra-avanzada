class Bugterpie(Exception):
    contador_programones = 0

    def __init__(self, programon):
        self.contador_programones = Bugterpie.contador_programones
        Bugterpie.contador_programones += 1
        print(f"El PROGRáMON N {programon.id}: {programon.nombre} es un Bugterpie")
        self.programon = programon

    @staticmethod
    def imprimir_bugterpies_atrapados():
        print(f"En total has capturado {Bugterpie.contador_programones} Bugterpies")
