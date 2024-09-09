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
        mes = nacimientos[i][3:5]
        print(f"Apellido {apellidos[i]}, Legajo {legajos[i]}, Mes {mes}")

print()


def insertion_sort(vector):
    n = len(vector)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    return vector


def bubble_sort(vector):
    n = len(vector)

    for _ in range(0, n - 1):
        for i in range(0, n - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

    return vector


notas_ordenadas = insertion_sort(notas)
control = notas_ordenadas[0]
z = 0

for i in range(0, len(notas_ordenadas)):
    nota = notas_ordenadas[i]

    if control == nota:
        z += 1
    else:
        print(f"La nota {control} se repite {z} veces")
        control = nota
        z = 1

print(f"La nota {control} se repite {z} veces")
