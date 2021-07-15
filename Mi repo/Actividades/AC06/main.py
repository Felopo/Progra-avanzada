from carga_archivos import cargar_datos
from dcconductor import DCConductor
from excepcion_patente import ErrorPatente

'''
Para cada uno de los conductores chequea si su información está correcta.
Si no está correcta, se informa en pantalla que el conductor no pudo ser
registrado y la razón, y si no, se informa que fue inscrito exitosamente.
En este archivo la idea es capturar y manejar las excepciones.
También deberás contar la cantidad total de errores.
'''

registro_oficial, conductores = cargar_datos("regiztro_ofizial.json", "conductores.csv")
registro_oficial, conductores = cargar_datos("registro_oficial.json", "conductores.csv")

dcconductor = DCConductor(registro_oficial, conductores)

'''
Editar desde aquí
'''
if registro_oficial and conductores:
    contador = 0
    for conductor in dcconductor.conductores:
        error_celular = dcconductor.chequear_celular(conductor)
        if error_celular != "No hubo error":
            print(error_celular)
            contador += 1
        error_rut = dcconductor.chequear_rut(conductor)
        if error_rut != "No hubo error":
            print(error_rut)
            contador += 1
        error_nombre = dcconductor.chequear_nombre(conductor)
        if error_nombre != "No hubo error":
            print(error_nombre)
            contador += 1
        error_patente = dcconductor.chequear_patente(conductor)
        if error_patente != "No hubo error":
            print(error_patente)
            contador += 1
        if error_celular == "No hubo error"and error_rut == "No hubo error" and \
                error_patente == "No hubo error" and \
                error_nombre == "No hubo error":
            dcconductor.seleccionados.append(conductor)
    print(f"La cantidad de errores fueron {str(contador)}")