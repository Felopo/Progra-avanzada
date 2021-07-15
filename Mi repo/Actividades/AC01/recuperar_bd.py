from phd_pinto import DrPintoDesencriptador


def recuperar_archivo(ruta):
    print('Recuperando archivo')
    objeto_pinto = DrPintoDesencriptador()
    objeto_pinto.ruta = ruta
    lista_desencriptados = objeto_pinto.desencriptar()
    return lista_desencriptados


def guardar_archivo(ruta, lineas_archivo):
    with open(ruta, "w", encoding="utf-8") as file:
        for linea in lineas_archivo:
            contenido = linea + "\n"
            file.write(contenido)
    print("Archivo guardado!!")
