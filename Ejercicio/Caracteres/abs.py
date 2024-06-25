# Funciones para calcular frecuencias absolutas, relativas y acumuladas
def frecuencia_absoluta(datos, limites_inf, limites_sup):
    frec_abs = []
    for i in range(len(limites_inf)):
        count = 0
        for dato in datos:
            if limites_inf[i] <= len(dato) < limites_sup[i]:
                count += 1
        frec_abs.append(count)
    return frec_abs