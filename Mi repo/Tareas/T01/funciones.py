from math import floor, ceil
import parametros


def velocidad_real(vel_min, vel_intencional, dif_control, hipotermia):
    vel_min = int(vel_min)
    vel_intencional = int(vel_intencional)
    dif_control = int(dif_control)
    hipotermia = int(hipotermia)
    vel_real = max(vel_min, vel_intencional + dif_control + hipotermia)
    return vel_real


def velocidad_intencional(efecto, vel_recomendada):
    vel_recomendada = int(vel_recomendada)
    if efecto == "precavido":
        vel_intencional = parametros.EFECTO_PRECAVIDO * vel_recomendada
    elif efecto == "osado":
        vel_intencional = parametros.EFECTO_OSADO * vel_recomendada
    return vel_intencional


def velocidad_recomendada(vel_base, ruedas, hielo_p, defensa_carro, rocas_p, exp_pil, dif_pista,
                          ef_hielo, ef_rocas, ef_dificultad):
    vel_base = int(vel_base)
    ruedas = int(ruedas)
    hielo_p = int(hielo_p)
    defensa_carro = int(defensa_carro)
    rocas_p = int(rocas_p)
    exp_pil = int(exp_pil)
    dif_pista = int(dif_pista)
    ef_hielo = int(ef_hielo)
    ef_rocas = int(ef_rocas)
    ef_dificultad = int(ef_dificultad)
    vel_recomendada = vel_base + ((ruedas - hielo_p) * ef_hielo) + \
        (defensa_carro - rocas_p) * ef_rocas + ((exp_pil - dif_pista) * ef_dificultad)
    return vel_recomendada


def efecto_de_la_hipotermia(num_vuelta, contextura_piloto, hielo_pista):
    num_vuelta = int(num_vuelta)
    contextura_piloto = int(contextura_piloto)
    hielo_pista = int(hielo_pista)
    hipotermia = min(0, num_vuelta * (contextura_piloto - hielo_pista))
    return hipotermia


# El codigo se debe encargar de que entre solo si es de 2 ruedas
def dificultad_de_control_del_vehiculo(perso,
                                       equilibrio, equilibrio_efecto, peso_medio, peso_vehiculo):
    equilibrio = int(equilibrio)
    peso_medio = int(peso_medio)
    peso_vehiculo = int(peso_vehiculo)
    if perso == "osado":
        equilibrio_efecto = 1
        dificultad_control = min(0,
                                 equilibrio * equilibrio_efecto - floor(peso_medio / peso_vehiculo))
    elif perso == "precavido":
        dificultad_control = min(0,
                                 equilibrio * equilibrio_efecto - floor(peso_medio / peso_vehiculo))
    return dificultad_control


def dano_al_vehiculo(defensa_carroceria, rocas_pista):
    defensa_carroceria = int(defensa_carroceria)
    rocas_pista = int(rocas_pista)
    dano_recibido_cada_vuelta = max(0, rocas_pista - defensa_carroceria)
    return dano_recibido_cada_vuelta


def tiempo_en_los_pits(tiempo_min_pits, durabilidad_ini_chasis, durabilidad_act_chasis, vel_pits):
    tiempo_min_pits = int(tiempo_min_pits)
    durabilidad_ini_chasis = int(durabilidad_ini_chasis)
    durabilidad_act_chasis = int(durabilidad_act_chasis)
    vel_pits = int(vel_pits)
    tiempo_pits = tiempo_min_pits + (durabilidad_ini_chasis - durabilidad_act_chasis) * vel_pits
    return tiempo_pits


def dinero_por_vuelta(numero_vuelta, dificultad_pista):
    numero_vuelta = int(numero_vuelta)
    dificultad_pista = int(dificultad_pista)
    dinero_vuelta_x = numero_vuelta * dificultad_pista
    return dinero_vuelta_x


def accidentes_durante_las_vueltas(vel_real, vel_rec, dura_max_chasis, dura_act_chasis):
    vel_real = int(vel_real)
    vel_rec = int(vel_rec)
    dura_max_chasis = int(dura_max_chasis)
    dura_act_chasis = int(dura_act_chasis)
    probabilidad_accidente = min(1, max(0, (vel_real - vel_rec) / vel_rec) +
                                 floor((dura_max_chasis - dura_act_chasis) / dura_max_chasis))
    return probabilidad_accidente


def tiempo_por_vuelta(largo_pista, vel_real):
    largo_pista = int(largo_pista)
    vel_real = int(vel_real)
    tiempo_vuelta = ceil(largo_pista/vel_real)
    return tiempo_vuelta


def dinero_por_ganar(num_vueltas_total, dif_pista, hielo_pista, rocas_pista):
    num_vueltas_total = int(num_vueltas_total)
    dif_pista = int(dif_pista)
    hielo_pista = int(hielo_pista)
    rocas_pista = int(rocas_pista)
    dinero_ganador = num_vueltas_total * (dif_pista + hielo_pista + rocas_pista)
    return dinero_ganador


def ventaja_con_ultimo_lugar(tiempo_ultimo_lugar, tiempo_primer_lugar):
    tiempo_primer_lugar = int(tiempo_primer_lugar)
    tiempo_ultimo_lugar = int(tiempo_ultimo_lugar)
    ventaja = tiempo_ultimo_lugar - tiempo_primer_lugar
    return ventaja


# Es importante que el main llame al bono perso, por la perso del piloto
def experiencia_por_ganar(vent_con_ultimo_lug, dificultad_pista, bono_personalidad):
    vent_con_ultimo_lug = int(vent_con_ultimo_lug)
    dificultad_pista = int(dificultad_pista)
    bono_personalidad = int(bono_personalidad)
    experiencia_recibida = (vent_con_ultimo_lug + dificultad_pista) * bono_personalidad
    return experiencia_recibida


def buscar_nombre(lista_archivo):
    lista_nombres_archivo = []
    for i in range(len(lista_archivo)):
        for j in range(len(lista_archivo[i])):
            if lista_archivo[0][j] == "Nombre":
                lista_nombres_archivo.append(lista_archivo[i][j])
    return lista_nombres_archivo


def buscar_num_vueltas(lista_archivo):
    lista_vueltas_archivo = []
    for i in range(len(lista_archivo)):
        for j in range(len(lista_archivo[i])):
            if lista_archivo[0][j] == "NúmeroVueltas":
                lista_vueltas_archivo.append(lista_archivo[i][j])
    return lista_vueltas_archivo


def buscar_tipo_pista(lista_archivo):
    lista_pistas_archivo = []
    for i in range(len(lista_archivo)):
        for j in range(len(lista_archivo[i])):
            if lista_archivo[0][j] == "Tipo":
                lista_pistas_archivo.append(lista_archivo[i][j])
    return lista_pistas_archivo


def ordenar_columnas_archivo(lista_archivo):
    linea_orden = lista_archivo[0]
    diccionario_orden = {}
    for i in range(len(linea_orden)):
        diccionario_orden[linea_orden[i]] = i
    return diccionario_orden


def condiciones_compra_vehiculo(opciones, juego):
    precio_auto = 400
    precio_tronco = 300
    precio_moto = 250
    precio_bici = 200
    print()
    if opciones == "1" and juego.jugador.dinero >= precio_auto:
        return "1"
    elif opciones == "2" and juego.jugador.dinero >= precio_tronco:
        return "1"
    elif opciones == "3" and juego.jugador.dinero >= precio_moto:
        return "1"
    elif opciones == "4" and juego.jugador.dinero >= precio_bici:
        return "1"
    elif opciones == "0":
        return "0"
    elif opciones == "1" and juego.jugador.dinero < precio_auto:
        print("No tienes dinero suficiente para comprar este vehículo...")
        return "2"
    elif opciones == "2" and juego.jugador.dinero < precio_tronco:
        print("No tienes dinero suficiente para comprar este vehículo...")
        return "2"
    elif opciones == "3" and juego.jugador.dinero < precio_moto:
        print("No tienes dinero suficiente para comprar este vehículo...")
        return "2"
    elif opciones == "4" and juego.jugador.dinero < precio_bici:
        print("No tienes dinero suficiente para comprar este vehículo...")
        return "2"
    else:
        print("Ingrese una opción válida por favor...")
        return "2"
