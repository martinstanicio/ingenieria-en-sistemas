# AyED
# Autor: Martín Stanicio
# Fecha: 18/06/2024


def calc(x: float, y: float):
    sum = x + y
    prom = sum / 2
    max = x if x > y else y

    return sum, prom, max
