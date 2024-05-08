# AyED
# Autor: Martín Stanicio
# Fecha: 26/04/2024

numero1 = 0.0
numero2 = 0.0
numero3 = 0.0
numero4 = 0.0
numero_mayor = 0.0

try:
    numero1 = float(input("Ingrese el número 1: "))
    numero2 = float(input("Ingrese el número 2: "))
    numero3 = float(input("Ingrese el número 3: "))
    numero4 = float(input("Ingrese el número 4: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

numero_mayor = numero1

if numero2 >= numero_mayor:
  numero_mayor = numero2

if numero3 >= numero_mayor:
  numero_mayor = numero3

if numero4 >= numero_mayor:
  numero_mayor = numero4

print(numero_mayor)