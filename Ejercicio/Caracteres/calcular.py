import math
def calcular_rango(datos):
    valor_min = min(datos, key=len)  # Encontrar la cadena más corta como mínimo
    valor_max = max(datos, key=len)  # Encontrar la cadena más larga como máximo
    rango = len(valor_max) - len(valor_min)  # Calcular la diferencia en longitudes
    return rango, valor_min, valor_max

def calcular_numero_clases(n):
    num_clases = 1 + 3.3 * math.log10(n)
    return math.ceil(num_clases)

def calcular_ancho_clase(rango, num_clases):
    ancho_clase = rango / num_clases
    return ancho_clase

def calcular_limites_clase(valor_min, ancho_clase, num_clases):
    # Convertir las cadenas en rangos numéricos basados en la longitud de las cadenas
    limites_inferiores = [len(valor_min) + i * ancho_clase for i in range(num_clases)]
    limites_superiores = [lim_inf + ancho_clase for lim_inf in limites_inferiores]
    return limites_inferiores, limites_superiores

def calcular_marcas_clase(limites_inferiores, limites_superiores):
    marcas_clase = [(inf + sup) / 2 for inf, sup in zip(limites_inferiores, limites_superiores)]
    return marcas_clase