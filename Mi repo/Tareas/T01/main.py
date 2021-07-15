import parametros
import menus
import menus_2
import carrera


print()
print("----- Bienvenido a Initial P -----")
menu_sesion = menus.MenuDeSesion()
carga_o_nueva_partida = menu_sesion.ingresar_input()
sigue_en_menu = True
if carga_o_nueva_partida == "nueva_partida":
    juego = menu_sesion.crear_nueva_partida()
elif carga_o_nueva_partida == "carga_partida":
    juego = menu_sesion.cargar_partida()
while sigue_en_menu:
    menu_principal = menus.MenuPrincipal(juego).ingresar_input()
    if menu_principal == "comprar_vehiculo":
        menus.CompraDeVehiculos(juego).ingresar_input()
    elif menu_principal == "iniciar_carrera":
        menu_preparacion_carrera = menus_2.MenuPreparacionCarrera(juego)
        juego = menu_preparacion_carrera.ingresar_input()
        continua_carrera = True
        while continua_carrera:
            menu_carrera = menus_2.MenuCarrera().ingresar_input()
            if menu_carrera == "ir_a_los_pits":
                juego = menus_2.MenuPits(juego).ingresar_input()
            elif menu_carrera == "continuar_carrera":
                juego_carrera = carrera.Carrera(juego).agregar_contrincantes()
                sigue_dando_vueltas = True
                while sigue_dando_vueltas:
                    carrera = carrera.Carrera(juego_carrera).vuelta()
    #   Se que guardar partida debería estar en la clase del menu_principal, pero no alcancé
    #   a cambiarlo.
    elif menu_principal == "guardar_partida":
        linea_piloto_a_guardar = juego.jugador.nombre + str(juego.jugador.dinero) + \
         juego.jugador.personalidad + str(juego.jugador.contextura) + \
         str(juego.jugador.equilibrio) + str(juego.jugador.experiencia) + juego.jugador.equipo
        linea_vehiculo_a_guardar_autr = juego.vehiculo.nombre + juego.vehiculo.dueno + \
                                        juego.vehiculo.categoria + str(juego.vehiculo._chasis) + \
                                        str(juego.vehiculo._carroceria) + \
                                        str(juego.vehiculo._ruedas) + str(juego.vehiculo._motor) + \
                                        str(juego.vehiculo.peso)
        linea_vehiculo_a_guardar_mobi = juego.vehiculo.nombre + juego.vehiculo.dueno + \
            juego.vehiculo.categoria + str(juego.vehiculo._chasis) + \
            str(juego.vehiculo._carroceria) + \
            str(juego.vehiculo._ruedas) + str(juego.vehiculo._zapatillas) + \
            str(juego.vehiculo.peso)

        with open(parametros.PATHS["PILOTOS"][1], "a+", encoding="utf-8") as archivo:
            archivo.write(linea_piloto_a_guardar + "\n")
        if juego.vehiculo.num_ruedas == 4:
            with open(parametros.PATHS["VEHICULOS"][1], "a+", encoding="utf-8") as archivo:
                archivo.write(linea_vehiculo_a_guardar_autr + "\n")
        elif juego.vehiculo.num_ruedas == 2:
            with open(parametros.PATHS["VEHICULOS"][1], "a+", encoding="utf-8") as archivo:
                archivo.write(linea_vehiculo_a_guardar_mobi + "\n")
        with open("juego.csv", "a+", encoding="utf-8") as archivo:
            for i in range(len(juego.contrincantes)):
                archivo.write(juego.contrincantes[i])
        print("Parida Guardada con éxito...")
