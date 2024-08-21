# AyED
# Autor: Martín Stanicio
# Fecha: 20/08/2024

empleados = 500
legajos = [0] * empleados
apellidos = [""] * empleados
edades = [0] * empleados
sueldos = [0.0] * empleados

max_edad = -1

for i in range(empleados):
    print(f"Empleado {i + 1}")
    legajos[i] = int(input("Legajo: "))
    apellidos[i] = input("Apellido: ")
    edades[i] = int(input("Edad: "))
    sueldos[i] = float(input("Sueldo: "))
    print("\n")

for i in range(empleados):
    if edades[i] > max_edad:
        max_edad = edades[i]

for i in range(empleados):
    if edades[i] == max_edad:
        print(f"Legajo {legajos[i]} - Apellido {apellidos[i]} - Sueldo {sueldos[i]}")
