# AyED
# Autor: Martín Stanicio
# Fecha: 12/04/2024

try:
    x = float(input("Ingrese un valor de x: "))
    y = float(input("Ingrese un valor de x: "))

    print(f"Suma = {x + y}")
    print(f"Resta = {x - y}")
    print(f"Multiplicación = {x * y}")
    print(f"Potencia = {x**y}")
    print(f"División = {x / y}")
    print(f"Cociente entero = {x // y}")
    print(f"Resto del cociente = {x % y}")
except ValueError:
    print("\nPor favor ingrese números válidos")
