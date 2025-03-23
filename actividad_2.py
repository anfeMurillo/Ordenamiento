def insertion_sort(arreglo):
    N = len(arreglo)
    i = 1

    while i < N:
        current = arreglo[i]  
        j = i - 1  

        while j >= 0 and arreglo[j] > current:
            arreglo[j + 1] = arreglo[j]
            j -= 1

        arreglo[j + 1] = current  
        i += 1
# Ejemplo de uso del ordenamiento por inserción
arreglo = [5, 3, 8, 1, 2, 7]
insertion_sort(arreglo)
print("Arreglo ordenado:", arreglo)