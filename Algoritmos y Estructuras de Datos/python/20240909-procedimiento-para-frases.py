# AyED
# Autor: Martín Stanicio
# Fecha: 09/09/2024


def info_frases(frases):
    elementos = len(frases)
    palabras = [1] * elementos
    vocales = [0] * elementos

    for i in range(0, elementos):
        frase = frases[i]
        caracteres = len(frase)

        if caracteres == 0:
            palabras[i] = 0

        for j in range(0, caracteres):
            match frase[j]:
                case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                    vocales[i] += 1
                case " ":
                    palabras[i] += 1

    return palabras, vocales
