def frecuencia_relativa(frecuencias, total_datos):
    frec_relativa = [frec / total_datos for frec in frecuencias]
    return frec_relativa

def frecuencia_acumulada(frecuencias):
    total_datos = sum(frecuencias)
    frec_acumulada = [sum(frecuencias[:i+1]) / total_datos * 100 for i in range(len(frecuencias))]
    return frec_acumulada