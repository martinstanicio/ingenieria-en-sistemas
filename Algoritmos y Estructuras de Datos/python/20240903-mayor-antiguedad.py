# AyED
# Autor: Martín Stanicio
# Fecha: 03/09/2024

continuar = "si"
min_ingreso = 99999999

legajo = ""
sueldo = 0.0

while continuar != "no":
    l = int(input("Legajo: "))
    s = float(input("Sueldo: "))
    f = input("Fecha: ")

    dia = f[:2]
    mes = f[3:5]
    anio = f[6:]

    fecha = int(anio + mes + dia)

    if fecha < min_ingreso:
        min_ingreso = fecha
        legajo = l
        sueldo = s

    continuar = input("Desea continuar? ")

print(f"Legajo: {legajo}")
print(f"Sueldo: {sueldo}")
