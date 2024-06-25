def imprimir_tabla(datos_ordenados, limites_inferiores, limites_superiores, marcas_clase, frec_absoluta, frec_relativa, frec_acumulada):
    print("{:<12} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Clase", "Límite inferior", "Límite superior", "Marca de clase", "Frec. Absoluta", "Frec. Relativa", "Frec. Acumulada (%)"))
    print("-" * 112)
    
    for i in range(len(limites_inferiores)):
        clase = f"Clase {i+1}"
        lim_inf = round(limites_inferiores[i], 2)
        lim_sup = round(limites_superiores[i], 2)
        marca = round(marcas_clase[i], 2)
        frec_abs = frec_absoluta[i]
        frec_rel = round(frec_relativa[i], 4)
        frec_acum = round(frec_acumulada[i], 2)
        print("{:<12} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(clase, lim_inf, lim_sup, marca, frec_abs, frec_rel, frec_acum))
    
    print("-" * 112)