import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


class NormalDistributionGenerator:
    def generate(self, mean, std_dev, num_values):
        values = np.random.normal(mean, std_dev, num_values)
        return values

class GUIN(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de números pseudoaleatorios con distribución normal")

        self.mean_label = ttk.Label(self, text="Media:")
        self.mean_label.grid(row=0, column=0, padx=5, pady=5)
        self.mean_entry = ttk.Entry(self)
        self.mean_entry.grid(row=0, column=1, padx=5, pady=5)

        self.std_dev_label = ttk.Label(self, text="Desviación estándar:")
        self.std_dev_label.grid(row=1, column=0, padx=5, pady=5)
        self.std_dev_entry = ttk.Entry(self)
        self.std_dev_entry.grid(row=1, column=1, padx=5, pady=5)

        self.num_values_label = ttk.Label(self, text="Número de valores:")
        self.num_values_label.grid(row=2, column=0, padx=5, pady=5)
        self.num_values_entry = ttk.Entry(self)
        self.num_values_entry.grid(row=2, column=1, padx=5, pady=5)

        self.generate_button = ttk.Button(self, text="Generar", command=self.generate_numbers)
        self.generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.results_text = tk.Text(self, height=10, width=50)
        self.results_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.plot_button = ttk.Button(self, text="Mostrar Gráfico", command=self.plot_distribution)
        self.plot_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.color_index = 0
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        self.table_label = ttk.Label(self, text="Tabla de Valores:")
        self.table_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.tree = ttk.Treeview(self, columns=("Iteración", "Xi", "Ri", "Ni"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Iteración")
        self.tree.heading("#2", text="Xi")
        self.tree.heading("#3", text="Ri")
        self.tree.heading("#4", text="Ni")

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        self.tree.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.scrollbar.grid(row=8, column=2, sticky="ns")

    def generate_numbers(self):
        mean = float(self.mean_entry.get())
        std_dev = float(self.std_dev_entry.get())
        num_values = int(self.num_values_entry.get())

        generator = NormalDistributionGenerator()
        values = generator.generate(mean, std_dev, num_values)

        self.results_text.delete('1.0', tk.END)
        for i, value in enumerate(values, start=1):
            self.results_text.insert(tk.END, f"X{i}: {value}\n")

        self.update_table(values)

    def update_table(self, values):
        self.tree.delete(*self.tree.get_children())
        for i, value in enumerate(values, start=1):
            ri = value / max(values)
            ni = ri - min(values) / max(values)
            self.tree.insert("", "end", values=(i, value, ri, ni))

    def plot_distribution(self):
        mean = float(self.mean_entry.get())
        std_dev = float(self.std_dev_entry.get())
        num_values = int(self.num_values_entry.get())

        generator = NormalDistributionGenerator()
        values = generator.generate(mean, std_dev, num_values)

        color = self.colors[self.color_index % len(self.colors)]
        self.color_index += 1

        self.ax.plot(range(1, num_values + 1), values, color=color)
        self.ax.set_xlabel('Iteración')
        self.ax.set_ylabel('Número Pseudoaleatorio')
        self.ax.set_title('Secuencia de números pseudoaleatorios')
        self.ax.grid(True)

        self.canvas.draw()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
