import random
import numpy as np
import matplotlib.pyplot as plt

# Clase para representar un jugador
class Jugador:
    def __init__(self, genero):
        self.resistencia = random.randint(10, 35)
        self.experiencia = 10
        self.suerte = random.uniform(1, 3)
        self.genero = genero

# Función para simular un lanzamiento
def lanzamiento(jugador):
    if jugador.genero == 'mujer':
        precision = [0.3, 0.68, 0.95, 1.0]  # Probabilidades acumuladas para las categorías de precisión
        puntajes = [10, 9, 8, 0]            # Puntajes correspondientes a cada categoría de precisión
    else:
        precision = [0.2, 0.55, 0.95, 1.0]   # Probabilidades acumuladas para las categorías de precisión
        puntajes = [10, 9, 8, 0]            # Puntajes correspondientes a cada categoría de precisión

    # Generamos un número aleatorio entre 0 y 1 para determinar la categoría de precisión
    random_number = random.random()
    for i in range(len(precision)):
        if random_number <= precision[i]:
            puntaje = puntajes[i]
            break
    return puntaje

# Función para simular una ronda
def ronda(equipo1, equipo2):
    lanzamientos_equipo1 = [lanzamiento(jugador) for jugador in equipo1]
    lanzamientos_equipo2 = [lanzamiento(jugador) for jugador in equipo2]
    puntaje_equipo1 = sum(lanzamientos_equipo1)
    puntaje_equipo2 = sum(lanzamientos_equipo2)

    return puntaje_equipo1, puntaje_equipo2

# Función para determinar al jugador con más suerte en un equipo
def jugador_con_mas_suerte(equipo):
    return max(equipo, key=lambda jugador: jugador.suerte)

# Función para simular un juego
def juego():
    equipo1 = [Jugador('hombre' if i < 3 else 'mujer') for i in range(5)]
    equipo2 = [Jugador('hombre' if i < 3 else 'mujer') for i in range(5)]

    ganador_individual = None

    for _ in range(10):
        puntaje_equipo1, puntaje_equipo2 = ronda(equipo1, equipo2)
        if puntaje_equipo1 > puntaje_equipo2:
            ganador_individual = equipo1
        elif puntaje_equipo1 < puntaje_equipo2:
            ganador_individual = equipo2
        else:
            # Empate, lanzamientos extras
            while puntaje_equipo1 == puntaje_equipo2:
                puntaje_equipo1_extra, puntaje_equipo2_extra = ronda(equipo1, equipo2)
                puntaje_equipo1 += puntaje_equipo1_extra
                puntaje_equipo2 += puntaje_equipo2_extra

    ganador_individual = 'equipo1' if ganador_individual == equipo1 else 'equipo2' if ganador_individual == equipo2 else 'empate'

    return puntaje_equipo1, puntaje_equipo2, jugador_con_mas_suerte(equipo1), jugador_con_mas_suerte(equipo2), ganador_individual

# Función para simular múltiples juegos
def simulacion(num_juegos):
    resultados = {
        'jugador_mas_suerte': [],
        'jugador_mas_experiencia': [],
        'equipo_ganador': [],
        'genero_victorias': {'hombre': 0, 'mujer': 0},
        'puntajes_juego': []
    }

    for _ in range(num_juegos):
        puntaje_equipo1, puntaje_equipo2, jugador_suerte_equipo1, jugador_suerte_equipo2, ganador_individual = juego()

        resultados['puntajes_juego'].append((puntaje_equipo1, puntaje_equipo2))
        resultados['jugador_mas_suerte'].append(jugador_suerte_equipo1 if jugador_suerte_equipo1.suerte > jugador_suerte_equipo2.suerte else jugador_suerte_equipo2)
        resultados['jugador_mas_experiencia'].append(jugador_suerte_equipo1 if jugador_suerte_equipo1.experiencia > jugador_suerte_equipo2.experiencia else jugador_suerte_equipo2)

        # Verificamos si el ganador individual es 'equipo1' o 'equipo2' antes de incrementar su contador en el diccionario
        if ganador_individual in ['equipo1', 'equipo2']:
            resultados['equipo_ganador'].append(ganador_individual)
            if ganador_individual not in resultados['genero_victorias']:
                resultados['genero_victorias'][ganador_individual] = 0
            resultados['genero_victorias'][ganador_individual] += 1
        else:
            resultados['equipo_ganador'].append('empate')

    return resultados


# Función para generar tablas
def mostrar_resultados(resultados):
    print("Resultados de la simulación:")
    print("----------------------------")

    # Tabla de jugador con más suerte
    print("Jugador con más suerte:")
    print("| Juego | Género | Resistencia | Experiencia | Suerte |")
    for i, jugador in enumerate(resultados['jugador_mas_suerte']):
        print(f"| {i+1} | {jugador.genero} | {jugador.resistencia} | {jugador.experiencia} | {jugador.suerte} |")
    print()

    # Tabla de jugador con más experiencia
    print("Jugador con más experiencia:")
    print("| Juego | Género | Resistencia | Experiencia | Suerte |")
    for i, jugador in enumerate(resultados['jugador_mas_experiencia']):
        print(f"| {i+1} | {jugador.genero} | {jugador.resistencia} | {jugador.experiencia} | {jugador.suerte} |")
    print()

    # Tabla de equipo ganador
    print("Equipo ganador:")
    print("| Juego | Ganador | Puntaje Equipo 1 | Puntaje Equipo 2 |")
    for i, ganador in enumerate(resultados['equipo_ganador']):
        print(f"| {i+1} | {ganador} | {resultados['puntajes_juego'][i][0]} | {resultados['puntajes_juego'][i][1]} |")
    print()

    # Género con más victorias
    print("Género con más victorias:")
    print(f"Hombre: {resultados['genero_victorias']['hombre']}")
    print(f"Mujer: {resultados['genero_victorias']['mujer']}")

# Función para graficar los puntajes por juego
def graficar_puntajes(resultados):
    puntajes_equipo1 = [x[0] for x in resultados['puntajes_juego']]
    puntajes_equipo2 = [x[1] for x in resultados['puntajes_juego']]
    juegos = range(1, len(puntajes_equipo1) + 1)

    plt.plot(juegos, puntajes_equipo1, label='Equipo 1', marker='o')
    plt.plot(juegos, puntajes_equipo2, label='Equipo 2', marker='o')
    plt.xlabel('Juego')
    plt.ylabel('Puntaje')
    plt.title('Puntajes por Juego')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Ejecutando")
resultados_simulacion = simulacion(3)
mostrar_resultados(resultados_simulacion)
graficar_puntajes(resultados_simulacion)