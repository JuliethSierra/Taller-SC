import tkinter as tk
from collections import Counter
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def read_document():
    with open("frogProblem/numbers.txt", "r") as file:
        numbers_str = file.read().strip()  # Eliminar espacios en blanco
        numbers_str = numbers_str.rstrip(',')  # Eliminar comas adicionales
        numbers = [float(num) for num in numbers_str.split(',')]
        return numbers


class FrogProblem:
    x_coordinates_1D = []

    def __init__(self, master, ventana_principal):
        self.graph_frame = None
        self.master = master
        self.ventana_principal = ventana_principal
        self.master.title("Problema de la rana")

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Definir el tamaño de la ventana
        ventana_width = int(screen_width * 0.8)
        ventana_height = int(screen_height * 0.8)

        x = (screen_width - ventana_width) // 2
        y = (screen_height - ventana_height) // 2

        self.master.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")

        self.etiqueta = tk.Label(master, text="Problema de la rana")
        self.etiqueta.pack(pady=10)

        self.options = ["Select", "1D", "2D", "3D"]
        self.selected_option = tk.StringVar()

        self.combo = ttk.Combobox(master, textvariable=self.selected_option)
        self.combo["values"] = self.options
        self.combo.set(self.options[0])
        self.combo.pack(pady=10)

        self.boton_volver = tk.Button(master, text="Volver", command=self.volver)
        self.boton_volver.pack(pady=10)

        self.combo.bind("<<ComboboxSelected>>", self.seleccionar_dimension)
        self.image_label = tk.Label(master)
        self.image_label.pack()

        # Mostrar la imagen de la rana inicialmente
        self.show_frog_image()

    def show_frog_image(self):
        frog_image = tk.PhotoImage(file="frogProblem/rana.png")
        frog_image_resized = frog_image.subsample(2, 2)

        self.image_label.configure(image=frog_image_resized)
        self.image_label.image = frog_image_resized

    def seleccionar_dimension(self, event=None):
        selection = self.selected_option.get()
        print(f"Seleccionaste la opción: {selection}")
        if selection == "Select":
            return
        else:
            self.image_label.pack_forget()
        self.clear_previous_graph()
        if selection == "1D":
            self.generar_paseo_1D()
            if "Frecuencias" not in self.options:
                self.options.append("Frecuencias")
                self.combo['values'] = self.options
        elif selection == "Frecuencias":
            self.show_frequencies()
        elif selection == "2D":
            self.generar_paseo_2D()
        elif selection == "3D":
            self.generar_paseo_3D()

    # Método para mostrar las frecuencias, para esto ya se debió seleccionar inicialmente el gráfico de 1D,
    # ya que de allí salen las posiciones x
    def show_frequencies(self):
        self.clear_previous_graph()

        # Calcular las frecuencias de las posiciones
        frequencies = Counter(self.x_coordinates_1D)
        # Convertir los resultados en dos listas separadas
        positions = list(frequencies.keys())
        frequencies_positions = list(frequencies.values())

        fig, ax = plt.subplots(figsize=(12, 12))
        # Graficar las frecuencias en un gráfico de barras
        ax.bar(positions, frequencies_positions, color='skyblue')
        ax.axhline(y=0, color='r')
        ax.set_xlabel('Positions')
        ax.set_ylabel('Frequencies')
        ax.set_title('Frequency of Positions')

        # Esta parte es para mostrarlo en la interfaz
        self.graph_frame = tk.Frame(self.master)
        self.graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Método para la generación de la ruta en 1 dimensión
    def generar_paseo_1D(self):
        self.clear_previous_graph()  # Primero limpiar por si ya está otro gráfico en la pantalla
        numbers = read_document()  # Tomar los números generados y que se encuentran en el documento
        x, y = [0], [0]

        for num in numbers:  # Ciclo que toma cada uno de los números y los valida
            if num < 5:  # Si es menor que 5 se va hacia la izquierda ( x - 1 )
                x.append(x[-1] - 1)
                y.append(y[-1] - 1)
            else:  # Si no se va la derecha ( x + 1)
                x.append(x[-1] + 1)
                y.append(y[-1] - 1)

        FrogProblem.x_coordinates_1D = x  # Guardar las posiciones para después graficar las frecuencias

        fig, ax = plt.subplots(figsize=(12, 12))
        ax.plot(x, y)
        ax.grid()
        ax.plot(0, 0, 'ro')
        ax.plot(x[-1], y[-1], 'yo')
        ax.axhline(y=0, color='r')
        ax.axvline(x=0, color='r')
        print("Punto final: ", (x[-1], y[-1]))

        self.graph_frame = tk.Frame(self.master)
        self.graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Método para la gráfica en 2 dimensiones
    def generar_paseo_2D(self):
        self.clear_previous_graph()

        numbers = read_document()

        x, y = [0], [0]

        for num in numbers:  # Se lee cada número y se verifica
            if num < 2.5:  # Menor a 2.5 es hacia arriba por ese es ( y + 1 )
                x.append(x[-1])
                y.append(y[-1] + 1)
            elif 2.5 <= num < 5:  # De 2.5 a 5 es hacia abajo por ese es ( y - 1 )
                x.append(x[-1])
                y.append(y[-1] - 1)
            elif 5 <= num < 7.5:  # De 5 a 7.5 es hacia la derecha (x + 1)
                x.append(x[-1] + 1)
                y.append(y[-1])
            else:  # Y si no es que es a la izquierda (x - 1)
                x.append(x[-1] - 1)
                y.append(y[-1])

            if x[-1] == 250 and y[-1] == 300:
                print("SI LLEGÓ LA RANA")
                break

        fig, ax = plt.subplots(figsize=(12, 12))
        ax.plot(x, y)
        ax.grid()
        ax.plot(0, 0, 'ro')
        ax.plot(x[-1], y[-1], 'yo')
        ax.axhline(y=0, color='r')
        ax.axvline(x=0, color='r')
        print("Punto final: ", (x[-1], y[-1]))

        self.graph_frame = tk.Frame(self.master)
        self.graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Método para las 3 dimensiones
    def generar_paseo_3D(self):
        self.clear_previous_graph()
        numbers = read_document()

        # Nuestras 3 dimensiones
        x, y, z = [0], [0], [0]
        # Variables para después ver la cantidad de datos
        c1, c2, c3, c4, c5, c6 = 0, 0, 0, 0, 0, 0
        for i, num in enumerate(numbers):
            if num < 1.67:              # Menor a 1.67 es hacia arriba (y+1)
                x.append(x[-1])
                y.append(y[-1] + 1)
                z.append(z[-1])
                c1 += 1
            elif 1.67 <= num < 3.33:   # Entre 1.67 y 3.33 es hacia abajo (y-1)
                x.append(x[-1])
                y.append(y[-1] - 1)
                z.append(z[-1])
                c2 += 1
            elif 3.33 <= num < 5:       # Entre 3.33 y 5 es hacia la derecha (x+1)
                x.append(x[-1] + 1)
                y.append(y[-1])
                z.append(z[-1])
                c3 += 1
            elif 5 <= num < 6.67:       # Entre 5 y 6.67 es hacia la izquierda(x-1)
                x.append(x[-1] - 1)
                y.append(y[-1])
                z.append(z[-1])
                c4 += 1
            elif 6.67 <= num < 8.33:    # Entre 6.67 y 8.33 es hacia adelante (z+1)
                x.append(x[-1])
                y.append(y[-1])
                z.append(z[-1] + 1)
                c5 += 1
            elif 8.33 <= num < 10:      # Entre 8.33 y 10 es hacia atrás (z-1)
                x.append(x[-1])
                y.append(y[-1])
                z.append(z[-1] - 1)
                c6 += 1
            # Verificar si la rana ha llegado a la posición solicitada
            if x[-1] == 45 and y[-1] == 23 and z[-1] == 17:
                print("La rana ha llegado a la posición (45, 23, 17) en {} saltos.".format(i + 1))
                break

        print(f"C1: {c1} C2: {c2} C3: {c3} C4: {c4} C5: {c5} C6: {c6}")
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z)
        ax.scatter(0, 0, 0, color='r', marker='o')
        ax.scatter(x[-1], y[-1], z[-1], color='g', marker='o')

        ax.set_xlim(min(x) - 1, max(x) + 1)
        ax.set_ylim(min(y) - 1, max(y) + 1)
        ax.set_zlim(min(z) - 1, max(z) + 1)

        print("Última coordenada:", (x[-1], y[-1], z[-1]))
        self.graph_frame = tk.Frame(self.master)
        self.graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Método para volver a la pestaña principal
    def volver(self):
        self.master.destroy()
        if self.ventana_principal:
            self.ventana_principal.deiconify()

    # Quitar el gráfico que se encuentre en la pantalla
    def clear_previous_graph(self):
        if self.graph_frame:
            self.graph_frame.destroy()
        self.graph_frame = None
