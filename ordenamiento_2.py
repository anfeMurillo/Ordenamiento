empleados = [
    {"nombre": "Carlos", "edad": 29, "salario": 3000},
    {"nombre": "Ana", "edad": 25, "salario": 3500},
    {"nombre": "Luis", "edad": 32, "salario": 4000},
    {"nombre": "Marta", "edad": 28, "salario": 3200},
    {"nombre": "Pedro", "edad": 35, "salario": 4200},
    {"nombre": "Elena", "edad": 27, "salario": 2800},
    {"nombre": "Sofía", "edad": 30, "salario": 3100},
    {"nombre": "Javier", "edad": 26, "salario": 3300}
]

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  # Dividir en dos mitades
    left_half = merge_sort(arr[:mid], key)
    right_half = merge_sort(arr[mid:], key)
    
    return merge(left_half, right_half, key)

def merge(left, right, key):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Agregar elementos restantes
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

def heapify(arr, n, i, key):
    largest = i  # Nodo raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Verificar si el hijo izquierdo es mayor
    if left < n and arr[left][key] > arr[largest][key]:
        largest = left

    # Verificar si el hijo derecho es mayor
    if right < n and arr[right][key] > arr[largest][key]:
        largest = right

    # Si el mayor no es la raíz, intercambiar y seguir heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)

    # Construir el Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    # Extraer elementos del Heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el mayor con el último
        heapify(arr, i, 0, key)

def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr  # Caso base
    
    pivot = arr[len(arr) // 2][key]
    left = [x for x in arr if x[key] < pivot]  # Menores que el pivote
    middle = [x for x in arr if x[key] == pivot]  # Iguales al pivote
    right = [x for x in arr if x[key] > pivot]  # Mayores que el pivote
    
    return quick_sort(left, key) + middle + quick_sort(right, key)  # Combinar

def binary_search(arr, key, value):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][key] == value:
            return mid
        elif arr[mid][key] < value:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

def main():
    while True:
        print("Hola, bienvenido/a mi programa empresarial, ¿Qué quieres hacer?:")
        print("1. Ordenar por edad")
        print("2. Ordenar por nombre")
        print("3. Ordenar por salario")
        print("4. Buscar por edad")
        print("5. Buscar por salario")
        print("6. Salir")
        
        choice = input("Elige una opción: ")
        
        if choice == "1":
            heap_sort(empleados, "edad")
            print("Empleados ordenados por edad:", empleados)
        elif choice == "2":
            sorted_empleados = quick_sort(empleados, "nombre")
            print("Empleados ordenados por nombre:", sorted_empleados)
        elif choice == "3":
            sorted_empleados = merge_sort(empleados, "salario")
            print("Empleados ordenados por salario:", sorted_empleados)
        elif choice == "4":
            edad = int(input("Introduce la edad a buscar: "))
            heap_sort(empleados, "edad")
            index = binary_search(empleados, "edad", edad)
            if index != -1:
                print("Empleado encontrado!:", empleados[index])
            else:
                print("Empleado no encontrado")
        elif choice == "5":
            salario = int(input("Introduce el salario a buscar: "))
            merge_sort(empleados, "salario")
            index = binary_search(empleados, "salario", salario)
            if index != -1:
                print("Empleado encontrado:", empleados[index])
            else:
                print("Empleado no encontrado")
        elif choice == "6":
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

if __name__ == "__main__":
    main()
