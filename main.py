import tkinter as tk
from VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    # Crear la ventana principal de la aplicación
    ventana_principal = tk.Tk()
    ventana_principal.title("MontecarloProblem")

    # Dimensiones de la ventana principal
    screen_width = ventana_principal.winfo_screenwidth()
    screen_height = ventana_principal.winfo_screenheight()
    ventana_width = int(screen_width * 0.2)
    ventana_height = int(screen_height * 0.2)

    # Coordenadas para centrar la ventana principal
    x = (screen_width - ventana_width) // 2
    y = (screen_height - ventana_height) // 2

    # Establecer el tamaño y posición de la ventana principal
    ventana_principal.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")

    # Iniciar la aplicación
    app = VentanaPrincipal(ventana_principal)
    ventana_principal.mainloop()
