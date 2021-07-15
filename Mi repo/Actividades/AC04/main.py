from excavadores import Excavador
from imprimidores import Imprimidor
from threading import Lock
from utils import Tunel, BolsaDinero
from time import time


class Simulacion:

    def __init__(self):

        self.berlin = Lock()
        self.tunel = Tunel()
        self.bolsa_dinero = BolsaDinero()
        nombres_excavadores = ["Moscu", "Denver", "Helsinki"]
        nombres_falsificadores = ["Tokio", "Nairobi", "Rio"]
        self.excavadores = [Excavador(f"Excavador {i}",
                                      self.berlin,
                                      self.tunel) for i in nombres_excavadores]
        self.imprimidores = [Imprimidor(f"Imprimidor {i}",
                                        self.berlin,
                                        self.bolsa_dinero) for i in nombres_falsificadores]

    def comenzar(self):
        self.t_inicio = time()
        for excavador in self.excavadores:
            excavador.start()
        for imprimidor in self.imprimidores:
            imprimidor.start()
        self.tunel.tunel_listo.wait()
        self.bolsa_dinero.dinero_listo.wait()
        self.t_fin = time()
        self.estadisticas()

    def estadisticas(self):
        print("Estadísticas:")
        print(f"Cantidad de dinero: ${self.bolsa_dinero.dinero_acumulado}")
        print(f"Tiempo: {self.t_fin - self.t_inicio}")


if __name__ == '__main__':
    simulacion = Simulacion()
    simulacion.comenzar()
