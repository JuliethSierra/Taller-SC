import numpy as np
import matplotlib.pyplot as plt
class PruebasEstadisticas:
    @staticmethod
    def media_conjunto(conjunto):
         """
        Calcula la media aritmética de un conjunto de datos.

        Parámetros:
            conjunto (list): El conjunto de datos del cual se calcula la media.

        Retorna:
            float: La media aritmética del conjunto de datos.
        """
        suma = sum(conjunto)
        media = suma / len(conjunto)
        return media


    @staticmethod
    def varianza_conjunto(conjunto):
         """
        Calcula la varianza de un conjunto de datos.

        Parámetros:
            conjunto (list): El conjunto de datos del cual se calcula la varianza.

        Retorna:
            float: La varianza del conjunto de datos.
        """
        media = PruebasEstadisticas.media_conjunto(conjunto)
        suma_cuadrados = sum((x - media) ** 2 for x in conjunto)
        varianza = suma_cuadrados / len(conjunto)
        return varianza


    @staticmethod
    def prueba_de_medias(conjunto):
         """
        Realiza la prueba de medias para determinar si la media del conjunto está dentro de un rango específico.

        Parámetros:
            conjunto (list): El conjunto de datos para realizar la prueba.

        Retorna:
            bool: True si la media del conjunto está dentro del rango [0.49, 0.51], False en caso contrario.
        """
        media = PruebasEstadisticas.media_conjunto(conjunto)
        resultado = 0.49 <= media <= 0.51
        return resultado


    @staticmethod
    def prueba_de_varianza(conjunto):
         """
        Realiza la prueba de varianza para determinar si la varianza del conjunto está dentro de un rango específico.

        Parámetros:
            conjunto (list): El conjunto de datos para realizar la prueba.

        Retorna:
            bool: True si la varianza del conjunto está dentro del rango [0.077, 0.083], False en caso contrario.
        """
        varianza = PruebasEstadisticas.varianza_conjunto(conjunto)
        resultado = 0.077 <= varianza <= 0.083
        return resultado


    @staticmethod
    def prueba_ks(conjunto):
         """
        Realiza la prueba de Kolmogorov-Smirnov para determinar si el conjunto sigue una distribución uniforme.

        Parámetros:
            conjunto (list): El conjunto de datos para realizar la prueba.

        Retorna:
            bool: True si el conjunto sigue una distribución uniforme, False en caso contrario.
        """
        conjunto_ordenado = sorted(conjunto)
        n = len(conjunto)
        d_plus = max((i + 1) / n - conjunto_ordenado[i] for i in range(n))
        d_minus = max(conjunto_ordenado[i] - i / n for i in range(n))
        d = max(d_plus, d_minus)
        ks_estadistico = ((n ** 0.5) + 0.12 + 0.11 / n) * d
        ks_criterio = 1.36 / (n ** 0.5)
        resultado = ks_estadistico <= ks_criterio
        return resultado


    @staticmethod
    def prueba_chi2(conjunto):
         """
        Realiza la prueba de Chi-cuadrado para determinar si el conjunto sigue una distribución uniforme.

        Parámetros:
            conjunto (list): El conjunto de datos para realizar la prueba.

        Retorna:
            bool: True si el conjunto sigue una distribución uniforme, False en caso contrario.
        """
        frecuencias_esperadas = [0.1] * 10
        frecuencias_obtenidas = [conjunto.count(i) / len(conjunto) for i in range(10)]
        chi2_estadistico = sum((obs - esp) ** 2 / esp for obs, esp in zip(frecuencias_obtenidas, frecuencias_esperadas))
        chi2_criterio = 16.919
        resultado = chi2_estadistico <= chi2_criterio
        return resultado


    @staticmethod
    def prueba_poker(conjunto):
         """
        Realiza la prueba de Póker para determinar si el conjunto de números es aleatorio.

        Parámetros:
            conjunto (list): El conjunto de datos para realizar la prueba.

        Retorna:
            bool: True si el conjunto de números es aleatorio, False en caso contrario.
        """
            ocurrencias = {}
            for num in conjunto:
                num_str = str(num)
                frecuencia = len(set(num_str))
                if frecuencia not in ocurrencias:
                    ocurrencias[frecuencia] = 0
                ocurrencias[frecuencia] += 1
            chi2_estadistico = sum(((obs - 1250) ** 2) / 1250 for obs in ocurrencias.values())
            chi2_criterio = 11.07
            resultado = chi2_estadistico <= chi2_criterio
            return resultado
   
    @staticmethod
    def dividir_en_intervalos(conjunto):
        intervalos = []
        for i in range(0, len(conjunto), 100):
            intervalos.append(conjunto[i:i+100])
        return intervalos



