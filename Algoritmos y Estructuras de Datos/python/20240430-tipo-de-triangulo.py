# AyED
# Autor: Martín Stanicio
# Fecha: 30/04/2024

ladoA = 0.0
ladoB = 0.0
ladoC = 0.0

try:
    ladoA = float(input("Ingrese el lado A: "))
    ladoB = float(input("Ingrese el lado B: "))
    ladoC = float(input("Ingrese el lado C: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

if ladoA == ladoB:
    if ladoA == ladoC:
        print("Equilatero")
    else:
        print("Isosceles")
else:
    if ladoA == ladoC:
        print("Isosceles")
    else:
        if ladoB == ladoC:
            print("Isosceles")
        else:
            print("Escaleno")
