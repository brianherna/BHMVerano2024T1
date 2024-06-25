def frecuencia_relativa(frec_abs, total):
    frec_rel = [round(abs / total, 2) for abs in frec_abs]
    return frec_rel