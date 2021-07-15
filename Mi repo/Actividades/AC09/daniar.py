import os
import json
import time


class DocengelionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Docengelion):
            nuevo_obj = self.__dict__.copy()
            nuevo_obj["estado"] = "reparacion"
            nuevo_obj["registro_reparacion"] = "Fecha: " + time.strftime("%d/%m/%y") + \
                                               ", Hora: " + time.strftime("%H:%M:%S")
            return {"modelo": obj.modelo,
                    "nucleo": obj.nucleo,
                    "estado": nuevo_obj["estado"],
                    "registro_reparacion": nuevo_obj["registro_reparacion"]}
        return super().default(obj)


class Docengelion:
    def __init__(self, modelo, nucleo, *args, **kwargs):
        self.modelo = modelo
        self.nucleo = nucleo
        self.estado = 'funcional'
        self.registro_reparacion = None


def recibir_eva(ruta):
    lista_docengelions = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for dato in datos:
            docengelion = Docengelion(dato["modelo"], dato["nucleo"], dato["estado"],
                                      dato["registro_reparacion"])
            if dato["modelo"] == "01":
                print(dato["nucleo"])
            lista_docengelions.append(docengelion)
        return lista_docengelions


def reparar_eva(docengelion):
    docengelion_serializado = json.dumps(docengelion, cls=DocengelionEncoder)
    nombre_archivo = f"Unidad-{docengelion.modelo}.json"
    os.makedirs("Daniar", exist_ok=True)
    with open(os.path.join("Daniar", nombre_archivo), "w") as archivo:
        json.dump(docengelion_serializado, archivo)


if __name__ == '__main__':
    try:
        dcngelions = recibir_eva('docent.json')
        if dcngelions:
            print("DANIAR200: Ha cargado las unidades Docengelion")
        try:
            for unidad in dcngelions:
                reparar_eva(unidad)
            print("DANIAR201: Se estan reparando las unidades Docengelion")
        except Exception as error:
            print(f'Error: {error}')
            print("DANIAR501: No ha podido reparar las unidades Docengelion")
    except Exception as error:
        print(f'Error: {error}')
        print("DANIAR404: No ha podido cargar las unidades Docengelion")

