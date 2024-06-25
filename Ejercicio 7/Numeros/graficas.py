import matplotlib.pyplot as plt

def crear_histograma(marcas_clase, frecuencias):
    plt.figure(figsize=(8, 6))
    plt.bar(marcas_clase, frecuencias, edgecolor="k",
           color=["#F190C1", "#E79DF1", "#C190F1", "#A1F190", "#E7F190"])
    
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.show()
def crear_ojiva(marcas_clase, frecuencias):
    frec_acumulada = [sum(frecuencias[:i+1]) for i in range(len(frecuencias))]
    
    datos_x = [0] + marcas_clase + [marcas_clase[-1] + (marcas_clase[1] - marcas_clase[0])]
    datos_y = [0] + frec_acumulada + [frec_acumulada[-1]]

    plt.figure(figsize=(12, 6))  # Ancho, alto de la figura

    # Trazar la ojiva
    plt.plot(datos_x, datos_y, 
             linewidth=5, color="r", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="b")

    # Configuraciones adicionales del gráfico
    plt.xticks(marcas_clase, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias acumuladas", fontsize=20)
    plt.title("Ojiva", fontsize=25)
    plt.grid(True)  # Activar la cuadrícula

    plt.show()  # Mostrar el gráfico