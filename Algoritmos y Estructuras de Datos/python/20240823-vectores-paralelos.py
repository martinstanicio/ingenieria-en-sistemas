# AyED
# Autor: Martín Stanicio
# Fecha: 23/08/2024

deportistas = 2000

apellidos = [""] * deportistas
nombres = [""] * deportistas
edades = [0] * deportistas
pesos = [0.0] * deportistas

max_edad = -1
peso_sumatoria = 0

for i in range(deportistas):
    apellidos[i] = input("Apellido: ")
    nombres[i] = input("Nombre: ")
    edades[i] = int(input("Edad: "))
    pesos[i] = float(input("Peso: "))
    print("")

    if edades[i] > max_edad:
        max_edad = edades[i]

    peso_sumatoria += pesos[i]

peso_promedio = peso_sumatoria / deportistas

for i in range(deportistas):
    if edades[i] == max_edad:
        print(f"El deportista '{apellidos[i]}, {nombres[i]}' tiene la mayor edad")

for i in range(deportistas):
    if pesos[i] < peso_promedio:
        print(
            f"El deportista '{apellidos[i]}, {nombres[i]}' de {edades[i]} años, tiene un peso menor al promedio"
        )
