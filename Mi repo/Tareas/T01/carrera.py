import funciones
import parametros
import random
import entidades


class Contrincante:
    def __init__(self, nombre, nivel, perso, contextura, eq, exp, equipo, vehiculo):
        self.nombre = nombre
        self.nivel = nivel
        self.personalidad = perso
        self.contextura = contextura
        self.equilibrio = eq
        self.experiencia = exp
        self.equipo = equipo
        self.vehiculo = vehiculo
        self.dict_contrincantes_ord = None
        self.exploto = False
        self.tiempo = None

    def guardar_contrincante(self, dict_ord):
        lista_orden = []
        for i in range(len(dict_ord)):
            if dict_ord["Nombre"] == i:
                lista_orden.append(self.nombre)
            elif dict_ord["Nivel"] == i:
                lista_orden.append(self.nivel)
            elif dict_ord["Personalidad"] == i:
                lista_orden.append(self.personalidad)
            elif dict_ord["Contextura"] == i:
                lista_orden.append(self.contextura)
            elif dict_ord["Equilibrio"] == i:
                lista_orden.append(self.equilibrio)
            elif dict_ord["Experiencia"] == i:
                lista_orden.append(self.experiencia)
            elif dict_ord["Equipo"] == i:
                if self.equipo == "Híbridos":
                    lista_orden.append("Hibridos")
                else:
                    lista_orden.append(self.equipo)
        lista_orden = map(lambda x: str(x), lista_orden)
        string_datos_contrincante = ",".join(lista_orden)
        with open("juego.csv", "a+") as archivo:
            archivo.write(string_datos_contrincante + "\n")


class Carrera:
    def __init__(self, juego):
        self.juego = juego
        self.contrincantes = []

    def agregar_contrincantes(self):
        contrincantes = []
        with open(parametros.PATHS["CONTRINCANTES"][1], "r+", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip().split(",")
                contrincantes.append(linea)
        nombre_contrincantes = funciones.buscar_nombre(contrincantes)
        dict_contrincantes_ord = funciones.ordenar_columnas_archivo(contrincantes)
        contrincantes = contrincantes[1:]
        nuevo_contrincante = 0
        for i in range(len(self.juego.pista.contrincantes[1:])):
            for j in range(len(nombre_contrincantes)):
                if self.juego.pista.contrincantes[i] == nombre_contrincantes[j]:
                    vehiculo_al_azar = random.choice(["Automovil", "Troncomovil", "Bicicleta",
                                                      "Motocicleta"])
                    if vehiculo_al_azar == "Automovil":
                        d_c_o = dict_contrincantes_ord
                        nuevo_contrincante = Contrincante(
                            nombre=contrincantes[i][d_c_o["Nombre"]],
                            nivel=contrincantes[i][d_c_o["Nivel"]],
                            perso=contrincantes[i][d_c_o["Personalidad"]],
                            contextura=int(contrincantes[i][d_c_o["Contextura"]]),
                            eq=int(contrincantes[i][d_c_o["Equilibrio"]]),
                            exp=int(contrincantes[i][d_c_o["Experiencia"]]),
                            equipo=contrincantes[i][d_c_o["Equipo"]],
                            vehiculo=entidades.Automovil(nombre=f"Contrincante{i}",
                                                         dueno=contrincantes[i][d_c_o["Nombre"]]))
                        nuevo_contrincante.dict_contrincantes_ord = d_c_o
                        self.juego.agregar_contrincante(nuevo_contrincante)
                    elif vehiculo_al_azar == "Troncomovil":
                        d_c_o = dict_contrincantes_ord
                        nuevo_contrincante = Contrincante(
                            nombre=contrincantes[i][d_c_o["Nombre"]],
                            nivel=contrincantes[i][d_c_o["Nivel"]],
                            perso=contrincantes[i][d_c_o["Personalidad"]],
                            contextura=int(contrincantes[i][d_c_o["Contextura"]]),
                            eq=int(contrincantes[i][d_c_o["Equilibrio"]]),
                            exp=int(contrincantes[i][d_c_o["Experiencia"]]),
                            equipo=contrincantes[i][d_c_o["Equipo"]],
                            vehiculo=entidades.Troncomovil(nombre=f"Contrincante{i}",
                                                           dueno=contrincantes[i][d_c_o["Nombre"]]))
                        nuevo_contrincante.dict_contrincantes_ord = d_c_o
                        self.juego.agregar_contrincante(nuevo_contrincante)
                    elif vehiculo_al_azar == "Motocicleta":
                        d_c_o = dict_contrincantes_ord
                        nuevo_contrincante = Contrincante(
                            nombre=contrincantes[i][d_c_o["Nombre"]],
                            nivel=contrincantes[i][d_c_o["Nivel"]],
                            perso=contrincantes[i][d_c_o["Personalidad"]],
                            contextura=int(contrincantes[i][d_c_o["Contextura"]]),
                            eq=int(contrincantes[i][d_c_o["Equilibrio"]]),
                            exp=int(contrincantes[i][d_c_o["Experiencia"]]),
                            equipo=contrincantes[i][d_c_o["Equipo"]],
                            vehiculo=entidades.Motocicleta(nombre=f"Contrincante{i}",
                                                           dueno=contrincantes[i][d_c_o["Nombre"]]))
                        nuevo_contrincante.dict_contrincantes_ord = d_c_o
                        self.juego.agregar_contrincante(nuevo_contrincante)
                    elif vehiculo_al_azar == "Bicicleta":
                        d_c_o = dict_contrincantes_ord
                        nuevo_contrincante = Contrincante(
                            nombre=contrincantes[i][d_c_o["Nombre"]],
                            nivel=contrincantes[i][d_c_o["Nivel"]],
                            perso=contrincantes[i][d_c_o["Personalidad"]],
                            contextura=int(contrincantes[i][d_c_o["Contextura"]]),
                            eq=int(contrincantes[i][d_c_o["Equilibrio"]]),
                            exp=int(contrincantes[i][d_c_o["Experiencia"]]),
                            equipo=contrincantes[i][d_c_o["Equipo"]],
                            vehiculo=entidades.Bicicleta(nombre=f"Contrincante{i}",
                                                         dueno=contrincantes[i][d_c_o["Nombre"]]))
                        nuevo_contrincante.dict_contrincantes_ord = d_c_o
                        self.juego.agregar_contrincante(nuevo_contrincante)
        if nuevo_contrincante != 0:
            nuevo_contrincante.guardar_contrincante(dict_contrincantes_ord)
        else:
            print("No hay contrincantes para esta pista...")
        return self.juego

    num_vuelta = 0
    tiempo_acumulado = 0

    def vuelta(self):
        jugadores = []
        lista_pil_des = []
        vehiculo_p = self.juego.vehiculo
        piloto_p = self.juego.jugador
        pista = self.juego.pista
        if vehiculo_p.num_ruedas == 4:
            velocidad_recomendada_p = funciones.velocidad_recomendada(
                vehiculo_p._motor, vehiculo_p._ruedas, pista.hielo, vehiculo_p._carroceria,
                pista.rocas, piloto_p.experiencia, pista.dificultad, parametros.POUND_EFECT_HIELO,
                parametros.POUND_EFECT_ROCAS, parametros.POUND_EFECT_DIFICULTAD)
            velocidad_intencional_p = funciones.velocidad_intencional(piloto_p.personalidad,
                                                                      velocidad_recomendada_p)
            hipotermia = funciones.efecto_de_la_hipotermia(self.num_vuelta, piloto_p.contextura,
                                                           pista.hielo)
            dif_control = 0
            velocidad_real_p = funciones.velocidad_real(
                parametros.VELOCIDAD_MINIMA, velocidad_intencional_p, dif_control, hipotermia)
            accidente = funciones.accidentes_durante_las_vueltas(
                velocidad_real_p, velocidad_recomendada_p, parametros.AUTOMOVIL["CHASIS"]["MAX"],
                vehiculo_p._chasis, )
            if random.random() >= accidente:
                piloto_descalificado = self.accidente(piloto_p)
                lista_pil_des.append(piloto_descalificado)
        elif vehiculo_p.num_ruedas == 2:
            velocidad_recomendada_p = funciones.velocidad_recomendada(
                vehiculo_p._zapatillas, vehiculo_p._ruedas, pista.hielo, vehiculo_p._carroceria,
                pista.rocas, piloto_p.experiencia, pista.dificultad, parametros.POUND_EFECT_HIELO,
                parametros.POUND_EFECT_ROCAS, parametros.POUND_EFECT_DIFICULTAD)
            velocidad_intencional_p = funciones.velocidad_intencional(piloto_p.personalidad,
                                                                      velocidad_recomendada_p)
            hipotermia = funciones.efecto_de_la_hipotermia(self.num_vuelta, piloto_p.contextura,
                                                           pista.hielo)
            dif_control = funciones.dificultad_de_control_del_vehiculo(
                piloto_p.personalidad, piloto_p.equilibrio, parametros.EQUILIBRIO_PRECAVIDO,
                parametros.PESO_MEDIO, vehiculo_p.peso)
            velocidad_real_p = funciones.velocidad_real(
                parametros.VELOCIDAD_MINIMA, velocidad_intencional_p, dif_control, hipotermia)
            accidente = funciones.accidentes_durante_las_vueltas(
                velocidad_real_p, velocidad_recomendada_p, parametros.BICICLETA["CHASIS"]["MAX"],
                vehiculo_p._chasis, )
            if random.random() >= accidente:
                piloto_descalificado = self.accidente(piloto_p)
                lista_pil_des.append(piloto_descalificado)
        tiempo_vuelta = funciones.tiempo_por_vuelta(
            pista.largo_pista, velocidad_real_p)
        self.tiempo_acumulado += tiempo_vuelta
        piloto_p.tiempo = tiempo_vuelta
        jugadores.append(piloto_p)
        for i in range(len(self.contrincantes)):
            if self.contrincantes[i].vehiculo.num_ruedas == 2:
                velocidad_recomendada_c = funciones.velocidad_recomendada(
                                          self.contrincantes[i].vehiculo._zapatillas,
                                          self.contrincantes[i].vehiculo._ruedas,
                                          pista.hielo, self.contrincantes[i].vehiculo._carroceria,
                                          pista.rocas, self.contrincantes[i].experiencia,
                                          pista.dificultad, parametros.POUND_EFECT_HIELO,
                                          parametros.POUND_EFECT_ROCAS,
                                          parametros.POUND_EFECT_DIFICULTAD)
                velocidad_intencional_c = funciones.velocidad_intencional(
                    self.contrincantes[i].personalidad, velocidad_recomendada_c)
                hipotermia_c = funciones.efecto_de_la_hipotermia(self.num_vuelta,
                                                                self.contrincantes[i].contextura,
                                                                 )
                dif_control_c = funciones.dificultad_de_control_del_vehiculo(
                    self.contrincantes[i].personalidad, self.contrincantes[i].equilibrio,
                    parametros.EQUILIBRIO_PRECAVIDO, parametros.PESO_MEDIO,
                    self.contrincantes[i].vehiculo.peso)
                velocidad_real_c = funciones.velocidad_real(
                    parametros.VELOCIDAD_MINIMA, velocidad_intencional_c, dif_control_c,
                    hipotermia_c,)
                accidente_c = funciones.accidentes_durante_las_vueltas(
                    velocidad_real_c, velocidad_recomendada_c,
                    parametros.BICICLETA["CHASIS"]["MAX"], vehiculo_p._chasis, )
                if random.random() >= accidente_c:
                    piloto_descalificado = self.accidente(self.contrincantes[i])
                    lista_pil_des.append(piloto_descalificado)
            elif self.contrincantes[i].vehiculo.num_ruedas == 4:
                velocidad_recomendada_c = funciones.velocidad_recomendada(
                    self.contrincantes[i].vehiculo._motor,
                    self.contrincantes[i].vehiculo._ruedas,
                    pista.hielo, self.contrincantes[i].vehiculo._carroceria,
                    pista.rocas, self.contrincantes[i].experiencia,
                    pista.dificultad, parametros.POUND_EFECT_HIELO,
                    parametros.POUND_EFECT_ROCAS,
                    parametros.POUND_EFECT_DIFICULTAD)
                velocidad_intencional_c = funciones.velocidad_intencional(
                    self.contrincantes[i].personalidad, velocidad_recomendada_c)
                hipotermia_c = funciones.efecto_de_la_hipotermia(self.num_vuelta,
                                                                 self.contrincantes[i].contextura,
                                                                 pista.hielo)
                dif_control_c = 0
                velocidad_real_c = funciones.velocidad_real(
                    parametros.VELOCIDAD_MINIMA, velocidad_intencional_c, dif_control_c,
                    hipotermia_c, )
                accidente_c = funciones.accidentes_durante_las_vueltas(
                    velocidad_real_c, velocidad_recomendada_c,
                    parametros.AUTOMOVIL["CHASIS"]["MAX"], vehiculo_p._chasis, )
                if random.random() >= accidente_c:
                    piloto_descalificado = self.accidente(self.contrincantes[i])
                    lista_pil_des.append(piloto_descalificado)
            tiempo_vuelta_c = funciones.tiempo_por_vuelta(
                pista.largo_pista, velocidad_real_c)
            self.contrincantes[i].tiempo = tiempo_vuelta_c
            jugadores.append(self.contrincantes[i])
        print(f"Vuelta: {str(self.num_vuelta)} de {str(pista.numero_vueltas)} \n"
              f" \n"
              f"Tu velocidad no se vió afectada durante la vuelta. \n"
              f" \n"
              f"Orden de los competidores:")
        jugadores.sort(key=lambda x: x.tiempo)
        print("")
        for i in range(len(jugadores)):
            print(f"{str(i)}) {jugadores[i].nombre} {str(jugadores[i].tiempo)}")
        print("Competidores descalificados:")
        for i in range(len(lista_pil_des)):
            print(f"- {lista_pil_des[i]}")
        if piloto_p.nombre == jugadores[0]:
            dinero_p_vuelta = funciones.dinero_por_vuelta(self.num_vuelta, pista.dificultad)
            piloto_p.dinero += dinero_p_vuelta
        else:
            for i in range(len(self.contrincantes)):
                if self.contrincantes[i].nombre == jugadores[0]:
                    dinero_por_vuelta = funciones.dinero_por_vuelta(
                        self.num_vuelta, pista.dificultad)
                    self.contrincantes[i].dinero += dinero_por_vuelta
        return self.juego

    def accidente(self, piloto):
        if "Contrincante" not in piloto.nombre:
            self.juego.vehiculo._chasis = 0
            print("Tu chasis explotó, te tendrás que retirar de la carrera")
            print("Volviendo al menú principal")
        else:
            piloto.vehiculo._chasis = 0
            piloto.exploto = True
        return piloto.nombre
