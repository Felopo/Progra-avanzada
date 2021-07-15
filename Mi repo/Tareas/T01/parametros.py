from random import choice


AUTOMOVIL = {
    'CHASIS': {
        'MIN': 40,
        'MAX': 100
    },
    'CARROCERIA': {
        'MIN': 40,
        'MAX': 100
    },
    'RUEDAS': {
        'MIN': 10,
        'MAX': 50
    },
    'MOTOR': {
        'MIN': 20,
        'MAX': 100
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 0
    },
    'PESO': {
        'MIN': 150,
        'MAX': 250
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 40,
        'MAX': 100
    },
    'CARROCERIA': {
        'MIN': 40,
        'MAX': 100
    },
    'RUEDAS': {
        'MIN': 10,
        'MAX': 50
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 0
    },
    'ZAPATILLAS': {
        'MIN': 10,
        'MAX': 50
    },
    'PESO': {
        'MIN': 150,
        'MAX': 200   # Un poco menos que el automovil porque este no tiene motor
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 20,
        'MAX': 50
    },
    'CARROCERIA': {
        'MIN': 20,
        'MAX': 50
    },
    'RUEDAS': {
        'MIN': 10,
        'MAX': 40
    },
    'MOTOR': {
        'MIN': 30,
        'MAX': 200
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 0
    },
    'PESO': {
        'MIN': 50,
        'MAX': 100
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 10,
        'MAX': 50
    },
    'CARROCERIA': {
        'MIN': 20,
        'MAX': 35
    },
    'RUEDAS': {
        'MIN': 10,
        'MAX': 40
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 0
    },
    'ZAPATILLAS': {
        'MIN': 10,
        'MAX': 45
    },
    'PESO': {
        'MIN': 10,
        'MAX': 50
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 100,
        'EFECTO': 30
    },
    'CARROCERIA': {
        'COSTO': 50,
        'EFECTO': 30
    },
    'RUEDAS': {
        'COSTO': 20,
        'EFECTO': 10
    },
    'MOTOR': {
        'COSTO': 200,
        'EFECTO': 50
    },
    'ZAPATILLAS': {
        'COSTO': 100,
        'EFECTO': 30
    }
}


# Características de los pilotos de los diferentes equipos
EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': "precavido"
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': choice(["osado", "precavido"])
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': "osado"
    }
}


# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = 10

# Velocidad intencional
EFECTO_OSADO = 20
EFECTO_PRECAVIDO = 15

# Dificultad de control del vehículo
PESO_MEDIO = 30
EQUILIBRIO_PRECAVIDO = 2

# Tiempo pits
TIEMPO_MINIMO_PITS = 10
VELOCIDAD_PITS = 2

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 1
DESBONIFICACION_OSADO = 1/2

# Correcciones enunciado
POUND_EFECT_HIELO = 2
POUND_EFECT_ROCAS = 2
POUND_EFECT_DIFICULTAD = 2
NUMERO_CONTRINCANTES = 3

# Paths de los archivos

PATHS = {
    'PISTAS': ["T01", "pistas.csv"],
    'CONTRINCANTES': ["T01", "contrincantes.csv"],
    'PILOTOS': ["T01", "pilotos.csv"],
    'VEHICULOS': ["T01", "vehículos.csv"]
}


# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
