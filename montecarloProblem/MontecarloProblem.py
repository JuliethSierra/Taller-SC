import tkinter as tk

class MontecarloProblem:
    def __init__(self, master):
        self.master = master
        self.master.title("MontecarloProblem")
        self.etiqueta = tk.Label(master, text="MontecarloProblem")
        self.etiqueta.pack()