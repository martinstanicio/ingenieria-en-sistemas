# AyED
# Autor: Martín Stanicio
# Fecha: 09/04/2024

base = 0.0
altura = 0.0
area = 0.0


try:
    base = float(input("Ingrese la base del triángulo\n"))
    altura = float(input("Ingrese la altura del triángulo\n"))

    area = base * altura / 2

    print(f"El área del triángulo es {area}")
except ValueError:
    print("\nPor favor ingrese números válidos")
