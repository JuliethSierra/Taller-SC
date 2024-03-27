import numpy as np
import matplotlib.pyplot as plt
class PruebasEstadisticas:
    @staticmethod
    def media_conjunto(conjunto):
        suma = sum(conjunto)
        media = suma / len(conjunto)
        return media


    @staticmethod
    def varianza_conjunto(conjunto):
        media = PruebasEstadisticas.media_conjunto(conjunto)
        suma_cuadrados = sum((x - media) ** 2 for x in conjunto)
        varianza = suma_cuadrados / len(conjunto)
        return varianza


    @staticmethod
    def prueba_de_medias(conjunto):
        media = PruebasEstadisticas.media_conjunto(conjunto)
        resultado = 0.49 <= media <= 0.51
        return resultado


    @staticmethod
    def prueba_de_varianza(conjunto):
        varianza = PruebasEstadisticas.varianza_conjunto(conjunto)
        resultado = 0.077 <= varianza <= 0.083
        return resultado


    @staticmethod
    def prueba_ks(conjunto):
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
        frecuencias_esperadas = [0.1] * 10
        frecuencias_obtenidas = [conjunto.count(i) / len(conjunto) for i in range(10)]
        chi2_estadistico = sum((obs - esp) ** 2 / esp for obs, esp in zip(frecuencias_obtenidas, frecuencias_esperadas))
        chi2_criterio = 16.919
        resultado = chi2_estadistico <= chi2_criterio
        return resultado


    @staticmethod
    def prueba_poker(conjunto):
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



