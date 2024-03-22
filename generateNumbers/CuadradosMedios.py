import matplotlib.pyplot as plt
import random
import tkinter as tk
from itertools import cycle
from tkinter import ttk


class UniformRandomGenerator:
    def __init__(self, a, b, seed=None):
        self.a = a
        self.b = b
        self.seed = seed
        if seed:
            random.seed(seed)

    def generate(self, num_values):
        values = []
        for i in range(1, num_values + 1):
            value = random.uniform(self.a, self.b)
            values.append((i, value, value / self.b, i))
        return values

class GUIM(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de números pseudoaleatorios - Distribución Uniforme")

        self.a_label = ttk.Label(self, text="Límite inferior (a):")
        self.a_label.grid(row=0, column=0, padx=5, pady=5)
        self.a_entry = ttk.Entry(self)
        self.a_entry.grid(row=0, column=1, padx=5, pady=5)

        self.b_label = ttk.Label(self, text="Límite superior (b):")
        self.b_label.grid(row=1, column=0, padx=5, pady=5)
        self.b_entry = ttk.Entry(self)
        self.b_entry.grid(row=1, column=1, padx=5, pady=5)

        self.seed_label = ttk.Label(self, text="Semilla (opcional):")
        self.seed_label.grid(row=2, column=0, padx=5, pady=5)
        self.seed_entry = ttk.Entry(self)
        self.seed_entry.grid(row=2, column=1, padx=5, pady=5)

        self.num_values_label = ttk.Label(self, text="Número de valores:")
        self.num_values_label.grid(row=3, column=0, padx=5, pady=5)
        self.num_values_entry = ttk.Entry(self)
        self.num_values_entry.grid(row=3, column=1, padx=5, pady=5)

        self.generate_button = ttk.Button(self, text="Generar", command=self.generate_numbers)
        self.generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.plot_button = ttk.Button(self, text="Graficar", command=self.plot_numbers)
        self.plot_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.results_text = tk.Text(self, height=10, width=50)
        self.results_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.tree = ttk.Treeview(self, columns=("Iteración", "Xi", "Ri", "Ni"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Iteración")
        self.tree.heading("#2", text="Xi")
        self.tree.heading("#3", text="Ri")
        self.tree.heading("#4", text="Ni")
        self.tree.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.colors = cycle(['blue', 'green', 'red', 'purple', 'orange'])

    def generate_numbers(self):
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        seed = self.seed_entry.get()
        num_values = int(self.num_values_entry.get())

        generator = UniformRandomGenerator(a, b, seed)
        values = generator.generate(num_values)

        self.results_text.delete('1.0', tk.END)
        for i, (iteration, xi, ri, ni) in enumerate(values, start=1):
            self.results_text.insert(tk.END, f"X{i}: {xi}\n")
            self.tree.insert("", "end", values=(i, iteration, xi, ri, ni))

    def plot_numbers(self):
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        seed = self.seed_entry.get()
        num_values = int(self.num_values_entry.get())

        generator = UniformRandomGenerator(a, b, seed)
        values = generator.generate(num_values)

        color = next(self.colors)

        plt.plot([v[1] for v in values], color=color)
        plt.xlabel('Iteración')
        plt.ylabel('Valor')
        plt.title('Gráfico de líneas de números pseudoaleatorios')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
