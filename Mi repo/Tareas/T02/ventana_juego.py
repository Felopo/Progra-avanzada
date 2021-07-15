from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, QApplication)
from PyQt5.QtCore import (pyqtSignal, Qt, QMimeData)
from PyQt5.QtGui import (QPixmap, QIcon, QDrag, QPainter)
import random
from parametros_generales import (N, PATHS, PATHS_CHOCLO, PATHS_ALCACHOFA, PATHS_RECURSOS,
                                  PATHS_OTROS, POSICION_VENTANA_JUEGO)
from parametros_generales import PATHS_PERSONAJE as PP
from personaje import Personaje
from ventana_lateral import VentanaLateral
from ventana_tienda import VentanaTienda


class VentanaJuego(QWidget):

    senal_mapa_enviar_datos_mapa = pyqtSignal(dict, list)
    actualizar_senal_ventana = pyqtSignal(dict)
    senal_abrir_tienda = pyqtSignal()
    senal_dinero_personaje = pyqtSignal(int)
    senal_agregar_objeto_inventario = pyqtSignal(str, int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.personaje = None
        self.n = N
        self.x = 840
        self.y = 850
        self._frame = 1
        self.sprite_actual = None
        self.personaje_ventana = None
        self.casa = None
        self.fondo = None
        self.personaje = None
        self.tienda = None
        self.ventana_tienda = VentanaTienda()
        self.ventana_lateral = None
        self.mover_personaje_senal = None
        self.lista_cultivables = None
        self.diccionario_coord = None
        self.largo_mapa = None
        self.ancho_mapa = None
        self.senal_dinero_trampa = None
        self.cultivable = None
        self.espacio_cultivable_sprite = None
        self.grilla_inventario = QGridLayout()
        self.inventario_v = QVBoxLayout()
        self.inventario_v.addStretch(1)
        self.cantidad_items_inventario = 0
        self.filas_inventario = 0
        self.set_vacio = set()
        self.lista_etiquetas_cultivables = []
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("DCCampo")
        self.setWindowIcon(QIcon(PATHS["logo"]))
        self.setGeometry(POSICION_VENTANA_JUEGO[0], POSICION_VENTANA_JUEGO[1], self.x, self.y)
        self.fondo = QLabel(self)
        self.fondo.setGeometry(-300, -300, 5000, 5000)
        self.ruta_fondo = PATHS["imagen_fondo"]
        pixeles_fondo = QPixmap(self.ruta_fondo)
        self.fondo.setPixmap(pixeles_fondo)
        self.fondo.setScaledContents(True)

    def inventario(self):
        self.fondo_inventario = QLabel(self)
        self.ruta_fondo_inventario = PATHS_OTROS["inventario_fondo"]
        pixeles_fondo_inventario = QPixmap(self.ruta_fondo_inventario).scaled(self.n *
                                                                              self.ancho_mapa,
                                                                              self.n *
                                                                              self.largo_mapa/2)
        self.fondo_inventario.setPixmap(pixeles_fondo_inventario)
        self.fondo_inventario.setScaledContents(True)
        self.fondo_inventario.move(0, self.n * self.largo_mapa)

    def agregar_item_inventario(self, item, posicion):
        if item == "semillas_choclo":
            self.ruta_item = PATHS_CHOCLO["fase_1"]
            self.item = DraggableLabel(ruta=self.ruta_item)
        elif item == "semillas_alcachofa":
            self.ruta_item = PATHS_ALCACHOFA["fase_1"]
            self.item = DraggableLabel(ruta=self.ruta_item)
        else:
            self.ruta_item = PATHS_OTROS[item]
            self.item = DraggableLabel(ruta=PATHS[self.espacio_cultivable_sprite])
        pixeles_item = QPixmap(self.ruta_item)
        self.item.setPixmap(pixeles_item)
        self.item.setScaledContents(True)
        self.item.setMaximumHeight(30)
        self.item.setMaximumWidth(30)
        self.grilla_inventario.addWidget(self.item, self.filas_inventario,
                                         self.cantidad_items_inventario)
        self.inventario_v.addLayout(self.grilla_inventario)
        self.setLayout(self.inventario_v)
        self.cantidad_items_inventario += 1
        if posicion > 12 and self.cantidad_items_inventario > 12:
            self.filas_inventario += 1
            self.cantidad_items_inventario = 0

    def init_personaje(self, pos_x, pos_y, largo_mapa, ancho_mapa, lista_rocas, lista_pasto):
        self.ventana_lateral = VentanaLateral()
        self.personaje = Personaje(pos_y, pos_x, largo_mapa, ancho_mapa, lista_rocas, lista_pasto)
        self.senal_dinero_personaje.connect(self.ventana_tienda.comprable)
        self.senal_dinero_personaje.emit(self.personaje._dinero)
        self.personaje_ventana = QLabel(self)
        self.personaje_ventana.move(pos_y * self.n, pos_x * self.n)
        self.sprite_actual = QPixmap(PP[("D", 1)]).scaled(self.n, self.n)
        self.personaje_ventana.setPixmap(self.sprite_actual)
        self.init_signals()

    def init_signals(self):
        self.actualizar_senal_ventana.connect(self.actualizar_ventana)
        self.mover_personaje_senal = self.personaje.mover_personaje_senal
        self.personaje.actualizar_senal_ventana = self.actualizar_senal_ventana
        self.personaje.senal_dinero = self.ventana_tienda.senal_dinero
        self.ventana_tienda.senal_dinero.connect(self.ventana_tienda.comprable_inicial)
        self.ventana_tienda.senal_compra = self.personaje.senal_compra
        self.personaje.senal_compra.connect(self.personaje.agregar_objeto)
        self.personaje.senal_dinero_actualizado = self.ventana_tienda.senal_dinero_actualizado
        self.ventana_tienda.senal_dinero_actualizado.connect(self.ventana_tienda.comprable)
        self.personaje.senal_dinero_actualizado_lateral = \
            self.ventana_lateral.senal_dinero_actualizado_lateral
        self.ventana_lateral.senal_dinero_actualizado_lateral.connect(
            self.ventana_lateral.cambiar_dinero)
        self.personaje.senal_agregar_objeto_inventario = self.senal_agregar_objeto_inventario
        self.senal_agregar_objeto_inventario.connect(self.agregar_item_inventario)
        self.senal_dinero_trampa = self.personaje.senal_dinero_trampa
        self.personaje.senal_dinero_trampa.connect(self.personaje.dinero_trampa)

    key_event_dict = {
        Qt.Key_D: "R",
        Qt.Key_A: "L",
        Qt.Key_W: "U",
        Qt.Key_S: "D"}
    key_event_dict_trampa = {
        Qt.Key_M: "M",
        Qt.Key_N: "N",
        Qt.Key_Y: "Y"}

    def keyPressEvent(self, evento):
        if evento.key() in self.key_event_dict:
            accion = self.key_event_dict[evento.key()]
            self.mover_personaje_senal.emit(accion)
        if evento.key() in self.key_event_dict_trampa:
            self.set_vacio.add(self.key_event_dict_trampa[evento.key()])
        if "M" in self.set_vacio and "N" in self.set_vacio and "Y" in self.set_vacio:
            self.senal_dinero_trampa.emit()

    def keyReleaseEvent(self, evento):
        self.set_vacio = set()

    def mousePressEvent(self, event):
        for index, valor in enumerate(self.lista_cultivables):
            if len(self.lista_cultivables[index]) == 2:
                if (int(event.y()/self.n), int(event.x()/self.n)) in \
                        self.lista_cultivables[index + 2] and self.personaje.azada:
                    for i in range(len(self.lista_etiquetas_cultivables)):
                        for j in range(len(self.lista_etiquetas_cultivables[i])):
                            if type(self.lista_etiquetas_cultivables[i][j]) == list:
                                if [int(event.x()/self.n), int(event.y()/self.n)] \
                                        == self.lista_etiquetas_cultivables[i][j]:
                                    self.lista_etiquetas_cultivables[i][j -
                                                                        1].setAcceptDrops(True)

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, valor):
        self._frame = valor if valor <= 4 else 1

    def actualizar_ventana(self, evento):
        direccion = evento["direccion"]
        self.frame += 1
        self.sprite_actual = QPixmap(PP[(direccion, self.frame)]).scaled(self.n, self.n)
        self.personaje_ventana.setPixmap(self.sprite_actual)
        self.personaje_ventana.move(evento["x"]*self.n, evento["y"]*self.n)
        if [int(self.personaje._y), int(self.personaje._x)] in self.diccionario_coord["tienda"]:
            self.senal_abrir_tienda.connect(self.ventana_tienda.abrir_ventana)
            self.senal_abrir_tienda.emit()

    def creador_pasto(self, coordenada):
        self.pasto = QLabel(self)
        probabilidad = random.uniform(0, 1)
        if 0.4 < probabilidad <= 1:
            self.ruta_imagen_pasto = PATHS["espacio_pasto_solo_1"]
        elif 0 < probabilidad <= 0.1:
            self.ruta_imagen_pasto = PATHS["espacio_pasto_raro_1"]
        elif 0.1 < probabilidad <= 0.2:
            self.ruta_imagen_pasto = PATHS["espacio_pasto_raro_2"]
        elif 0.2 < probabilidad <= 0.3:
            self.ruta_imagen_pasto = PATHS["pasto_flores_amarillas"]
        elif 0.3 < probabilidad <= 0.4:
            self.ruta_imagen_pasto = PATHS["pasto_flores_amarillas_blancas"]
        pixeles_pasto = QPixmap(self.ruta_imagen_pasto).scaled(self.n, self.n)
        self.pasto.setPixmap(pixeles_pasto)
        self.pasto.move(coordenada[1]*self.n, coordenada[0]*self.n)

    def creador_rocas(self, coordenada):
        self.roca = QLabel(self)
        self.ruta_imagen_roca = PATHS["espacio_piedra_1"]
        pixeles_roca = QPixmap(self.ruta_imagen_roca).scaled(self.n, self.n)
        self.roca.setPixmap(pixeles_roca)
        self.roca.move(coordenada[1]*self.n, coordenada[0]*self.n)

    def creador_casa(self, coordenada):
        self.casa = QLabel(self)
        self.ruta_imagen_casa = PATHS["espacio_casa"]
        pixeles_casa = QPixmap(self.ruta_imagen_casa).scaled(2 * self.n, 2 * self.n)
        self.casa.setPixmap(pixeles_casa)
        self.casa.move(coordenada[1] * self.n, coordenada[0] * self.n)

    def creador_tienda(self, coordenada):
        self.tienda = QLabel(self)
        self.ruta_imagen_tienda = PATHS["espacio_tienda"]
        pixeles_tienda = QPixmap(self.ruta_imagen_tienda).scaled(2 * self.n, 2 * self.n)
        self.tienda.setPixmap(pixeles_tienda)
        self.tienda.move(coordenada[1] * self.n, coordenada[0] * self.n)

    def creador_espacios_cultivables(self, lista_dimensiones, lista_coord_bordes, lista_coord):
        # Bordes
        for pasto in range(lista_dimensiones[0]):
            self.borde_sup = QLabel(self)
            self.ruta_borde_sup = PATHS["espacio_cultivable_pasto_arriba"]
            pixeles_borde_sup = QPixmap(self.ruta_borde_sup).scaled(self.n, self.n)
            self.borde_sup.setPixmap(pixeles_borde_sup)
            self.borde_sup.move(lista_coord[pasto][1]*self.n, (lista_coord[pasto][0] - 1)*self.n)
        for pasto in range(1, lista_dimensiones[1] + 1):
            self.borde_der = QLabel(self)
            self.ruta_borde_der = PATHS["espacio_cultivable_pasto_derecha"]
            pixeles_borde_der = QPixmap(self.ruta_borde_der).scaled(self.n, self.n)
            self.borde_der.setPixmap(pixeles_borde_der)
            self.borde_der.move((lista_coord[(pasto * lista_dimensiones[0]) - 1][1] + 1)*self.n,
                                lista_coord[(pasto * lista_dimensiones[0]) - 1][0]*self.n)
        for pasto in range(lista_dimensiones[0]):
            self.borde_inf = QLabel(self)
            self.ruta_borde_inf = PATHS["espacio_cultivable_pasto_abajo"]
            pixeles_borde_inf = QPixmap(self.ruta_borde_inf).scaled(self.n, self.n)
            self.borde_inf.setPixmap(pixeles_borde_inf)
            self.borde_inf.move((lista_coord[(lista_dimensiones[1] - 1) *
                                             lista_dimensiones[0]][1] + pasto)*self.n,
                                (lista_coord[(lista_dimensiones[1] - 1) *
                                             lista_dimensiones[0]][0] + 1)*self.n)
        for pasto in range(lista_dimensiones[1]):
            self.borde_izq = QLabel(self)
            self.ruta_borde_izq = PATHS["espacio_cultivable_pasto_izquierda"]
            pixeles_borde_izq = QPixmap(self.ruta_borde_izq).scaled(self.n, self.n)
            self.borde_izq.setPixmap(pixeles_borde_izq)
            self.borde_izq.move((lista_coord[pasto*lista_dimensiones[0]][1] - 1)*self.n,
                                (lista_coord[pasto*lista_dimensiones[
                                    0]][0])*self.n)
        # Zona cultivable
        lista_cultivables = ["espacio_cultivable_1", "espacio_cultivable_2"]
        self.espacio_cultivable_sprite = random.choice(lista_cultivables)
        for zona in range(len(lista_coord)):
                self.cultivable = DropLabel(self)
                self.ruta_cultivable = PATHS[self.espacio_cultivable_sprite]
                pixeles_cultivable = QPixmap(self.ruta_cultivable).scaled(self.n, self.n)
                self.cultivable.setPixmap(pixeles_cultivable)
                self.cultivable.move(lista_coord[zona][1] * self.n, lista_coord[zona][0] * self.n)
                self.lista_etiquetas_cultivables.append(
                    [self.cultivable, [lista_coord[zona][1], lista_coord[zona][0]]])
        # Esquinas
        esquina_sup_izq = lista_coord_bordes[0]
        esquina_sup_der = lista_coord_bordes[lista_dimensiones[0] + 1]
        esquina_inf_izq = lista_coord_bordes[2 * (lista_dimensiones[0] + 1) +
                                             lista_dimensiones[1] + 1]
        esquina_inf_der = lista_coord_bordes[
            lista_dimensiones[0] + 1 + lista_dimensiones[1] + 1]
        self.esquina_sup_izq = QLabel(self)
        self.ruta_sup_izq = PATHS["espacio_cultivable_pasto_sup_izq"]
        pixeles_sup_izq = QPixmap(self.ruta_sup_izq).scaled(self.n, self.n)
        self.esquina_sup_izq.setPixmap(pixeles_sup_izq)
        self.esquina_sup_izq.move(esquina_sup_izq[1] * self.n, esquina_sup_izq[0] * self.n)
        self.esquina_sup_der = QLabel(self)
        self.ruta_sup_der = PATHS["espacio_cultivable_pasto_sup_der"]
        pixeles_sup_der = QPixmap(self.ruta_sup_der).scaled(self.n, self.n)
        self.esquina_sup_der.setPixmap(pixeles_sup_der)
        self.esquina_sup_der.move(esquina_sup_der[1] * self.n, esquina_sup_der[0] * self.n)
        self.esquina_inf_izq = QLabel(self)
        self.ruta_inf_izq = PATHS["espacio_cultivable_pasto_inf_izq"]
        pixeles_inf_izq = QPixmap(self.ruta_inf_izq).scaled(self.n, self.n)
        self.esquina_inf_izq.setPixmap(pixeles_inf_izq)
        self.esquina_inf_izq.move(esquina_inf_izq[1] * self.n, esquina_inf_izq[0] * self.n)
        self.esquina_inf_der = QLabel(self)
        self.ruta_inf_der = PATHS["espacio_cultivable_pasto_inf_der"]
        pixeles_inf_der = QPixmap(self.ruta_inf_der).scaled(self.n, self.n)
        self.esquina_inf_der.setPixmap(pixeles_inf_der)
        self.esquina_inf_der.move(esquina_inf_der[1] * self.n, esquina_inf_der[0] * self.n)

    def datos_recibidos(self, diccionario, lista_cultivables):
        self.lista_cultivables = lista_cultivables
        self.diccionario_coord = diccionario
        # Crear pasto
        for pasto in diccionario["pasto"]:
            self.creador_pasto(pasto)
        # Crear espacios cultivables
        for index, valor in enumerate(lista_cultivables):
            if len(lista_cultivables[index]) == 2:
                self.creador_espacios_cultivables(lista_cultivables[index],
                                                  lista_cultivables[index + 1],
                                                  lista_cultivables[index + 2])
        # Crear rocas en el mapa
        for roca in diccionario["rocas"]:
            self.creador_rocas(roca)
        # Crear casa
        self.creador_casa(diccionario["casa"][0])
        # Crear tienda
        self.creador_tienda(diccionario["tienda"][0])
        # Crear personaje
        for espacio in diccionario["pasto"]:
            if espacio not in diccionario["rocas"] and espacio not in diccionario["tienda"]:
                self.largo_mapa = diccionario["largo_mapa"]
                self.ancho_mapa = diccionario["ancho_mapa"]
                self.init_personaje(espacio[0], espacio[1],
                                    diccionario["largo_mapa"], diccionario["ancho_mapa"],
                                    diccionario["rocas"], diccionario["pasto"])
                self.inventario()
                break
        self.show()

# Drag and Drop
# Código sacado de "https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5",
# del comentario del usuario "eyllanesc"


class DraggableLabel(QLabel):

    def __init__(self, ruta, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.ruta = ruta

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() \
                < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.ruta)
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)


class DropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.posicion = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        self.posicion = event.pos()
        text = event.mimeData().text()
        self.setText(text)
        pixeles = QPixmap(text)
        self.setPixmap(pixeles)
        self.setScaledContents(True)
        event.acceptProposedAction()
        self.setAcceptDrops(False)
