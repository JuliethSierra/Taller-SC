import tkinter as tk
from generateNumbers.GenerateNumbers import VentanaGeneracionNumeros
from frogProblem.FrogProblem import FrogProblem
from generateTests.GenerateTests import GenerateTests
from montecarloProblem.MontecarloProblem import MontecarloProblem

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz Gráfica")

        self.boton_generar_numeros = tk.Button(master, text="Generación de números pseudoaleatorios", command=self.generar_numeros_pseudoaleatorios)
        self.boton_generar_numeros.pack()

        self.boton_pruebas = tk.Button(master, text="Pruebas", command=self.pruebas)
        self.boton_pruebas.pack()

        self.boton_problema_rana = tk.Button(master, text="Problema de la rana", command=self.problema_de_la_rana)
        self.boton_problema_rana.pack()

        self.boton_montecarlo = tk.Button(master, text="Montecarlo", command=self.montecarlo)
        self.boton_montecarlo.pack()

    def generar_numeros_pseudoaleatorios(self):
        ventana_generacion = tk.Toplevel(self.master)
        ventana_generacion.title("Generación de números pseudoaleatorios")
        ventana_generacion.geometry("300x200")
        app = VentanaGeneracionNumeros(ventana_generacion)

    def pruebas(self):
        ventana_generacion = tk.Toplevel(self.master)
        ventana_generacion.title("Pruebas")
        ventana_generacion.geometry("300x200")
        app = GenerateTests(ventana_generacion)

    def problema_de_la_rana(self):
        ventana_generacion = tk.Toplevel(self.master)
        ventana_generacion.title("Problema de la rana")
        ventana_generacion.geometry("300x200")
        app = FrogProblem(ventana_generacion)

    def montecarlo(self):
        ventana_generacion = tk.Toplevel(self.master)
        ventana_generacion.title("MontecarloProblem")
        ventana_generacion.geometry("300x200")
        app = MontecarloProblem(ventana_generacion)