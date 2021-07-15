# Tarea 0: LegoSweeper :school_satchel:

## Consideraciones generales :octocat:

<La Tarea funciona bien, pero me faltó hacer el bonus y en la linea __392__ del código, al argumento del lambda me faltó ponerle int(), para que me ordene los puntajes por todos los dígitos del número en vez de solo el primero.>

### Cosas implementadas y no implementadas :white_check_mark: :x:
* <Inicio Del Programa<sub>1</sub>>: Hecho Completo
    * Menú Inicio: Hecho Completo
    * Funcionalidades: Hecho Completo
    * Puntajes: __En la linea 392 me faltó ponerle int() al argumento del lambda__
* <Flujo del Juego<sub>2</sub>>: Hecho Completo
    * Menú de Juego: Hecho Completo
    * Tablero: Hecho Completo
    * Legos: Hecho Completo
    * Guardado de partida: Hecha Completo
* <Término del Juego<sub>3</sub>>: Hecho Completo
    * Fin del juego: Hecho Completo
    * Puntajes: Hecho Completo
* <General<sub>4</sub>>: Hecho Completo
    * Menús: Hecho Completo
    * Parámetros: Hecho Completo
* <Bonus<sub>5</sub>>: No lo Hice

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se deben crear archivos adicionales

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```:  __randint()__
2. ```math```: ```ceil()
3. ```sys```:  ```exit()
4. ```os.path```: ```join()


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Cuando el jugador ingresa una baldosa que ya está descubierta, se va a considerar su jugada igualmente como si no hubiera estado descubierta, pues en el enunciado no especificaba que hacer en ese caso>

## Explicación de las Funciones Usadas: :thinking:
1. ```menú_inicio()```:
    * Tiene las 4 opciones del Menú de Inicio
2. ```crear_tablero()```:
    * Crea el tablero con las dimensiones que indique el usuario
3. ```menú_juego(tab_legos, tab_jugador, nom_usuario)```:
    * Recibe un tablero con los legos repartidos, un tablero vacío (con puros espacios) para que juegue el jugador y recibe también el nombre de usuario que ingresa el jugador
    * En esta función es donde juega el jugador
    * Ambos tableros se van actualizando a medida que descubre baldosas el jugador
4. ```guardar_tableros(tab_legos, tab_jugador, nombre)```
    * Recibe dos tableros, el primero con los legos repartidos y el otro es el que vé el jugador, también recibe el nombre del achivo a guardar (nombre de usuario del jugador)
    * Guarda la partida del jugador
    * Guarda ambos tableros
5. ```cargar_lista(nombre)```:
    * Recibe el nombre del archivo a cargar (nombre de usuario del jugador)
    * Carga su partida previamente guardada
6. ```descubrir_baldosa(fila, columna, tablero)```:
    * Recibe la fila y columna que el jugador quiere descubrir, también recibe el tablero con los legos
    *  Descubre la baldosa que el jugador quiere descubrir

__PD: Puse las funciones en el readme porque no alcancé a comentar que hacía cada una en mi código
-----
