# Función para ordenar los datos por longitud de cadena
def ordenar_datos(datos):
    return sorted(datos, key=lambda x: len(x))