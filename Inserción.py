def mostrar_arreglo(arreglo): #creamos la funcion para mostrar la informacion
    print("Estado actual del arreglo:", ", ".join([f"{item['name']} ({item['code']})" for item in arreglo])) # mostramos el estado original del arreglo

def ordenamiento_insercion(arreglo):    #creo la funcion para ordenar el arreglo
    i = 1                               #inicializo mi variable en 1
    while i < len(arreglo):             #con un while indico que el limite es la longitud del arreglo
        dato = arreglo[i]               #nombro mi arreglo como dato
        j = i - 1                       #con un while indico que el limite es la longitud del arreglo

        while j >= 0 and arreglo[j]["code"] > dato["code"]:
            arreglo[j + 1] = arreglo[j]
            j -= 1

        arreglo[j + 1] = dato

        mostrar_arreglo(arreglo)

        i += 1  


arreglo_inicial = [
    { "name": "Sofía", "code": 3 },
    { "name": "Juan", "code": 4 },
    { "name": "Valentina", "code": 5 },
    { "name": "Andrés", "code": 8 },
    { "name": "Mariana", "code": 9 },
    { "name": "Camila", "code": 1 },
    { "name": "Daniel", "code": 2 },
    { "name": "Carlos", "code": 6 },
    { "name": "Isabella", "code": 7 },
    { "name": "Felipe", "code": 10 }
]


print("Arreglo inicial:")
mostrar_arreglo(arreglo_inicial)

ordenamiento_insercion(arreglo_inicial)

print("\nArreglo final ordenado:")
mostrar_arreglo(arreglo_inicial)


