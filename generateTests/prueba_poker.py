import tkinter as tk
from tkinter import ttk
import numpy as np
from collections import Counter


class PruebaPoker:
    @staticmethod
    def prueba_poker(numeros):
        resultado = False
        sumatoria = sum(numeros)
        contador_numeros = Counter(numeros)
        num_valores = len(contador_numeros)

        if num_valores == 5:
            resultado = True
        elif num_valores == 4:
            resultado = "O un par"
        elif num_valores == 3:
            if 2 in contador_numeros.values():
                resultado = "T Dos pares"
            else:
                resultado = "K Tercia"
        elif num_valores == 2:
            if 3 in contador_numeros.values():
                resultado = "Ftercia y par"
            else:
                resultado = "P Cuatro numeros del mismo valor"
        elif num_valores == 1:
            resultado = "Q Cinco del mismo valor"

        return resultado, sumatoria