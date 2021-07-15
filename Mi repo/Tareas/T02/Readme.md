# Tarea 02: DCCampo :school_satchel:

## Consideraciones generales :octocat:
- Me faltaron varias cosas por implementar, las cuales voy a detallar más en la parte de "cosas implementadas y no implementadas".
- El drag and drop fue lo último que hice, por lo que no lo alcancé a terminar completamente pues se puede hacer el drop solamente cuando el personaje tiene azada y clickea en la posición a arar, pero cuando se planta una semilla, no se produce nada (solo se ve la imagen), pues no alcancé a ponerle las respectivas señales.
- El tamaño de la ventana lo hice para que se acomodara al mapa con el que probaba el juego, pero éste se puede cambiar y adecuarlo a otros tipos de mapas.
- Los items comprados no se adecuan a la foto del inventario porque no supe como hacerlo (pero aparecen en la parte de abajo de la pantalla) y van subiendo a medida que se agregan más.
- La VEL_MOVIMIENTO la hice de tal forma que el personaje se moviera de manera fluída por el mapa.
- No implementé el tiempo, ni el crecimiento de los cultivos (para que no revisen eso).
- Si en el archivo a cargar hubieran dos casas o más, solamente se crearía una de estas y sería la que está escrita más arriba en el archivo.
- Si en el archivo a cargar hubieran dos tiendas o más, solamente se crearía una de estas y sería la que está escrita más arriba en el archivo.
### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Ventanas**: Faltan cosas
    * Ventana de Inicio: Hecha completa 
    * Ventana de Juego: Me faltó hacer la barra de energía. No implementé que el mapa funcionara para cuando los espacios cultivables, casa o tienda estén en los bordes por lo que especifico en los supuestos. Tampoco funciona para casas o tienda al lado de espacio cultivable
    * Inventario: Hecha completa
    * Tienda: Hecha completa
* **Entidades**: Faltan cosas
    * Jugador: Faltó la barra de energía del jugado y que el jugador pueda recoger recursos (pues no los hay)
    * Recursos: No lo hice
    * Herramientas: Implementada la parte de que solo se puede arar si es que el jugador tiene azada. La otra parte no    
* **Tiempo**: No lo hice
    * Reloj: No lo hice
* **Funcionalidades Extra**:
    * K+I+P: No lo hice pues no implementé la barra del personaje
    * M+N+Y: Hecha completa
    * Pausa: No lo hice pues no implementé el tiempo, aunque si presionas el botón pausa, este cambia a reanudar (al hacer esto hay que volver a hacer click en la ventana del juego para poder seguir moviendote, pues son dos ventanas distintas)
* **General**:
    * Modularización: Creo que logro una adecuada separación entre back-end y front-end
    * Dependencia Circular: No hay
    * Archivos: No los alcancé a usar todos
    * Consistencia: Hecha completa (aunque hay cosas que no se actualizan pues no las alcancé a implementar, como la barra de energía, el reloj, etc), pero lo que está, mantiene consistencia
    * parametros.py: Todos los parametros se encuentran en parametros_generales.py (rutas de los sprites, VEL_MOVIMIENTO, etc)
* **Bonus**: No lo hice
    * Pesca: No hay
    * Casa: No implementado

## Señales :signal_strength: 
Aquí se explica donde se crea cada señal:
- ventana_inicio.py:
    - Aquí se usan 4 señales:
        
        1. senal_actualizar
        2. procesar (None)
        3. mapa_valido (None)
        4. datos_mapa (None)
- ventana_juego.py:
    - Aquí se usan 7 señales:
    
       1. senal_mapa_enviar_datos_mapa
       2. actualizar_senal_ventana
       3. senal_abrir_tienda
       4. senal_dinero_personaje
       5. senal_agregar_objeto_inventario
       6. mover_personaje_senal (None)
       7. senal_dinero_trampa (None)
       (Aquí creo un self.init_senales, donde se conectan las señales)
- ventana_lateral.py:
    - Aquí se usa 1 señal:
    
        1. senal_dinero_actualizado_lateral
- ventana_tienda.py:
    - Aquí se usan 3 señales:
    
        1. senal_dinero
        2. senal_dinero_actualizado
        3. senal_compra (None)

(Quizá me faltaron algunas señales, pero esas son las más relevantes en mi código)

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se deben crear archivos adicionales.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```exit()```
2. ```PyQt5.QWidgets```: ```QApplication(), QWidget(), QVBoxLayout(), QPushButton(),  QGridLayout(), QLabel(), QLineEdit(), QHBoxLayout()```
3. ```PyQt5.QtCore```: ```pyqtsignal(), QObject(), Qt(), QMimeData(), QRect()```
4. ```PyQt5.QtGui```: ```QIcon(), QPixmap(), QDrag(), QPainter()```
5. ```PyQt5```: ```uic```
6. ```os```: ```path.join(), listdir()```
7. ```random```: ```uniform(), choice()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```crear_mapa.py```: Contiene a ```CreadorMapa```, la cual recibe una señal de la ventana de inicio para crear el mapa.
2. ```main.py```: Es el módulo a ejecutar, y aquí se instancian la ventana_inicio y la ventana_juego.
3. ```parametros_generales.py```: Aquí se encuentran todos los parámetros utilizados en la tarea (sprites, N, VEL_MOVIMIENTO, etc).
4. ```personaje.py```: Contiene a la clase ```Personaje```, la cual es el back-end del personaje.
5. ```revisar_inputs.py```: Contiene la clase ```Revisar```, se encarga de revisar el mapa pedido por el usuario y le envía señales a la ventana_inicio para decirle si es válido o no.
6. ```ventana_inicio```: Contiene la clase ```VentanaInicio```. Es el front-end de la ventana de inicio.
7. ```ventana_juego```: Contiene la clase ```VentanaJuego```. Es el front-end donde se realiza el juego. También contiene a las clases ```DropLabel``` y ```DraggableLabel```, las cuales se encargan de crear etiquetas dropeables y draggueables.
8. ```ventana_lateral```: Tiene la clase ```VentanaLateral```.
9. ```ventana_tienda```: Contiene la clase ```VentanaTienda``` y la clase ```Ganar```. La clase Ganar se encarga de decirle al usuario que ganó si es que este se compra el boleto.
10. ```interfaces```: Es una carpeta, la cual contiene el front-end de la ```ventana_lateral``` y de la ```ventana_tienda```. Ambos son archivos .ui que fueron creados en QtDesigner.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Que una casa o una tienda no puedan estar al lado de un terreno cultivable, pues los alrededores del espacio cultivable son sprites de bordes, por lo que si hubiera una casa o una tienda ahí, se vería raro.
2. Que los espacios cultivables, tienda y casa no estarán en un borde del mapa, porque afectarían la visual.
-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. (https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5): Está implementado en el archivo ```ventana_juego.py``` en la línea 327. Son dos clases, una para poder crear objetos dragueables y la otra para crear objetos dropeables.
