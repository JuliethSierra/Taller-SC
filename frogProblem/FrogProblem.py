import tkinter as tk

class FrogProblem:
    def __init__(self, master):
        self.master = master
        self.master.title("Problema de la rana")
        self.etiqueta = tk.Label(master, text="Problema de la rana")
        self.etiqueta.pack()