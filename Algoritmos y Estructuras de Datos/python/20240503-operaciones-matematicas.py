# AyED
# Autor: Martín Stanicio
# Fecha: 03/05/2024

numero1 = 0
numero2 = 0
operacion = ""

try:
    numero1 = int(input("Ingrese el número 1 (entero): "))
    numero2 = int(input("Ingrese el número 2 (entero): "))
    operacion = input("Ingrese la operación que desea realizar (S, R, C o M): ")
except ValueError:
    print("\nPor favor ingrese números válidos")

if operacion == "S":
    print(numero1 + numero2)
elif operacion == "R":
    print(numero1 - numero2)
elif operacion == "C":
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        print(numero1 / numero2)
elif operacion == "M":
    print(numero1 * numero2)
else:
    print("Por favor ingrese una operación válida")
