import tkinter as tk
from tkinter import filedialog, messagebox
import os
import numpy as np
import matplotlib.pyplot as plt

class GenerateTests:
    def __init__(self, master):
        self.master = master
        self.master.title("Pruebas")
        self.etiqueta = tk.Label(master, text="Pruebas")
        self.etiqueta.pack()
      class PruebasEstadisticas:
    @staticmethod
    def media_conjunto(conjunto):
        suma = sum(conjunto)
        media = suma / len(conjunto)
        return media

    @staticmethod
    def varianza_conjunto(conjunto):
        media = PruebasEstadisticas.media_conjunto(conjunto)
        suma_cuadrados = sum((x - media) ** 2 for x in conjunto)
        varianza = suma_cuadrados / len(conjunto)
        return varianza

    @staticmethod
    def prueba_de_medias(conjunto):
        media = PruebasEstadisticas.media_conjunto(conjunto)
        resultado = 0.49 <= media <= 0.51
        return resultado

    @staticmethod
    def prueba_de_varianza(conjunto):
        varianza = PruebasEstadisticas.varianza_conjunto(conjunto)
        resultado = 0.077 <= varianza <= 0.083
        return resultado

    @staticmethod
    def prueba_ks(conjunto):
        conjunto_ordenado = sorted(conjunto)
        n = len(conjunto)
        d_plus = max((i + 1) / n - conjunto_ordenado[i] for i in range(n))
        d_minus = max(conjunto_ordenado[i] - i / n for i in range(n))
        d = max(d_plus, d_minus)
        ks_estadistico = ((n ** 0.5) + 0.12 + 0.11 / n) * d
        ks_criterio = 1.36 / (n ** 0.5)
        resultado = ks_estadistico <= ks_criterio
        return resultado

    @staticmethod
    def prueba_chi2(conjunto):
        frecuencias_esperadas = [0.1] * 10
        frecuencias_obtenidas = [conjunto.count(i) / len(conjunto) for i in range(10)]
        chi2_estadistico = sum((obs - esp) ** 2 / esp for obs, esp in zip(frecuencias_obtenidas, frecuencias_esperadas))
        chi2_criterio = 16.919
        resultado = chi2_estadistico <= chi2_criterio
        return resultado
    def prueba_poker(conjunto):
            ocurrencias = {}
            for num in conjunto:
                num_str = str(num)
                frecuencia = len(set(num_str))
                if frecuencia not in ocurrencias:
                    ocurrencias[frecuencia] = 0
                ocurrencias[frecuencia] += 1
            chi2_estadistico = sum(((obs - 1250) ** 2) / 1250 for obs in ocurrencias.values())
            chi2_criterio = 11.07
            resultado = chi2_estadistico <= chi2_criterio
            return resultado


class InterfazPruebasEstadisticas:
    def __init__(self, master):
        self.master = master
        master.title("Pruebas Estadísticas")

        self.label = tk.Label(master, text="Seleccione un archivo o ingrese números separados por comas:")
        self.label.pack()

        self.cargar_archivo_button = tk.Button(master, text="Cargar archivo", command=self.cargar_archivo)
        self.cargar_archivo_button.pack()

        self.archivo_entry = tk.Entry(master)
        self.archivo_entry.pack()

        self.ejecutar_pruebas_button = tk.Button(master, text="Ejecutar pruebas", command=self.ejecutar_pruebas)
        self.ejecutar_pruebas_button.pack()

        self.resultados_text = tk.Text(master, height=10, width=50)
        self.resultados_text.pack()

    def cargar_archivo(self):
        archivo_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Seleccione un archivo")
        self.archivo_entry.delete(0, tk.END)
        self.archivo_entry.insert(0, archivo_path)

    def ejecutar_pruebas(self):
        archivo_path = self.archivo_entry.get()
        if archivo_path:
            try:
                numeros = []
                with open(archivo_path, 'r') as file:
                    if archivo_path.endswith('.txt'):
                        # Leer archivo de texto plano
                        for line in file:
                            numeros.extend([float(num.replace(',', '.')) for num in line.strip().split()])
                    elif archivo_path.endswith('.csv'):
                        # Leer archivo CSV
                        import csv
                        csv_reader = csv.reader(file)
                        for row in csv_reader:
                            numeros.extend([float(num.replace(',', '.')) for num in row])
                    elif archivo_path.endswith('.tsv'):
                        # Leer archivo TSV
                        for line in file:
                            numeros.extend([float(num.replace(',', '.')) for num in line.strip().split('\t')])

                resultados = {
                    "Prueba de Medias": PruebasEstadisticas.prueba_de_medias(numeros),
                    "Prueba de Varianza": PruebasEstadisticas.prueba_de_varianza(numeros),
                    "Prueba KS": PruebasEstadisticas.prueba_ks(numeros),
                    "Prueba Chi2": PruebasEstadisticas.prueba_chi2(numeros),
                    "Prueba de Póker": PruebasEstadisticas.prueba_poker(numeros)
                }
                self.mostrar_resultados(resultados)
                self.mostrar_histograma(numeros)
                self.mostrar_histograma_chi2(numeros)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un archivo o ingrese números.")

    def mostrar_resultados(self, resultados):
        self.resultados_text.delete(1.0, tk.END)
        for prueba, resultado in resultados.items():
            if resultado:
                self.resultados_text.insert(tk.END, f"Los números pasan la {prueba}.\n")
            else:
                self.resultados_text.insert(tk.END, f"Los números NO pasan la {prueba}.\n")

    def mostrar_histograma(self, numeros):
        # Calcular la frecuencia de cada valor
        valores, frecuencias = np.unique(numeros, return_counts=True)

        # Definir el ancho de las barras y el espacio entre ellas
        ancho_barra = 0.5
        espacio_entre_barras = 0.1

        # Calcular el ancho total de cada conjunto de barras
        ancho_total = ancho_barra + espacio_entre_barras

        # Calcular la posición de inicio de cada conjunto de barras
        posiciones = np.arange(len(valores)) * ancho_total

        # Crear el gráfico de barras con espacio entre ellas
        plt.bar(posiciones, frecuencias, width=ancho_barra, color='skyblue')

        # Establecer etiquetas y título del gráfico
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        plt.title('Histograma para la Prueba de Smirnov')

        # Establecer las etiquetas del eje x en el centro de cada conjunto de barras
        plt.xticks(posiciones + ancho_barra / 2, valores)

        # Mostrar el gráfico
        plt.show()

    def mostrar_histograma_chi2(self, numeros):
        plt.hist(numeros, bins=10, alpha=0.5, color='orange', edgecolor='black')  # Generar histograma de Chi cuadrado
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        plt.title('Histograma para la Prueba de Chi Cuadrado')
        plt.show()


def main():
    root = tk.Tk()
    app = InterfazPruebasEstadisticas(root)
    root.mainloop()


if __name__ == "__main__":
    main()
