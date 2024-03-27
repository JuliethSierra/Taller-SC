import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import numpy as np
import matplotlib.pyplot as plt
from pruebas_estadisticas import PruebasEstadisticas
from chi2Handler import Chi2Handler
from prueba_poker import PruebaPoker
from collections import Counter

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

        self.prueba_seleccionada_label = tk.Label(master, text="Seleccione la prueba estadística:")
        self.prueba_seleccionada_label.pack()

        self.opciones_prueba = ("Prueba de Medias", "Prueba de Varianza", "Prueba KS", "Prueba Chi2", "Prueba de Póker")
        self.combo_prueba = ttk.Combobox(master, values=self.opciones_prueba, state="readonly")
        self.combo_prueba.pack()

        # Agregar casilla de verificación para seleccionar el opción de mostrar el proceso
        self.mostrar_proceso_var = tk.BooleanVar()
        self.mostrar_proceso_checkbox = tk.Checkbutton(master, text="Mostrar proceso", variable=self.mostrar_proceso_var)
        self.mostrar_proceso_checkbox.pack()

        # Agregar entrada para seleccionar el intervalo de datos
        self.intervalo_label = tk.Label(master, text="Intervalo de datos (separados por coma):")
        self.intervalo_label.pack()
        self.intervalo_entry = tk.Entry(master)
        self.intervalo_entry.pack()

        # Agregar casilla de verificación para seleccionar el tipo de gráfico para Chi cuadrado
        self.grafico_chi_var = tk.BooleanVar()
        self.grafico_chi_checkbox = tk.Checkbutton(master, text="Mostrar gráfico (Chi cuadrado)", variable=self.grafico_chi_var)
        self.grafico_chi_checkbox.pack()

        self.ejecutar_prueba_button = tk.Button(master, text="Ejecutar prueba", command=self.ejecutar_prueba)
        self.ejecutar_prueba_button.pack()

        self.resultados_text = tk.Text(master, height=10, width=100)
        self.resultados_text.pack()

    def cargar_archivo(self):
        archivo_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Seleccione un archivo")
        self.archivo_entry.delete(0, tk.END)
        self.archivo_entry.insert(0, archivo_path)

    def mostrar_resultados(self, prueba, resultado):
        self.resultados_text.insert(tk.END, f"Resultado de la {prueba}:\n")
        if prueba == "Prueba de Varianza":
            if resultado:
                self.resultados_text.insert(tk.END, "Los números pasan la prueba de varianza.\n")
                self.resultados_text.insert(tk.END, "Aceptación: Sí\n")
            else:
                self.resultados_text.insert(tk.END, "Los números NO pasan la prueba de varianza.\n")
                self.resultados_text.insert(tk.END, "Aceptación: No\n")

            alpha = 0.05  # Assuming alpha value
            n = len(self.numeros)
            R = max(self.numeros) - min(self.numeros)
            sigma = np.sqrt(PruebasEstadisticas.varianza_conjunto(self.numeros))
            alpha_over_2 = alpha / 2
            one_minus_alpha_over_2 = 1 - alpha_over_2
            X2_alpha_over_2 = 3.325  # Critical value for alpha/2 with degrees of freedom (n-1)
            X2_one_minus_alpha_over_2 = 16.919  # Critical value for 1 - alpha/2 with degrees of freedom (n-1)
            LI = sigma * np.sqrt((n - 1) / X2_one_minus_alpha_over_2)
            LS = sigma * np.sqrt((n - 1) / X2_alpha_over_2)

            self.resultados_text.insert(tk.END, f"Alpha: {alpha}\n")
            self.resultados_text.insert(tk.END, f"n: {n}\n")
            self.resultados_text.insert(tk.END, f"R: {R}\n")
            self.resultados_text.insert(tk.END, f"Sigma: {sigma}\n")
            self.resultados_text.insert(tk.END, f"Alpha/2: {alpha_over_2}\n")
            self.resultados_text.insert(tk.END, f"1-(alpha/2): {one_minus_alpha_over_2}\n")
            self.resultados_text.insert(tk.END, f"X^2 (alpha/2): {X2_alpha_over_2}\n")
            self.resultados_text.insert(tk.END, f"X^2 (1-(alpha/2)): {X2_one_minus_alpha_over_2}\n")
            self.resultados_text.insert(tk.END, f"LI: {LI}\n")
            self.resultados_text.insert(tk.END, f"LS: {LS}\n\n")
        else:
            if resultado:
                self.resultados_text.insert(tk.END, f"Los números pasan la {prueba}.\n\n")
            else:
                self.resultados_text.insert(tk.END, f"Los números NO pasan la {prueba}.\n\n")

    def ejecutar_prueba(self):
        archivo_path = self.archivo_entry.get()
        prueba_seleccionada = self.combo_prueba.get()

        if archivo_path and prueba_seleccionada:
            try:
                numeros = []
                with open(archivo_path, 'r') as file:
                    if archivo_path.endswith('.txt'):
                        for line in file:
                            numeros.extend([float(num.replace(',', '.')) for num in line.strip().split()])
                    elif archivo_path.endswith('.csv'):
                        import csv
                        csv_reader = csv.reader(file)
                        for row in csv_reader:
                            numeros.extend([float(num.replace(',', '.')) for num in row])
                    elif archivo_path.endswith('.tsv'):
                        for line in file:
                            numeros.extend([float(num.replace(',', '.')) for num in line.strip().split('\t')])

                resultado = None
                if prueba_seleccionada == "Prueba de Medias":
                    resultado = PruebasEstadisticas.prueba_de_medias(numeros)
                    if resultado is not None:
                        self.mostrar_resultados(prueba_seleccionada, resultado)
                        # Aquí agregamos la impresión adicional
                        if numeros:
                            R = None
                        if len(numeros) > 1:
                            R = max(numeros) - min(numeros)
                        if R is not None:
                            alpha = 0.05
                            n = len(numeros)
                            sigma = np.std(numeros)
                            alpha_over_2 = alpha / 2
                            one_minus_alpha_over_2 = 1 - alpha_over_2
                            z = 1.96
                            LI = np.mean(numeros) - z * (sigma / np.sqrt(n))
                            LS = np.mean(numeros) + z * (sigma / np.sqrt(n))

                            self.resultados_text.insert(tk.END, f"Alpha: {alpha}\n")
                            self.resultados_text.insert(tk.END, f"n: {n}\n")
                            self.resultados_text.insert(tk.END, f"R: {R}\n")
                            self.resultados_text.insert(tk.END, f"1-(alpha/2): {one_minus_alpha_over_2}\n")
                            self.resultados_text.insert(tk.END, f"z: {z}\n")
                            self.resultados_text.insert(tk.END, f"LI: {LI}\n")
                            self.resultados_text.insert(tk.END, f"LS: {LS}\n\n")
                        else:
                            messagebox.showwarning("Advertencia", "No hay datos suficientes para realizar la prueba de medias.")
                elif prueba_seleccionada == "Prueba de Varianza":
                    resultado = PruebasEstadisticas.prueba_de_varianza(numeros)
                    if resultado is not None:
                        self.mostrar_resultados(prueba_seleccionada, resultado)
                elif prueba_seleccionada == "Prueba KS":
                    resultado = PruebasEstadisticas.prueba_ks(numeros)
                    self.mostrar_resultados(prueba_seleccionada, resultado)
                    self.mostrar_histograma(numeros)
                    # Impresión adicional para la prueba de KS
                    if numeros:
                        n = len(numeros)
                        R = max(numeros) - min(numeros)
                        minimo = min(numeros)
                        maximo = max(numeros)
                        alpha = 0.05  # Puedes ajustar este valor según tus necesidades
                        aceptacion = "Sí" if resultado else "No"
                        self.resultados_text.insert(tk.END, f"Para la prueba KS:\n")
                        self.resultados_text.insert(tk.END, f"Pasa la prueba: {aceptacion}\n")
                        self.resultados_text.insert(tk.END, f"Aceptación: {aceptacion}\n")
                        self.resultados_text.insert(tk.END, f"Alpha: {alpha}\n")
                        self.resultados_text.insert(tk.END, f"n: {n}\n")
                        self.resultados_text.insert(tk.END, f"R: {R}\n")
                        self.resultados_text.insert(tk.END, f"Mínimo: {minimo}\n")
                        self.resultados_text.insert(tk.END, f"Máximo: {maximo}\n\n")
                elif prueba_seleccionada == "Prueba de Póker":
                    resultado = PruebasEstadisticas.prueba_poker(numeros)
                    if resultado is not None:  # Comprobación adicional para evitar errores
                        self.mostrar_resultados(prueba_seleccionada, resultado)
                        # Llamar a la función para mostrar los resultados en una tabla
                        self.mostrar_resultados_en_tabla(prueba_seleccionada, numeros)
                elif prueba_seleccionada == "Prueba Chi2":
                    intervalo = self.intervalo_entry.get()
                    if intervalo:
                        resultado = PruebasEstadisticas.prueba_chi2(numeros)
                        if resultado is not None:
                            self.mostrar_resultados(prueba_seleccionada, resultado)
                            intervalo_lista = list(map(float, intervalo.split(',')))
                            chi2_handler = Chi2Handler(self.master, numeros, intervalo_lista, self.mostrar_proceso_var.get(), self.grafico_chi_var.get())
                            chi2_handler.mostrar_resultados()
                    else:
                        messagebox.showwarning("Advertencia", "Por favor ingrese el intervalo de datos para la prueba Chi cuadrado.")

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un archivo y una prueba estadística.")

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

        # Crear el gráfico de barras
        plt.bar(posiciones, frecuencias, width=ancho_barra, color='skyblue')

        # Establecer etiquetas y título del gráfico
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        plt.title('Histograma para la Prueba de Smirnov')

        # Establecer las etiquetas del eje x en el centro de cada conjunto de barras
        plt.xticks(posiciones + ancho_barra / 2, valores)

        # Mostrar el gráfico
        plt.show()

    def mostrar_resultados_en_tabla(self, prueba, numeros):
        ventana_tabla = tk.Toplevel(self.master)
        ventana_tabla.title("Resultados en Tabla")

        # Creamos un canvas para permitir el desplazamiento vertical
        canvas = tk.Canvas(ventana_tabla)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tabla_frame = tk.Frame(canvas)
        tabla_frame.pack()

        # Agregamos el frame de la tabla al canvas
        canvas.create_window((0, 0), window=tabla_frame, anchor=tk.NW)

        # Creamos una barra de desplazamiento para moverse verticalmente
        scrollbar = tk.Scrollbar(ventana_tabla, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=scrollbar.set)

        # Crear etiquetas para los encabezados de la tabla
        encabezados = ("Valores RI", "Oi", "Probabilidad", "Ei", "(Ei-Oi)^2/Ei")
        for col, encabezado in enumerate(encabezados):
            tk.Label(tabla_frame, text=encabezado, relief=tk.RIDGE, width=15).grid(row=0, column=col, sticky=tk.NSEW)

        # Calcular frecuencias de los valores
        frecuencias = Counter(numeros)

        # Calcular total de observaciones
        total_observaciones = len(numeros)

        # Calcular Ei y chi cuadrado para cada valor
        ei_values = []
        chi_cuadrado_values = []
        for valor, frecuencia in frecuencias.items():
            ei = total_observaciones * (1/6)  # Para la prueba de poker
            ei_values.append(ei)
            chi_cuadrado = ((frecuencia - ei) ** 2) / ei
            chi_cuadrado_values.append(chi_cuadrado)

        # Calcular sumatoria de chi cuadrado
        suma_chi_cuadrado = sum(chi_cuadrado_values)

        # Llenar la tabla con los datos
        for i, (valor, frecuencia, ei, chi_cuadrado) in enumerate(zip(frecuencias.keys(), frecuencias.values(), ei_values, chi_cuadrado_values), start=1):
            probabilidad = frecuencia / total_observaciones
            chi_cuadrado_resultado = (ei - frecuencia) ** 2 / ei if ei != 0 else 0
            # Establecer un ancho más amplio para la columna de valores
            tk.Label(tabla_frame, text=valor, width=20).grid(row=i, column=0)
            tk.Label(tabla_frame, text=frecuencia).grid(row=i, column=1)
            tk.Label(tabla_frame, text=f"{probabilidad:.4f}").grid(row=i, column=2)
            tk.Label(tabla_frame, text=f"{ei:.4f}").grid(row=i, column=3)
            tk.Label(tabla_frame, text=f"{chi_cuadrado_resultado:.4f}").grid(row=i, column=4)

        # Agregar fila para la sumatoria de chi cuadrado
        tk.Label(tabla_frame, text="Suma").grid(row=len(frecuencias) + 1, column=0, sticky=tk.E)
        tk.Label(tabla_frame, text="").grid(row=len(frecuencias) + 1, column=1)
        tk.Label(tabla_frame, text="").grid(row=len(frecuencias) + 1, column=2)
        tk.Label(tabla_frame, text="").grid(row=len(frecuencias) + 1, column=3)
        tk.Label(tabla_frame, text=f"{suma_chi_cuadrado:.4f}").grid(row=len(frecuencias) + 1, column=4)

        # Agregar clasificación vertical en la tabla
        clasificacion_vertical = PruebaPoker.prueba_poker(list(frecuencias.keys()))
        tk.Label(tabla_frame, text="Clasificación Vertical:").grid(row=len(frecuencias) + 2, column=0, sticky=tk.E)
        tk.Label(tabla_frame, text=clasificacion_vertical).grid(row=len(frecuencias) + 2, column=1, columnspan=4, sticky=tk.W)

        # Hacer que la tabla sea redimensionable
        for i in range(len(frecuencias) + 2):
            tabla_frame.grid_rowconfigure(i, weight=1)
            tabla_frame.grid_columnconfigure(i, weight=1)

        # Configurar el canvas para que se desplace con la rueda del ratón
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))

def main():
    root = tk.Tk()
    app = InterfazPruebasEstadisticas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
