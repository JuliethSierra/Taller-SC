import tkinter as tk

class GenerateTests:
    def __init__(self, master):
        self.master = master
        self.master.title("Pruebas")
        self.etiqueta = tk.Label(master, text="Pruebas")
        self.etiqueta.pack()