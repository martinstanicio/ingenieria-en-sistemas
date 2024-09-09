# AyED
# Autor: Martín Stanicio
# Fecha: 09/09/2024


def convertir_frases(frases):
    elementos = len(frases)
    ans = [""] * elementos

    for i in range(0, elementos):
        frase = frases[i]

        for j in range(0, len(frase)):
            caracter = frase[j]
            cod = ord(caracter)

            if cod >= 65 and cod <= 90:
                ans[i] += chr(cod + 32)
            else:
                ans[i] += caracter

    return ans
