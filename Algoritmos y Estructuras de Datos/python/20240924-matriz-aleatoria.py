# AyED
# Autor: Martín Stanicio
# Fecha: 24/09/2024

from random import randint

f = 4
c = 5
matriz = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

for i in range(0, f):
    for j in range(0, c):
        matriz[i][j] = randint(100, 400)

print(matriz)
