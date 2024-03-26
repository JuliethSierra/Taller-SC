import tkinter as tk

from VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = VentanaPrincipal(ventana_principal)
    ventana_principal.mainloop()