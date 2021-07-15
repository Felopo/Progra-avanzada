from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        super().__init__(id_cliente, nombre, contrasena)
        self.tiene_fraude = False

    @property
    def saldo_actual(self):
        return self.saldo

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        if nuevo_saldo < 0:
            self.tiene_fraude = True
        else:
            self.saldo = nuevo_saldo

    def deposito_seguro(self, dinero):
        self.depositar(dinero)
        self.saldo_actual = self.saldo_actual - int(dinero)
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            datos_trans = str(self.id_cliente) + ", depositar, " + str(dinero)
            archivo.write(datos_trans)

    def retiro_seguro(self, dinero):
        if not self.tiene_fraude:
            self.retirar()
            self.saldo_actual = self.saldo_actual + int(dinero)
            ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
            with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
                datos_tans = str(self.id_cliente) + ", retirar, " + str(dinero)
                archivo.write(datos_tans)


class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        super().__init__()

    def cargar_clientes(self, ruta):
        with open(ruta, "rt") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea.strip()
                linea.split(",")
                cliente = ClienteSeguro(linea[0], linea[1], linea[3])
                self.clientes.append(cliente)

    def realizar_transaccion(self, id_cliente, dinero, accion):
        for cliente in self.clientes:
            if cliente[0] == id_cliente:
                if accion == "depositar":
                    cliente.deposito_seguro(dinero)
                elif accion == "retirar":
                    cliente.retiro_seguro(dinero)

    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        for elemento in historial:
            elemento.split(", ")
            id = elemento[0]
            accion = elemento[1]
            monto = elemento[2]
            lista_clientes = []
            ids_fraudulentos = []
            ruta_clientes = path.join('banco_seguro', 'clientes.txt')
            with open(ruta_clientes, 'a+') as archivo:
                archiv = archivo.readlines()
                for linea in archiv:
                    linea = linea.strip()
                    lista_clientes.append(linea)
                for cliente in lista_clientes:
                    cliente = cliente.split(", ")
                    id_cliente = cliente[0]
                    nom_cliente = cliente[1]
                    c_cliente = cliente[3]
                    print(id)
                    print(id_cliente)
                    if id_cliente == id:
                        if nom_cliente != accion:
                            ids_fraudulentos.append(cliente)
                            cliente_fraudulento = ClienteSeguro(id_cliente, nom_cliente, c_cliente)
                            cliente_fraudulento.tiene_fraude = True
                            archivo.write(cliente_fraudulento)

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        lista_transacciones = []
        ruta_transacciones = path.join("banco_seguro", "transacciones.txt")
        with open(ruta_transacciones, "a+") as archivo:
            lista = archivo.readlines()
            for elemento in lista:
                elemento = elemento.strip()
                lista_transacciones.append(elemento)
        lista_clientes = []
        with open(ruta, "a+") as archivo:
            lista = archivo.readlines()
            for elemento in lista:
                elemento = elemento.strip()
                lista_clientes.append(elemento)
            contador_clientes = 0
            ids_fraudulentos = []
            for dato in lista_transacciones:
                if dato.split(", ")[2] != lista_clientes[contador_clientes].split(", ")[2]:
                    id_cliente = lista_clientes[contador_clientes].split(", ")[0]
                    nom_cliente = lista_clientes[contador_clientes].split(", ")[1]
                    contra_cliente = lista_clientes[contador_clientes].split(", ")[3]
                    ids_fraudulentos.append(dato.split(", ")[0])
                    cliente_fraudulento = ClienteSeguro(id_cliente, nom_cliente, contra_cliente)
                    cliente_fraudulento.tiene_fraude = True
                    archivo.write(cliente_fraudulento)
                contador_clientes += 1
