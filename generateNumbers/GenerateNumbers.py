import tkinter as tk

class VentanaGeneracionNumeros:
    def __init__(self, master):
        self.master = master
        self.master.title("Generación de números pseudoaleatorios")
        self.etiqueta = tk.Label(master, text="Generación de números pseudoaleatorios")
        self.etiqueta.pack()

