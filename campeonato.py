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
    def puntajes_unicos(self):
        """
        Devuelve un array con todos los puntajes 
        diferentes que aparecen en el campeonato, sin repetirlos.
        """
        return np.unique(self.puntaje_jugadores)

    def rango_puntaje(self):
        """
        Identifica al jugador con mayor diferencia entre su puntaje
        más alto y más bajo.

        También informa sus puntajes extremos y su evolución
        a lo largo del campeonato.

        """
        # np.ptp ("peak to peak") devuelve máximo - mínimo. Con axis=1 se
        # calcula una vez por cada fila (jugador).
        # Aporta información sobre el campeonato: mide qué tan irregular fue
        # cada jugador. Un rango chico indica un rendimiento constante y uno
        # grande, un jugador con partidas muy buenas y otras muy malas.
        # Se usa argmax sobre los rangos para identificar al más irregular.
        
        rangos = np.ptp(self.puntaje_jugadores, axis=1)
        indice = rangos.argmax()

        nombre = self.nombres_jugadores[indice]

        puntajes = self.puntaje_jugadores[indice]
        puntaje_minimo = np.min(puntajes)
        puntaje_maximo = np.max(puntajes)

        primer_puntaje = puntajes[0]
        ultimo_puntaje = puntajes[-1]

        if ultimo_puntaje > primer_puntaje:
            evolucion = "Mostró una mejora a lo largo del campeonato."
        elif ultimo_puntaje < primer_puntaje:
            evolucion = "Su rendimiento empeoró a lo largo del campeonato."
        else:
            evolucion = "Mantuvo el mismo puntaje entre la primera y la última partida."

        rango = rangos[indice]

        return (
            f"  Jugador con mayor variación de puntajes: {nombre}\n"
            f"  Puntaje más bajo: {puntaje_minimo}\n"
            f"  Puntaje más alto: {puntaje_maximo}\n"
            f"  Evolución: {evolucion}\n"
            f"  Rango de puntajes: {rango} puntos \n"
        )