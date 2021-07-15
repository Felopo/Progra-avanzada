def reparar_comunicacion(ruta):
    out = bytearray()
    with open(ruta, 'rb') as bytes_file:
        datos = bytearray(bytes_file.read())
        for i in range(0, len(datos), 16):
            pivote = datos[i]
            chunk = datos[i:i+16]
            for dato in chunk:
                if dato >= pivote:
                    chunk.remove(dato)
                if dato == chunk[-1] and dato != pivote:
                    chunk.remove(pivote)
            out.extend(chunk)
    with open('Docengelion.bmp', 'wb') as bytes_file:
        bytes_file.write(out)


if __name__ == '__main__':
    try:
        reparar_comunicacion('EVA.xdc')
        print("PINTOSAR201: Comunicacion con pilotos ESTABLE")
    except Exception as error:
        print(f'Error: {error}')
        print("PINTOSAR301: CRITICO pilotos incomunicados DESCONEXION INMINENTE")