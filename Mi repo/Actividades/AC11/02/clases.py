from random import randint, choice
from time import sleep
from threading import Lock, Thread, Event
from math import log2


class Critico(Event, Thread):
    def __init__(self):
        Thread.__init__(self, daemon=True)
        Event.__init__(self)
        self.start()

    def run(self):
        while True:
            sleep(randint(10, 100) / 10)
            self.set()


class Entrenador:

    critico = Critico()

    def __init__(self, nombre):
        self.nombre = nombre
        self.hp_programon_original = randint(100, 200)
        self.hp_programon = self.hp_programon_original
        self.ataque_programon = randint(90, 120)
        self.defensa_programon = randint(80, 100)

    def atacar(self, enemigo):
        dano = round(20 * self.ataque_programon / enemigo.defensa_programon)
        if self.critico.is_set():
            print(f"{self.nombre} Tendrá un golpe crítico!!")
            dano = dano * 2
            self.critico.clear()
        if enemigo.hp_programon <= 0:
            enemigo.hp_programon = 0
        print(f'{self} ataca {dano} a {enemigo}')
        enemigo.hp_programon -= dano

    def sanar(self):
        self.hp_programon = self.hp_programon_original

    def __repr__(self):
        return f'({self.nombre} HP:{self.hp_programon})'


class Batalla(Thread):

    id_actual = 1
    lock = Lock()
    ganadores = []

    def __init__(self):
        super().__init__()
        print('¡Batalla creada!')
        self.id = Batalla.id_actual
        Batalla.id_actual += 1
        self.oponente_1 = None
        self.oponente_2 = None
        self.ganador = None
        self.ganadores = Batalla.ganadores

    def run(self):
        with self.lock:
            if isinstance(self.oponente_1, Entrenador) and isinstance(self.oponente_2, Entrenador):
                print(f'{self} esperando batallas...')
                print(f'{self} lista para comenzar.')
                self.realizar_batalla()
            elif isinstance(self.oponente_1, Batalla) and isinstance(self.oponente_2, Batalla):
                # Se debería quedar esperando a que terminen las batallas y luego
                # correr el código de abajo, pero no pude hacer que se quedara esperando :(
                for ganador in self.ganadores:
                    if ganador.id == self.oponente_1.id:
                        self.oponente_1 = self.ganador
                    elif ganador.id == self.oponente_2.id:
                        self.oponente_2 = self.ganador
                if isinstance(self.oponente_1, Entrenador) and \
                        isinstance(self.oponente_2, Entrenador):
                    self.realizar_batalla()

    def realizar_batalla(self):
        print(f'----------¡Comienza batalla {self.id}! A '
              f'{int(log2(self.id))} de final----------')
        print(f'{self.oponente_1} versus {self.oponente_2}')
        opciones = [self.oponente_1, self.oponente_2]
        primero_en_atacar = choice(opciones)
        while self.oponente_1.hp_programon > 0 and self.oponente_2.hp_programon > 0:
            primero_en_atacar.atacar(self.oponente_2 if
                                     primero_en_atacar == self.oponente_1 else self.oponente_1)
            if primero_en_atacar == self.oponente_1:
                primero_en_atacar = self.oponente_2
            elif primero_en_atacar == self.oponente_2:
                primero_en_atacar = self.oponente_1
            sleep(0.1)
        if self.oponente_1.hp_programon <= 0:
            self.ganador = self.oponente_2
        else:
            self.ganador = self.oponente_1
        self.ganador.sanar()
        print(f'----------¡Gana {self.ganador}!----------')
        Batalla.ganadores.append(self.ganador)

    def __repr__(self):
        return f'Batalla {self.id}'
