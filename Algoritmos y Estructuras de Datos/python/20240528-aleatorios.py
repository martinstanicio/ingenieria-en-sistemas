# AyED
# Autor: Martín Stanicio
# Fecha: 28/05/2024

from random import randint

cantidad_pares = 0
cantidad_impares = 0
contador = 0
numero = 0.0

cantidad_pares = 0
cantidad_impares = 0

while contador < 10:
    numero = randint(50, 101)
    
    if numero % 2 == 0:
        cantidad_pares = cantidad_pares + 1
    else:
        cantidad_impares = cantidad_impares + 1
    
    contador = contador + 1

print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_impares}")