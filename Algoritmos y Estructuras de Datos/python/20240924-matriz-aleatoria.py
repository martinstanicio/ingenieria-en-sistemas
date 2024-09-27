# AyED
# Autor: Martín Stanicio
# Fecha: 24/09/2024

from random import randint

matriz = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

for i in range(0, 4):
    for j in range(0, 5):
        matriz[i][j] = randint(100, 400)
