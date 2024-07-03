# AyED
# Autor: Martín Stanicio
# Fecha: 02/07/2024

legajo_min = 0
ingreso_min = 0
ingreso_num_min = 99999999
continuar = "si"

while continuar != "no":
    legajo = int(input("Ingrese el número de legajo: "))
    ingreso = input("Ingrese la fecha de ingreso: ")

    dia = ingreso[:2]
    mes = ingreso[3:5]
    anio = ingreso[6:]

    ingreso_num = int(anio + mes + dia)

    if ingreso_num < ingreso_num_min:
        legajo_min = legajo
        ingreso_min = ingreso

    continuar = input("Desea continuar? ")

print(f"Legajo: {legajo_min}")
print(f"Fecha de ingreso: {ingreso_min}")
