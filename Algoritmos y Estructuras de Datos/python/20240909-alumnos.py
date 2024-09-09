# AyED
# Autor: Martín Stanicio
# Fecha: 09/09/2024

alumnos = int(input("Cantidad de alumnos: "))
apellidos = [""] * alumnos
legajos = [0] * alumnos
nacimientos = [""] * alumnos
notas = [0.0] * alumnos

max_nota = -1.0

for i in range(0, alumnos):
    print(f"Alumno {i + 1}")
    apellidos[i] = input("Apellido: ")
    legajos[i] = int(input("Legajo: "))
    nacimientos[i] = input("Fecha de nacimiento (dd/mm/aaaa): ")
    notas[i] = float(input("Nota: "))
    print()

    if notas[i] > max_nota:
        max_nota = notas[i]

print(f"Nota máxima: {max_nota}")

for i in range(0, alumnos):
    if notas[i] == max_nota:
        print(f"{apellidos[i]}, {legajos[i]}, {nacimientos[i]}")
