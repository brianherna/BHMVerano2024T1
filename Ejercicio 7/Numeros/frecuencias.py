def frecuencia_relativa(frec_abs, total):
    frec_rel = [round(abs / total, 2) for abs in frec_abs]
    return frec_rel

def frecuencia_acumulada(frec_abs):
    frec_acum = []
    acum = 0
    for abs in frec_abs:
        acum += abs
        frec_acum.append(acum)
    return frec_acum