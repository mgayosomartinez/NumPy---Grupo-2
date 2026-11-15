import numpy as np
from repositorio import RepositorioCSV
from visualizar import Visualizador
from campeonato import Campeonato
from jugador import Jugador

# ---------------------------------------------------------------
# Lectura del archivo
# ---------------------------------------------------------------
nombres_jugadores, puntuaciones_jugadores, partidas = RepositorioCSV.cargar_campeonato('campeones/Campeonato.csv')
print("Nombres de jugadores:", nombres_jugadores)
print("Puntuaciones de jugadores:\n", puntuaciones_jugadores)
print("Partidas:", partidas)

# ---------------------------------------------------------------
# Estadísticas del campeonato
# ---------------------------------------------------------------
campeonato = Campeonato(nombres_jugadores, puntuaciones_jugadores, partidas)

campeon, puntaje_mejor = campeonato.mejor_jugador()
print(f"\nEl mejor jugador es {campeon} con un promedio de {puntaje_mejor}")

nombre_peor, puntaje_peor = campeonato.peor_jugador()
print(f"El peor jugador es {nombre_peor} con un promedio de {puntaje_peor}")

print(f"Promedio del campeonato: {campeonato.promedio_general()}")

print(f"Promedio por partida: {campeonato.promedios_por_partida()}\n")

# ---------------------------------------------------------------
# Métodos de NumPy investigados
# ---------------------------------------------------------------
print(f"Puntajes diferentes: {campeonato.puntajes_unicos()} \n")
print('Analisis Regularidad')
print(campeonato.rango_puntaje())

# ---------------------------------------------------------------
# Gráficas
# ---------------------------------------------------------------
Visualizador.grafico_promedios(nombres_jugadores, campeonato.promedios_por_jugador())
Visualizador.grafico_torta(nombres_jugadores, puntuaciones_jugadores)
Visualizador.grafico_dispersion(nombres_jugadores, puntuaciones_jugadores, partidas)
Visualizador.grafico_lineas(nombres_jugadores, puntuaciones_jugadores, partidas)

# ---------------------------------------------------------------
# Crear un jugador a partir de los datos del campeonato
# ---------------------------------------------------------------
print('Creacion jugador:')
nombre_buscado = "Ana"

# np.where devuelve los índices donde se cumple la condición;
# [0] toma el array de índices (filas) y [0] el primero, que es la ubicación
ubicacion = np.where(nombres_jugadores == nombre_buscado)[0][0]
print(f'    Ubicacion en array de jugadores:{ubicacion}')
puntuaciones_buscado = puntuaciones_jugadores[ubicacion]
jugador1 = Jugador(nombre_buscado, puntuaciones_buscado)
print(f'    Jugador creado:{jugador1.get_nombre()}')
print(f'    Promedio:{jugador1.promedio()}')