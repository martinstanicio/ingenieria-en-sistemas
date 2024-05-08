# AyED
# Autor: Martín Stanicio
# Fecha: 19/04/2024

numero = 0.0

try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("\nPor favor ingrese un número válido")

# bifurcacion simple
if numero > 0:
    print(f"{numero} es positivo")

# bifucacion doble
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")


