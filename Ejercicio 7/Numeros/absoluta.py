def frecuencia_absoluta(datos, limites_inferiores, limites_superiores):
    frec_absoluta = []
    
    for inf, sup in zip(limites_inferiores, limites_superiores):
        contador = sum(1 for dato in datos if inf <= dato < sup)
        frec_absoluta.append(contador)
    
    return frec_absoluta