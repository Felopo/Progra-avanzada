from threading import Thread, Lock
from utils import reloj
import random


class Excavador(Thread):

    lock = Lock()

    def __init__(self, nombre, berlin, tunel):
        super().__init__()
        self.nombre = nombre
        self.berlin = berlin
        self.tunel = tunel
        self.daemon = True

    def run(self):
        while self.tunel.metros_avanzados <= self.tunel.largo:
            reloj(10)
            metros = random.randint(50, 100)
            self.avanzar(metros)
            probabilidad = random.uniform(0, 1)
            if 0 < probabilidad <= 0.1:
                self.problema_picota()
        self.tunel.tunel_listo.set()

    def problema_picota(self):
        print(f"{self.nombre} tuvo un problema con la picota...")
        with self.berlin:
            print(f"{self.nombre} tuvo un problema con la picota...")
            reloj(5)
            print("Vino Berlín y lo arregló")

    def avanzar(self, metros):
        with self.lock:
            self.tunel.metros_avanzados += metros
            print(f"{self.nombre} está avanzando en el tunel...")