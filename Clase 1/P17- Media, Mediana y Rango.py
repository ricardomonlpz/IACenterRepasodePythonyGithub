def calcular_media(lista):
    if not lista:
        return None  # Devuelve None si la lista está vacía para evitar divisiones por cero
    suma = sum(lista)
    media = suma / len(lista)
    return media

def calcular_mediana(lista):
    if not lista:
        return None  # Devuelve None si la lista está vacía
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        # Si la lista tiene un número par de elementos, la mediana es el promedio de los dos del medio.
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        mediana = (medio1 + medio2) / 2
    else:
        # Si la lista tiene un número impar de elementos, la mediana es el elemento del medio.
        mediana = lista_ordenada[n // 2]
    return mediana

def calcular_rango(lista):
    if not lista:
        return None  # Devuelve None si la lista está vacía
    maximo = max(lista)
    minimo = min(lista)
    rango = maximo - minimo
    return rango

# Crear una lista de datos numéricos
datos = [20,5,6,7,2,2]

# Calcular la media, mediana y rango de la lista
media = calcular_media(datos)
mediana = calcular_mediana(datos)
rango = calcular_rango(datos)

# Imprimir los resultados en la consola
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Rango: {rango}")