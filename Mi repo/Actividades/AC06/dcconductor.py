import csv
from conductores import Conductor
from excepcion_patente import ErrorPatente
import os


class DCConductor:

    def __init__(self, registro_oficial, conductores):
        '''
        El constructor crea las estructuras necesarias para almacenar los datos
         proporcionados, recibe la información necesaria para el funcionamiento de la clase.
        '''
        self.registro_oficial = registro_oficial
        self.conductores = conductores
        self.seleccionados = list()

    def revisar_rut(self, rut):
        if "." in rut or "-" not in rut[8]:
            raise ValueError

    def chequear_rut(self, conductor):
        try:
            self.revisar_rut(conductor.rut)
        except ValueError:
            return f"Error: El rut {conductor.rut} no debe contener puntos o el guión no está en " \
                   "la posición en la que debería"
        else:
            return "No hubo error"

    def revisar_nombre(self, nombre):
        for dato in self.registro_oficial:
            if dato == nombre:
                return
        raise ValueError

    def chequear_nombre(self, conductor):
        try:
            self.revisar_nombre(conductor.nombre)
        except ValueError:
            return f"Error: El nombre del conductor {conductor.nombre} no está en el " \
                   f"registro oficial"
        else:
            return "No hubo error"

    def revisar_celular(self, celular):
        largo_celular = len(str(celular))
        string_celular = str(celular)
        if not celular.isnumeric():
            raise TypeError
        if largo_celular > 9:
            raise IndexError
        if string_celular[0] != "9":
            raise ValueError

    def chequear_celular(self, conductor):
        try:
            self.revisar_celular(conductor.celular)
        except TypeError:
            return f"Error: El número {conductor.celular} debe contener solamente números (int)"
        except IndexError:
            return f"Error:El número {conductor.celular} debe ser de largo nueve"
        except ValueError:
            return f"Error:El número {conductor.celular} debe empezar con un 9"
        else:
            return "No hubo error"

    def revisar_patente(self, conductor, nombre, patente):
        for dato in self.registro_oficial:
            if nombre == dato and patente == self.registro_oficial[dato]:
                return
        raise ErrorPatente(conductor)

    def chequear_patente(self, conductor):
        try:
            self.revisar_patente(conductor, conductor.nombre, conductor.patente)
        except ErrorPatente as error:
            return f"Error: {error}"
        else:
            return "No hubo error"
