import math
def calcular_rango(datos):
    valor_min = min(datos)
    valor_max = max(datos)
    rango = valor_max - valor_min
    return rango, valor_min, valor_max

def calcular_numero_clases(n):  # EN CUANTAS SE DIVIDE
    num_clases = 1 + 3.3 * math.log10(n)
    return math.ceil(num_clases)  # Redondeamos hacia arriba al número entero más cercano

def calcular_ancho_clase(rango, num_clases):
    ancho_clase = rango / num_clases
    return ancho_clase

def calcular_limites_clase(valor_min, ancho_clase, num_clases):
    limites_inferiores = [valor_min + i * ancho_clase for i in range(num_clases)]
    limites_superiores = [lim_inf + ancho_clase for lim_inf in limites_inferiores]
    return limites_inferiores, limites_superiores

def calcular_marcas_clase(limites_inferiores, limites_superiores):
    marcas_clase = [(inf + sup) / 2 for inf, sup in zip(limites_inferiores, limites_superiores)]
    return marcas_clase