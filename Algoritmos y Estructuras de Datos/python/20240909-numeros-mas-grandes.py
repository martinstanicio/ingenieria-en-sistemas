# AyED
# Autor: Martín Stanicio
# Fecha: 09/09/2024


def insertion_sort(vector):
    n = len(vector)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if vector[i] < vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    return vector


def bubble_sort(vector):
    n = len(vector)

    for _ in range(0, n - 1):
        for i in range(0, n - 1):
            if vector[i] < vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

    return vector


elementos = 40
numeros = [0] * elementos

for i in range(0, elementos):
    numeros[i] = int(input("Ingrese un número: "))

numeros = insertion_sort(numeros)

for i in range(0, 4):
    print(numeros[i])
