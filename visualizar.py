import matplotlib.pyplot as plt
import numpy as np


class Visualizador:
    """Genera las gráficas del campeonato usando matplotlib."""

    # Segundos que cada gráfica queda en pantalla antes de cerrarse sola
    TIEMPO_EN_PANTALLA = 5

    @staticmethod
    def _mostrar_y_cerrar():
        """
        Muestra la gráfica actual sin frenar el programa, la deja en pantalla
        TIEMPO_EN_PANTALLA segundos y la cierra sola.
        (Método auxiliar: lo usan las cuatro gráficas para no repetir código.)
        """
        # block=False: muestra la ventana pero el programa sigue ejecutándose
        plt.show(block=False)
        # pause: mantiene la ventana abierta (y "viva") durante esos segundos
        plt.pause(Visualizador.TIEMPO_EN_PANTALLA)
        # close: cierra la figura, así la siguiente gráfica empieza de cero
        plt.close()

    @staticmethod
    def grafico_promedios(nombres, promedios):
        """
        Gráfica de BARRAS con el promedio de cada jugador.

        Parámetros:
            nombres: nombres de los jugadores.
            promedios: promedio de cada jugador.

        Requisitos:
            - Una barra por jugador.
            - Rotular ambos ejes e incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
        plt.figure(figsize=(8, 5))
        # Una barra por jugador: en X el nombre, en la altura el promedio
        plt.bar(nombres, promedios, color='royalblue', edgecolor='black')
        plt.xlabel('Jugador')
        plt.ylabel('Promedio de puntaje')
        plt.title('Promedio de puntaje por jugador')
        Visualizador._mostrar_y_cerrar()

    @staticmethod
    def grafico_torta(nombres, puntuaciones):
        """
        Gráfica de TORTA con la proporción del puntaje total del campeonato
        que aportó cada jugador.

        Parámetros:
            nombres: nombres de los jugadores.
            puntuaciones: puntajes de los jugadores en cada partida.

        Requisitos:
            - Cada porción debe representar el puntaje total del jugador
              en el campeonato, calculado con NumPy.
            - Cada porción debe llevar el nombre del jugador y su porcentaje.
            - Incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
        # axis=1: suma a lo largo de las columnas -> un total por fila (jugador)
        totales = np.sum(puntuaciones, axis=1)

        plt.figure(figsize=(7, 7))
        # labels: nombre de cada porción / autopct: porcentaje con 1 decimal
        plt.pie(totales, labels=nombres, autopct='%1.1f%%', startangle=90)
        plt.title('Proporción del puntaje total del campeonato por jugador')
        Visualizador._mostrar_y_cerrar()

    @staticmethod
    def grafico_dispersion(nombres, puntuaciones, partidas):
        """
        Gráfica de DISPERSIÓN con todos los puntajes del campeonato:
        en el eje X las partidas y en el eje Y el puntaje obtenido.

        Parámetros:
            nombres: nombres de los jugadores.
            puntuaciones: puntajes de los jugadores en cada partida.
            partidas: nombres de las partidas.

        Requisitos:
            - Los puntos de cada jugador deben distinguirse de los demás.
            - Mostrar una leyenda para identificar a cada jugador.
            - Rotular ambos ejes e incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
        plt.figure(figsize=(9, 5))
        # Un scatter por jugador: cada llamada usa un color distinto
        # y el label es lo que después aparece en la leyenda.
        # puntuaciones[i] es la fila i: los 5 puntajes del jugador i.
        for i in range(len(nombres)):
            plt.scatter(partidas, puntuaciones[i], s=70, label=nombres[i])
        plt.xlabel('Partida')
        plt.ylabel('Puntaje')
        plt.title('Puntajes de cada jugador en cada partida')
        plt.legend(title='Jugador', loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        Visualizador._mostrar_y_cerrar()

    @staticmethod
    def grafico_lineas(nombres, puntuaciones, partidas):
        """
        Gráfica de LÍNEAS con la evolución de cada jugador a lo largo
        de las partidas del campeonato.

        Parámetros:
            nombres: nombres de los jugadores.
            puntuaciones: puntajes de los jugadores en cada partida.
            partidas: nombres de las partidas.

        Requisitos:
            - Una línea por jugador, con un marcador en cada punto.
            - Mostrar una leyenda para identificar a cada jugador.
            - Rotular ambos ejes e incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
        plt.figure(figsize=(9, 5))
        # Una línea por jugador; marker='o' pone un punto en cada partida
        for i in range(len(nombres)):
            plt.plot(partidas, puntuaciones[i], marker='o', label=nombres[i])
        plt.xlabel('Partida')
        plt.ylabel('Puntaje')
        plt.title('Evolución de cada jugador a lo largo del campeonato')
        plt.legend(title='Jugador', loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        Visualizador._mostrar_y_cerrar()
