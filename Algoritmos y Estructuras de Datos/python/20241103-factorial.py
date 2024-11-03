# AyED
# Autor: Martín Stanicio
# Fecha: 03/11/2024


def factorial(n: int) -> int:
    ans = 1

    if n > 1:
        ans = n * factorial(n - 1)

    return ans
