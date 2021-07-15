# Tarea 01: Initial P :school_satchel:

## Consideraciones generales :cactus: 
- <1> Mi tarea funciona bien, hasta que llega al inicio de la carrera, pues no tuve tiempo de terminar la parte de las vueltas y recompensas por jugador, por lo que esta última parte quizá se vea hecha a la rapida y con errores.
- <2> Lo otro que tampoco alcancé a hacer fue la parte de guardar y cargar partidas con los atributos de pilotos y vehículos actualizados pues como no hice lo de la carrera no alcancé a guardar esos atributos actualizados.
- <3> Puse unas cosas para abrir archivos en el main porque estaba desesperado y cuando me quedaba poco tiempo, por lo que no es necesario la revisión de estos.
- <4> Cuando el usuario elige su nombre de usuario y el nombre de su auto, estos son guardados en los respectivos archivos como indica el enunciado, pero como no alcancé a terminar la parte de la carrera con los contrincantes, usuario y vehículos de ambos, no se llega a guardar después la partida. Por lo mismo, no se puede cargar partida (en la linea 167 de el módulo menus.py tengo comentado esto que me faltó hacer).
- <5> Usé la función sleep() del módulo time para que la carrera se demorara un poco en comenzar.
- <6> Hice el bonus de los menús, pero no el de los power ups.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Programación Orientada a Objetos: Me faltó hacer el diagrama de clases actualizado.
    * Diagrama: El diagrama que entregué es el de la primera entrega de este, por lo que a este le faltan muchas otras clases y métodos que le fui agregando a medida que avanzaba
    * Definición de clases: Hecha Completa
    * Relaciones entre clases: Hecha completa 
* Cargar y guardar partidas: Leer ```consideraciones generales <4>```
* Initial P:
    * Crear partida: Hecha completa
    * Pits: Se pueden comprar mejoras de manera correcta, pero no repara el vehículo ni añade el tiempo a la siguiente vuelta.
    * Carrera: Se calcula correctamente todo lo que pide el enunciado, pero lo demás no funciona, pues no lo alcancé a terminar y no está hecho.
    * Fin carrera: No está hecha
* Consola: Hecha completa
* Archivos: Hecha completa
* Bonus:
    * Buenas prácticas: Hecha completa
    * Power ups: No la hice

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No se deben crear archivos adicionales.
## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint(), random(), choice()```
2. ```os.path```: ```join()``` 
3. ```math```: ```ceil()```, ```floor()```
4. ```sys```: ```exit()```
5. ```time```: ```sleep()```
6. ```abc```: ```ABC()```, ```abstractmethod()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entidades.py```: Contiene a las clases:
    * ```Vehiculo```, de la cual heredan los 4 tipos de vehiculos.
    * ```Pistas```, de la cual heredan la pista hielo y roca, y de estas hereda la pista suprema
    * ```Piloto```, de la cual heredan los 3 equipos posibles para los pilotos
2. ```funciones.py```: 
    * Este módulo contiene todas las fórmulas (en funciones) para todas las cosas que pedía el enunciado que ocurrían durante la carrera como: hipotermia, tiempo por vuelta, etc.
    * También le agregué algunas otras funciones para ordenar los archivos si es que las columnas venían desordenadas.
3. ```menus.py``` y ```menus_2.py```: Son todos los menús que sirven para que el juego funcione hechos con clases abstractas. (lo separé en 2 módulos porque se me estaban acabando las lineas).
4. ```carrera.py```: Contiene a las clases Contrincante y Carrera
5. ```juego.py```: Contiene a la clase juego, la cual es la que guarda al usuario, sus autos, y la lista de contrincantes. Se va actualizando a medida que avanza el juego y hay cambios en alguno de estos objetos.
PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>
## Descuentos
```Se que estoy entregando el README.md tarde (perdonn, se me había olvidado :c), pero lo voy a subir para que se les haga más fácil la corrección de mi tarea (aceptando los descuentos por entregar tarde el README.md).```
