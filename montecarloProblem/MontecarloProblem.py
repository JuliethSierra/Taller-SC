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
        print("Resultados")
        game = Game()
        #game.create_teams("team1")
        # Crear equipos
        equipo1 = game.create_teams("Equipo1").players
        equipo2 = game.create_teams("Equipo2").players

        # Ejecutar una ronda y obtener el puntaje del equipo
        resultado_ronda = game.ronda(equipo1, equipo2)

        # Imprimir el resultado de la ronda
        print("El resultado de la ronda es:", resultado_ronda)

        game.finalGame(equipo1, equipo2)