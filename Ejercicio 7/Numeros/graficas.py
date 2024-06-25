import matplotlib.pyplot as plt

def crear_histograma(marcas_clase, frecuencias):
    plt.figure(figsize=(12, 6))
    plt.bar(marcas_clase, frecuencias,
           width=1, edgecolor="k",
           color=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.show()


def crear_ojiva(marcas_clase, frecuencias):
    frec_acumulada = [sum(frecuencias[:i+1]) for i in range(len(frecuencias))]
    
    datos_x = [0] + marcas_clase + [marcas_clase[-1] + (marcas_clase[1] - marcas_clase[0])]
    datos_y = [0] + frec_acumulada + [frec_acumulada[-1]]

    plt.figure(figsize=(12, 6))

    plt.plot(datos_x, datos_y, 
             linewidth=5, color="r", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="b")

    plt.xticks(marcas_clase, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias acumuladas", fontsize=20)
    plt.title("Ojiva", fontsize=25)
    plt.grid(True)

    plt.show()