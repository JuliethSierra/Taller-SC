"""import tkinter as tk

class MontecarloProblem:
    def __init__(self, master):
        self.master = master
        self.master.title("MontecarloProblem")
        self.etiqueta = tk.Label(master, text="MontecarloProblem")
        self.etiqueta.pack()"""
import tkinter as tk
import matplotlib.pyplot as plt
from montecarloProblem.Game import Game

class MontecarloProblem:
    def __init__(self, master):
        self.master = master
        self.master.title("MontecarloProblem")
        self.etiqueta = tk.Label(master, text="MontecarloProblem")
        self.etiqueta.pack()

        print("--------------------------------------------\nResultados")
        game = Game()
        #game.create_teams("team1")
        # Crear equipos
        firstTeam = game.create_teams("Equipo1")
        secondTeam = game.create_teams("Equipo2")

        # Ejecutar una ronda y obtener el puntaje del equipo
        #resultado_ronda = game.round(firstTeam, secondTeam)

        # Imprimir el resultado de la ronda
        #print("El resultado de la ronda es:", resultado_ronda)

        #pl = game.raffleLaunch(firstTeam, secondTeam)
        #print(pl)

        #resultado_juego = game.findWinnerTeam(firstTeam, secondTeam)
        #print("El ganador del juego es:", resultado_juego)

        #individualWinner = game.findIndividualWinner(firstTeam, secondTeam)
        #print("El ganador individual del juego es:", individualWinner)

        resultados = game.simulacion(5, firstTeam, secondTeam)
        print("Resultados: ", resultados)
        game.mostrar_resultados(resultados)
        game.graficar_puntajes(resultados)