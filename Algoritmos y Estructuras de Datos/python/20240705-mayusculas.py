# AyED
# Autor: Martín Stanicio
# Fecha: 05/07/2024

mayusculas = 0

frase = input("Ingrese la frase: ")

for letra in frase:
    if ord(letra) >= 65 and ord(letra) <= 90:
        mayusculas += 1

print(mayusculas)