import numpy as np


class Campeonato:
    """Coordina jugadores y partidas, y calcula las estadísticas del campeonato."""

    def __init__(self, nombres_jugadores, puntaje_jugadores, partidas):
        """
        Parámetros:
            nombres_jugadores: nombres de los jugadores.
            puntaje_jugadores: puntajes de los jugadores en cada partida.
            partidas: nombres de las partidas.
        """
        self.puntaje_jugadores = puntaje_jugadores
        self.partidas = partidas
        self.nombres_jugadores = nombres_jugadores

    def promedio_general(self):
        """
        Retorna el promedio de todos los puntajes del campeonato.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
        """
        # Sin axis, mean() promedia todos los elementos de la matriz
        return self.puntaje_jugadores.mean()

    def mejor_jugador(self):
        """
        Retorna el nombre del jugador con el promedio más alto
        y el valor de ese promedio.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
            - Retornar ambos valores juntos: nombre y promedio.
        """
        promedios = self.promedios_por_jugador()
        indice = promedios.argmax()  # posición del promedio más alto
        return self.nombres_jugadores[indice], promedios[indice]

    def peor_jugador(self):
        """
        Retorna el nombre del jugador con el promedio más bajo
        y el valor de ese promedio.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
            - Retornar ambos valores juntos: nombre y promedio.
        """
        promedios = self.promedios_por_jugador()
        indice = promedios.argmin()  # posición del promedio más bajo
        return self.nombres_jugadores[indice], promedios[indice]

    def promedios_por_jugador(self):
        """
        Retorna el promedio de cada jugador en el campeonato,
        en el mismo orden en que aparecen los nombres.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
        """
        # axis=1: promedia a lo largo de las columnas, uno por cada fila (jugador)
        return self.puntaje_jugadores.mean(axis=1)

    def promedios_por_partida(self):
        """
        Retorna el promedio de cada partida del campeonato,
        en el mismo orden en que aparecen las partidas.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
        """
        # axis=0: promedia a lo largo de las filas, uno por cada columna (partida)
        return self.puntaje_jugadores.mean(axis=0)

    # ------------------------------------------------------------------
    # INVESTIGACIÓN: dos métodos de NumPy que no se hayan visto en clase
    # ------------------------------------------------------------------
    def estadistica_investigada_1(self):
        """
        Mediana de los puntajes de cada partida.

        Retorna un array con la mediana de cada partida.
        """
        # np.median devuelve el valor central de los datos una vez ordenados.
        # Con axis=0 se calcula una mediana por cada columna (partida).
        # Aporta información sobre el campeonato: muestra el rendimiento
        # "típico" de cada partida sin que lo distorsionen puntajes
        # extremos (un jugador muy bueno o muy malo). Si la mediana difiere
        # mucho del promedio de esa partida, hay valores atípicos.
        return np.median(self.puntaje_jugadores, axis=0)

    def estadistica_investigada_2(self):
        """
        Jugador más irregular: el de mayor diferencia entre su mejor
        y su peor puntaje.

        Retorna una tupla (nombre, rango).
        """
        # np.ptp ("peak to peak") devuelve máximo - mínimo. Con axis=1 se
        # calcula una vez por cada fila (jugador).
        # Aporta información sobre el campeonato: mide qué tan irregular fue
        # cada jugador. Un rango chico indica un rendimiento constante y uno
        # grande, un jugador con partidas muy buenas y otras muy malas.
        # Se usa argmax sobre los rangos para identificar al más irregular.
        rangos = np.ptp(self.puntaje_jugadores, axis=1)
        indice = rangos.argmax()
        return self.nombres_jugadores[indice], rangos[indice]