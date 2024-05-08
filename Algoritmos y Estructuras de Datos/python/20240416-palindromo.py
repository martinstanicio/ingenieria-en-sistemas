# AyED
# Autor: Martín Stanicio
# Fecha: 16/04/2024

# Se ingresa un número entero de 4 dígitos, mostrar el número inverso.

numero_ingresado = 0
numero_ingresado_milesima = 0
numero_ingresado_centena = 0
numero_ingresado_decena = 0
numero_ingresado_unidad = 0

palindromo_milesima = 0
palindromo_centena = 0
palindromo_decena = 0
palindromo_unidad = 0
palindromo = 0

try:
    numero_ingresado = int(input("Ingrese un número de 4 dígitos: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

numero_ingresado_milesima = numero_ingresado // 1000
numero_ingresado_centesima = numero_ingresado % 1000 // 100
numero_ingresado_decena = numero_ingresado % 100 // 10
numero_ingresado_unidad = numero_ingresado % 10

palindromo_milesima = numero_ingresado_milesima * 1000
palindromo_centena = numero_ingresado_centena * 100
palindromo_decena = numero_ingresado_decena * 10
palindromo_unidad = numero_ingresado_unidad
palindromo = (
    palindromo_milesima + palindromo_centena + palindromo_decena + palindromo_unidad
)

print(palindromo)
