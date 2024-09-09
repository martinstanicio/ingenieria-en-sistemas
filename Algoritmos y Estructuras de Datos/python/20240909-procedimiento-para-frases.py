# AyED
# Autor: Martín Stanicio
# Fecha: 09/09/2024


def minuscula(frase: str):
    caracteres = len(frase)
    frase_min = ""

    for j in range(0, caracteres):
        caracter = frase[j]
        cod = ord(caracter)

    if cod >= 65 and cod <= 90:
        frase_min += chr(cod + 32)
    else:
        frase_min += caracter


def contar_palabras(frase: str) -> int:
    caracteres = len(frase)
    palabras = 1

    if caracteres == 0:
        palabras = 0

    for i in range(0, caracteres):
        if frase[i] == " ":
            palabras += 1

    return palabras


def contar_vocales(frase: str) -> int:
    frase_min = minuscula(frase)
    caracteres = len(frase)
    vocales = 0

    for i in range(0, caracteres):
        match frase_min[i]:
            case "a" | "e" | "i" | "o" | "u":
                vocales += 1


def info_frases(frases):
    elementos = len(frases)
    palabras = [0] * elementos
    vocales = [0] * elementos
