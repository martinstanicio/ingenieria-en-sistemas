# AyED
# Autor: Martín Stanicio
# Fecha: 03/09/2024

elementos = 100


def cantidadPalabras(frases):
    palabras = [1] * elementos
    for i in range(0, elementos):
        frase = frases[i]

        if len(frase) == 0:
            palabras[i] = 0

        for j in range(0, len(frase)):
            if frase[j] == " ":
                palabras[i] += 1

    return palabras
