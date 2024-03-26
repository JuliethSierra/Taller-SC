from pruebas_estadisticas import PruebasEstadisticas
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt


class Chi2Handler:
    def __init__(self, master, numeros, intervalo, mostrar_proceso, mostrar_grafico):
        self.master = master
        self.numeros = numeros
        self.intervalo = intervalo
        self.mostrar_proceso = mostrar_proceso
        self.mostrar_grafico = mostrar_grafico


    def mostrar_resultados(self):
        if self.intervalo:
            intervalo_min = int(self.intervalo[0])
            intervalo_max = int(self.intervalo[1])


            # Filtrar los datos dentro del intervalo
            conjunto_filtrado = self.numeros[intervalo_min:intervalo_max]


            # Calcular los intervalos
            intervalos = PruebasEstadisticas.dividir_en_intervalos(conjunto_filtrado)


            if self.mostrar_proceso:
                tabla = PrettyTable()
                tabla.field_names = ["Ni", "Ri", "Número de dato", "Dato inicial", "Dato final", "Frecuencia obtenida",
                                    "Frecuencia esperada", "Chi cuadrado", "Número mínimo", "Número máximo"]
                chi2 = 0


                for idx, conjunto_intervalo in enumerate(intervalos, start=1):
                    frecuencias_esperadas = [len(conjunto_intervalo) / 10] * 10
                    cantidad_datos = len(conjunto_intervalo)
                    chi2_intervalo = 0
                    numero_minimo = min(conjunto_intervalo)
                    numero_maximo = max(conjunto_intervalo)


                    for i, dato in enumerate(conjunto_intervalo, start=1):
                        ri = i / cantidad_datos
                        frecuencia_obtenida = conjunto_intervalo.count(dato)
                        chi2_parcial = ((frecuencia_obtenida - len(conjunto_intervalo) / 10) ** 2) / (len(conjunto_intervalo) / 10)
                        chi2_intervalo += chi2_parcial
                        tabla.add_row([i, ri, i, dato, dato, frecuencia_obtenida, len(conjunto_intervalo) / 10,
                                    chi2_parcial, numero_minimo, numero_maximo])


                    tabla.add_row(["-", "-", "-", "-", "-", "-", "-", chi2_intervalo, "-", "-"])
                    chi2 += chi2_intervalo


                self.mostrar_tabla(tabla)
                self.mostrar_chi2_final(chi2)


            if self.mostrar_grafico:
                self.mostrar_histograma_chi2(conjunto_filtrado)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese el intervalo de datos para la prueba Chi cuadrado.")


    def mostrar_tabla(self, tabla):
        resultado_text = tk.Text(self.master, height=10, width=100)
        resultado_text.pack()
        resultado_text.insert(tk.END, str(tabla) + "\n\n")


    def mostrar_chi2_final(self, chi2):
        resultado_text = tk.Text(self.master, height=10, width=100)
        resultado_text.pack()
        resultado_text.insert(tk.END, f"Chi cuadrado final: {chi2}\n\n")


    def mostrar_histograma_chi2(self, numeros):
        plt.hist(numeros, bins=10, alpha=0.5, color='orange', edgecolor='black')  # Generar histograma de Chi cuadrado
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        plt.title('Histograma para la Prueba de Chi Cuadrado')
        plt.show()
