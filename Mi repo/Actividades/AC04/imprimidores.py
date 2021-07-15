from threading import Thread, Lock
from utils import reloj
import random


class Imprimidor(Thread):

    lock = Lock()

    def __init__(self, nombre, berlin, bolsa_dinero):
        super().__init__()
        self.nombre = nombre
        self.berlin = berlin
        self.bolsa_dinero = bolsa_dinero
        self.daemon = True

    def run(self):
        while self.bolsa_dinero.dinero_acumulado <= self.bolsa_dinero.meta_dinero:
            reloj(10)
            dinero = random.randint(100000, 500000)
            self.imprimir_dinero(dinero)
            probabilidad = random.uniform(0, 1)
            if 0 <= probabilidad < 0.2:
                self.problema_papel()
        self.bolsa_dinero.dinero_listo.set()

    def imprimir_dinero(self, dinero):
        print(f"{self.nombre} está imprimiendo dinero...")
        with self.lock:
            self.bolsa_dinero.dinero_acumulado += dinero
            print(f"{self.nombre} está imprimiendo dinero...")

    def problema_papel(self):
        with self.berlin:
            print(f"{self.nombre} tuvo un problema con el papel...")
            reloj(10)
            print("Llegó berlín y lo arregló")
