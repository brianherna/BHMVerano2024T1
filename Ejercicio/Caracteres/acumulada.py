def frecuencia_acumulada(frec_abs):
    frec_acum = []
    acum = 0
    for abs in frec_abs:
        acum += abs
        frec_acum.append(acum)
    return frec_acum