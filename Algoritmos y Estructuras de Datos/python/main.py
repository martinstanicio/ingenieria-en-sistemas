# AyED
# Autor: Martín Stanicio
# Fecha: 07/05/2024

horas_trabajadas = 0.0
categoria = ""
premio = 0.0
valor_hora = 0.0
categoria_es_invalida = 0
sueldo = 0.0

try:
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    categoria = input("Ingrese la categoría (A, B o C): ")
    premio = float(input("Ingrese el premio: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

match categoria:
    case "A":
        valor_hora = 15000
    case "B":
        valor_hora = 10000
    case "C":
        valor_hora = 7500
    case _:
        categoria_es_invalida = 1

if categoria_es_invalida == 0:
    sueldo = horas_trabajadas * valor_hora + premio
    print(sueldo)
else:
    print("Categoría incorrecta")
