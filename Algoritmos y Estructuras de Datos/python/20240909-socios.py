# AyED
# Autor: Martín Stanicio
# Fecha: 09/09/2024

socios = 4000
numeros = [0] * socios
apellidos = [""] * socios
edades = [0] * socios

min_edad = 999999

for i in range(0, socios):
    numeros[i] = int(input("Número de socio: "))
    apellidos[i] = input("Apellido: ")
    edades[i] = int(input("Edad: "))

    if edades[i] < min_edad:
        min_edad = edades[i]
