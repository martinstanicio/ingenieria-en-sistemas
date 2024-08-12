# AyED
# Autor: Martín Stanicio
# Fecha: 09/08/2024

elementos = 100
frases = [""] * elementos
cantidades = [0] * elementos
max = 0

for i in range(0, elementos):
    frase = input("Ingresar frase: ")
    frases[i] = frase
    cantidades[i] = 0
    
    for j in range(0, len(frase)):
        if frase[j] == " ":
            cantidades[i] += 1 

for i in range(0, elementos):
    if cantidades[i] > max:
        max = cantidades[i]

for i in range(0, elementos):
    if cantidades[i] == max:
        print(frases[i])
