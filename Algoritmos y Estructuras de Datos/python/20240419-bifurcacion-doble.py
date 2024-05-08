# AyED
# Autor: Martín Stanicio
# Fecha: 19/04/2024

numero = 0.0

try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("\nPor favor ingrese un número válido")

if numero >= 0:
    print("Positivo")
else:
    print("Negativo")
