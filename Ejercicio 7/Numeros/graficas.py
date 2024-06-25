import matplotlib.pyplot as plt

def crear_histograma(marcas_clase, frec_relativa):
    plt.figure(figsize=(8, 5))
    plt.bar(marcas_clase, frec_relativa, width=0.8, edgecolor="k", color="#F190C1")
    
    plt.xlabel("Datos", fontsize=15)
    plt.ylabel("Frecuencia relativa", fontsize=15)
    plt.title("Histograma de frecuencias relativas", fontsize=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.show()

def crear_ojiva(marcas_clase, frec_acumulada):
    plt.figure(figsize=(10, 6))
    plt.plot(marcas_clase, frec_acumulada, marker='o', linestyle='-', color='r', markersize=8)
    
    plt.xlabel("Datos", fontsize=15)
    plt.ylabel("Frecuencia acumulada", fontsize=15)
    plt.title("Ojiva de frecuencia acumulada", fontsize=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.show()