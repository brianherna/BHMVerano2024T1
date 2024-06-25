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

def crear_diagrama_barras(marcas_clase, frecuencias):
    plt.figure(figsize=(12, 6))
    
    plt.barh(marcas_clase, frecuencias,
             height=0.75, edgecolor="k",
             color=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    
    plt.yticks(marcas_clase, fontsize=15)
    plt.xlabel("Frecuencias", fontsize=20)
    plt.ylabel("Marcas de clase", fontsize=20)
    plt.title("Diagrama de barras", fontsize=25)
    plt.grid()
    plt.show()

def crear_poligono_frecuencias(marcas_clase, frecuencias):
    datos_x = [0] + list(marcas_clase) + [marcas_clase[-1] + (marcas_clase[1] - marcas_clase[0])]
    datos_y = [0] + list(frecuencias) + [0]

    plt.figure(figsize=(12, 6))
    plt.plot(datos_x, datos_y, 
             linewidth=5, color="r", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="b")

    plt.xticks(marcas_clase, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Polígono de frecuencias", fontsize=25)
    plt.grid(True)

    plt.show()

def crear_grafico_pastel(frecuencias, marcas_clase):
    plt.figure(figsize=(8, 8))
    plt.pie(frecuencias, 
            counterclock=False, 
            startangle=90, 
            autopct="%0.1f%%", 
            pctdistance=0.8, 
            colors=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"], 
            labels=marcas_clase)
    plt.title("Gráfico de pastel", fontsize=20)
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
