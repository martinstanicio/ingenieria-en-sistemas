# AyED
# Autor: Martín Stanicio
# Fecha: 05/11/2024


def corte_de_control(vector) -> None:
    n = len(vector)

    z = 0
    control = vector[0]

    for i in range(0, n):
        e = vector[i]

        if e == control:
            z += 1
        else:
            print(f"El elemento {control} se repite {z} veces")
            z = 1
            control = e

    print(f"El elemento {control} se repite {z} veces")
