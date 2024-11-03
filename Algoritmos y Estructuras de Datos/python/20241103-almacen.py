# AyED
# Autor: Martín Stanicio
# Fecha: 03/11/2024


def bubble_sort(vector):
    n = len(vector)

    for _ in range(0, n - 1):
        for i in range(0, n - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux
