# AyED
# Autor: Martín Stanicio
# Fecha: 16/04/2024

numero = 0
valor_absoluto = 0

try:
    numero = int(input("Ingrese un número entero: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

valor_absoluto = (numero**2)**0.5

print(int(valor_absoluto))
