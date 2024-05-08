# AyED
# Autor: Martín Stanicio
# Fecha: 16/04/2024

x = 0 + 0j
y = 0 + 0j

suma = 0 + 0j
resta = 0 + 0j
multiplicacion = 0 + 0j
division = 0 + 0j

try:
    x = complex(input("Ingrese un complejo x: "))
    y = complex(input("Ingrese un complejo y: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
