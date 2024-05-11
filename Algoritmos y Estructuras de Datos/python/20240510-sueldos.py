# AyED
# Autor: Martín Stanicio
# Fecha: 10/05/2024

import sys

sueldo = 0.0
cantidad_de_empleados = 0
contador_empleado = 0
sumatoria_de_sueldos = 0.0
promedio_de_sueldos = 0.0

cantidad_de_empleados = 5
contador_empleado = 0

while contador_empleado < cantidad_de_empleados:
    contador_empleado = contador_empleado + 1
    
    try:
        sueldo = float(input(f"Ingrese el sueldo del empleado {contador_empleado}: "))
    except ValueError:
        print("\nPor favor ingrese números válidos")
        sys.exit()
    
    sumatoria_de_sueldos = sumatoria_de_sueldos + sueldo

promedio_de_sueldos = sumatoria_de_sueldos / cantidad_de_empleados

print("Sumatoria de sueldos: ", sumatoria_de_sueldos)
print("Promedio de sueldos: ", promedio_de_sueldos)
