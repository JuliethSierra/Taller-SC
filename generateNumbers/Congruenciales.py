import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk  # Importa ttk como submódulo de tkinter


class PseudoRandomGenerator:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def generate(self, num_values):
        values = []
        xi = self.seed
        for _ in range(num_values):
            xi = (self.a * xi + self.c) % self.m
            values.append(xi / self.m)
        return values

class GUIC(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de números pseudoaleatorios")

        self.a_label = ttk.Label(self, text="Valor de a:")
        self.a_label.grid(row=0, column=0, padx=5, pady=5)
        self.a_entry = ttk.Entry(self)
        self.a_entry.grid(row=0, column=1, padx=5, pady=5)

        self.c_label = ttk.Label(self, text="Valor de c:")
        self.c_label.grid(row=1, column=0, padx=5, pady=5)
        self.c_entry = ttk.Entry(self)
        self.c_entry.grid(row=1, column=1, padx=5, pady=5)

        self.m_label = ttk.Label(self, text="Valor de m:")
        self.m_label.grid(row=2, column=0, padx=5, pady=5)
        self.m_entry = ttk.Entry(self)
        self.m_entry.grid(row=2, column=1, padx=5, pady=5)

        self.seed_label = ttk.Label(self, text="Semilla:")
        self.seed_label.grid(row=3, column=0, padx=5, pady=5)
        self.seed_entry = ttk.Entry(self)
        self.seed_entry.grid(row=3, column=1, padx=5, pady=5)

        self.num_values_label = ttk.Label(self, text="Número de valores:")
        self.num_values_label.grid(row=4, column=0, padx=5, pady=5)
        self.num_values_entry = ttk.Entry(self)
        self.num_values_entry.grid(row=4, column=1, padx=5, pady=5)

        self.generate_button = ttk.Button(self, text="Generar", command=self.generate_numbers)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.plot_button = ttk.Button(self, text="Graficar", command=self.plot_numbers)
        self.plot_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.results_text = tk.Text(self, height=10, width=50)
        self.results_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def generate_numbers(self):
        a = int(self.a_entry.get())
        c = int(self.c_entry.get())
        m = int(self.m_entry.get())
        seed = int(self.seed_entry.get())
        num_values = int(self.num_values_entry.get())

        generator = PseudoRandomGenerator(a, c, m, seed)
        values = generator.generate(num_values)

        self.results_text.delete('1.0', tk.END)
        for i, value in enumerate(values, start=1):
            self.results_text.insert(tk.END, f"X{i}: {value}\n")

    def plot_numbers(self):
        a = int(self.a_entry.get())
        c = int(self.c_entry.get())
        m = int(self.m_entry.get())
        seed = int(self.seed_entry.get())
        num_values = int(self.num_values_entry.get())

        generator = PseudoRandomGenerator(a, c, m, seed)
        values = generator.generate(num_values)

        plt.plot(range(1, num_values + 1), values, marker='o', linestyle='-')
        plt.xlabel('Iteración')
        plt.ylabel('Número Pseudoaleatorio')
        plt.title('Secuencia de números pseudoaleatorios')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
