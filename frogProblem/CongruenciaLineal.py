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
''' 
# UNO
seed = 123  # Semilla inicial
a = 1664525
c = 1013904223
m = 2**32
'''
'''
# DOS
seed = 123456789
a = 48271
c = 0
m = 2**31 - 1
'''
'''
#TRES
seed = 12345
a = 65539
c = 0
m = 2**31
'''

# CUATRO: ESTE SIRVE PARA EL DE 2 DIMENSIONES:
seed = 1
a = 22695477
c = 1
m = 2**32

'''
#CINCO
seed = 1009
a = 214013
c = 2531011
m = 2**31
'''
'''
#SEIS
seed = 123456789
a = 1664525
c = 1013904223
m = 2**32
'''
'''
#SIETE
seed = 123456789
a = 1140671485
c = 12820163
m = 2**24
'''
'''
#OCHO   También sirve para 2 dimensiones
seed = 1
a = 16807
c = 0
m = 2**31 - 1
'''
'''
#NUEVE
seed = 123456789
a = 1664525
c = 1013904223
m = 2**32 - 1
'''
'''
#DIEZ
seed = 123456789
a = 69069
c = 1
m = 2**32
'''
'''
#ONCE
seed = 1234567
a = 65539
c = 0
m = 2**31
'''
'''
#DOCE
seed = 1234567890
a = 6364136223846793005
c = 1442695040888963407
m = 2**64
'''
'''
# TRECE
seed = 987654321
a = 48271
c = 12345
m = 2**31 - 1
'''
'''
# CATORCE
seed = 987654321
a = 65539
c = 12345
m = 2**31
'''
'''
# QUINCE
seed = 123456789
a = 48271
c = 987654321
m = 2**31 - 1
'''
'''
# DIECISEIS
seed = 987654321
a = 22695477
c = 987654321
m = 2**31 - 1
'''

# Crea una instancia del generador
cl_prng = CongruenciaLineal(seed, a, c, m)

# Genera un millón de números pseudoaleatorios en el rango 0 a un millooooon
cantidad = 1000000
with open("numbers.txt", "w") as f:          # Lo guarda en el archivo que se utiliza en la rana
    for _ in range(cantidad):
        numero = cl_prng.random()
        f.write("{:.4f}, ".format(numero))

print("Números pseudoaleatorios guardados en 'numbers.txt'")