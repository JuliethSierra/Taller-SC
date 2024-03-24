class CongruenciaLineal:
    # Clase para crear los números pseudoaleatorios (el millón :( ) método de congruencia lineal

    def __init__(self, seed, a, c, m):
        self.seed = seed       # Semilla
        self.a = a             # Multiplicador
        self.c = c             # Incremento
        self.m = m             # Módulo
        self.state = seed

    # Método para generar los números entre 0 y 10 (que así se necesitan en la rana)
    def random(self, min=0, max=10):
        self.state = (self.a * self.state + self.c) % self.m         # Fórmula: Multiplicar el estado actual por el multiplicador, se agrega el complemento y se toma el residuo de la división por el módulo
        return min + (max - min) * (self.state / self.m)             # Se utiliza la técnica de escalado lineal según los rangos. Se normaliza dividiendo por el módulo

# Define los parámetros de la congruencia lineal
seed = 123  # Semilla inicial
a = 1664525
c = 1013904223
m = 2**32

# Crea una instancia del generador
cl_prng = CongruenciaLineal(seed, a, c, m)

# Genera un millón de números pseudoaleatorios en el rango 0 a un millooooon
cantidad = 1000000
with open("numbers2.txt", "w") as f:          # Lo guarda en el archivo que se utiliza en la rana
    for _ in range(cantidad):
        numero = cl_prng.random()
        f.write("{:.4f}, ".format(numero))

print("Números pseudoaleatorios guardados en 'numbers.txt'")