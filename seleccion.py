A = [
    {"name": "Camila", "code": 1},
    {"name": "Daniel", "code": 2},
    {"name": "Sofía", "code": 3},
    {"name": "Juan", "code": 4},
    {"name": "Valentina", "code": 5},
    {"name": "Carlos", "code": 6},
    {"name": "Isabella", "code": 7},
    {"name": "Andrés", "code": 8},
    {"name": "Mariana", "code": 9},
    {"name": "Felipe", "code": 10}
]

def SelectionSort(A):
    N = len(A) #Tomo el tamaño de la lista
    i = 0 #Inicializo la variable i en 0
    while i < N - 1: #Mientras i sea menor a N - 1
        minIndex = i #minIndex toma el valor de i
        j = i + 1 #j tomo el valor de i + 1
        while j < N: #Mientras j sea menor a N
            if A[j]["code"] < A[minIndex]["code"]: #Si el código de la posición j es menor al codigo de la posicion minIndex
                minIndex = j #minIndex toma el valor de j
            j = j + 1 #j aumenta en 1
        if minIndex != i: #Si minIndex es diferente de i
            temp = A[i] #temp toma el valor de A[i]
            A[i] = A[minIndex] #A[i] toma el valor de A[minIndex]
            A[minIndex] = temp #A[minIndex] toma el valor de temp
        i = i + 1 #i aumenta en 1
        
    return A #Retorno la lista ordenada

print(SelectionSort(A)) #Imprimo la lista ordenada :D