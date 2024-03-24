import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

class GUIM:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Generador de Números Pseudoaleatorios')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.label_semilla = tk.Label(self.frame, text='Semilla:')
        self.label_semilla.grid(row=0, column=0, padx=5, pady=5)
        self.entry_semilla = tk.Entry(self.frame)
        self.entry_semilla.grid(row=0, column=1, padx=5, pady=5)

        self.label_iteraciones = tk.Label(self.frame, text='Iteraciones:')
        self.label_iteraciones.grid(row=1, column=0, padx=5, pady=5)
        self.entry_iteraciones = tk.Entry(self.frame)
        self.entry_iteraciones.grid(row=1, column=1, padx=5, pady=5)

        self.btn_generar = tk.Button(self.frame, text='Generar', command=self.generar_secuencia)
        self.btn_generar.grid(row=2, columnspan=2, padx=5, pady=5)

        # Crear la tabla
        self.tree = ttk.Treeview(self.frame, columns=("Iteración", "Xi", "Ri"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Iteración")
        self.tree.heading("#2", text="Xi")
        self.tree.heading("#3", text="Ri")
        self.tree.grid(row=3, columnspan=2, padx=5, pady=5)

    def generar_secuencia(self):
        semilla = int(self.entry_semilla.get())
        n = int(self.entry_iteraciones.get())
        secuencia = self.cuadrados_medios(semilla, n)

        # Limpiar la tabla antes de actualizarla
        self.limpiar_tabla()

        # Actualizar la tabla
        for i, num in enumerate(secuencia):
            xi = num
            ri = num / 10000
            ni = i + 1
            self.tree.insert("", "end", values=(ni, xi, ri))

        # Actualizar el gráfico
        plt.plot(secuencia, marker='o')
        plt.title('Secuencia de números pseudoaleatorios (Método de Cuadrados Medios)')
        plt.xlabel('Iteraciones')
        plt.ylabel('Números')
        plt.show()

    def limpiar_tabla(self):
        # Limpiar la tabla
        for record in self.tree.get_children():
            self.tree.delete(record)

    def cuadrados_medios(self, semilla, n):
        numeros = [semilla]
        for i in range(n):
            cuadrado = numeros[-1] ** 2
            numero = int(str(cuadrado).zfill(4)[1:5])
            numeros.append(numero)
        return numeros

    def ejecutar(self):
        self.root.mainloop()

# Para ejecutar la interfaz gráfica desde otra clase
if __name__ == "__main__":
    gui = GUIM()
    gui.ejecutar()
