class Juego:
    def __init__(self, jugador, vehiculo):
        self.jugador = jugador
        self.vehiculo = vehiculo
        self.pista = None
        self.vehiculos = []
        self.contrincantes = []

    def agregar_contrincante(self, contrincante):
        self.contrincantes.append(contrincante)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def __str__(self):
        return self.jugador.nombre + self.vehiculo.nombre

    def __repr__(self):
        return str(self)
