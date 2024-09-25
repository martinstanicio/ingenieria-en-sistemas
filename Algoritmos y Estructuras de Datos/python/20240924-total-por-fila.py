# AyED
# Autor: Martín Stanicio
# Fecha: 24/09/2024

def fila_mayor_total(matriz) -> int:
    elem = len(matriz)
    totales = [0] * elem
    max = -9999999
    
    for i in range(0, elem):
        for j in range(0, elem):
            totales[i] += matriz[i][j]
        
        if totales[i] > totales[max]:
            max = i
    
    return max
