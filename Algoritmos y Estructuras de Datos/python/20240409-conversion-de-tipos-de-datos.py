# AyED
# Autor: Martín Stanicio
# Fecha: 09/04/2024

texto_ingresado = input("Ingrese un número:\n")

try:
    numero = float(texto_ingresado)
    print(f"\nEl número ingresado fue {numero}")
except ValueError:
    print("\nPor favor ingrese un número")
