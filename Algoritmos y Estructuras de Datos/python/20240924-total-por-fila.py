# AyED
# Autor: Martín Stanicio
# Fecha: 24/09/2024


def fila_mayor_total(matriz) -> int:
    e = len(matriz)
    totales = [0] * e
    max = 0

    for i in range(0, e):
        for j in range(0, e):
            totales[i] += matriz[i][j]

        if totales[i] > totales[max]:
            max = i

    return max
