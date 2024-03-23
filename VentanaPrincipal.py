import tkinter as tk
from MenuNumbers import MenuNumbers
from frogProblem.FrogProblem import FrogProblem
from generateTests.GenerateTests import GenerateTests
from montecarloProblem.MontecarloProblem import MontecarloProblem


class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz Gráfica")

        self.boton_generar_numeros = tk.Button(master, text="Generación de números pseudoaleatorios", command=self.menu_numbers)
        self.boton_generar_numeros.pack()

        self.boton_pruebas = tk.Button(master, text="Pruebas", command=self.pruebas)
        self.boton_pruebas.pack()

        self.boton_problema_rana = tk.Button(master, text="Problema de la rana", command=self.problema_de_la_rana)
        self.boton_problema_rana.pack()

        self.boton_montecarlo = tk.Button(master, text="Montecarlo", command=self.montecarlo)
        self.boton_montecarlo.pack()

        self.ventana_problema_rana = None

    def menu_numbers(self):
        ventana_generacion = tk.Toplevel(self.master)
        ventana_generacion.title("Menu Numeros Pseudoaleatorios")
        ventana_generacion.geometry("300x200")
        app = MenuNumbers(ventana_generacion)

    def pruebas(self):
        ventana_generacion = tk.Toplevel(self.master)
        ventana_generacion.title("Pruebas")
        ventana_generacion.geometry("300x200")
        app = GenerateTests(ventana_generacion)

    def problema_de_la_rana(self):
        if self.ventana_problema_rana is None or not self.ventana_problema_rana.winfo_exists():
            self.master.iconify()
            self.ventana_problema_rana = tk.Toplevel()
            self.ventana_problema_rana.title("Problema de la rana")
            self.ventana_problema_rana.geometry("300x200")
            app = FrogProblem(self.ventana_problema_rana, self.master)

    def montecarlo(self):
        ventana_generacion = tk.Toplevel(self.master)
        ventana_generacion.title("MontecarloProblem")
        ventana_generacion.geometry("300x200")
        app = MontecarloProblem(ventana_generacion)

    def mostrar_ventana_principal(self):
        if self.ventana_problema_rana:
            self.ventana_problema_rana.destroy()
            self.ventana_problema_rana = None
        self.master.deiconify()