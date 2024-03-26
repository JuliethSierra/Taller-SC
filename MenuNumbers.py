import tkinter as tk

from generateNumbers.DistribuicionUniforme import GUIU
from generateNumbers.CuadradosMedios import GUIM
from generateNumbers.DistribuicionNormal import GUIN
from generateNumbers.Congruenciales import GUIC

class MenuNumbers:
    def __init__(self, master):
        self.master = master
        self.master.title("Generacion de numeros")

        self.boton_cuadrados_medios = tk.Button(master, text="Metodo Cuadrados Medios", command=self.cuadrados_medios)
        self.boton_cuadrados_medios.pack()

        self.boton_congruenciales = tk.Button(master, text="Metodo Congruenciales", command=self.cogruenciales)
        self.boton_congruenciales.pack()

        self.boton_distribuicion_uniforme = tk.Button(master, text="Metodo distribuicion uniforme", command=self.distribuicion_uniforme)
        self.boton_distribuicion_uniforme.pack()

        self.boton_distribuicion_normal = tk.Button(master, text="Metodo distribuicion normal", command=self.distribuicion_normal)
        self.boton_distribuicion_normal.pack()
        
    def cuadrados_medios(self):
        app = GUIM()
    
    def cogruenciales(self):
        app = GUIC()
    
    def distribuicion_uniforme(self):
        app = GUIU()
    
    def distribuicion_normal(self):
        app = GUIN()

