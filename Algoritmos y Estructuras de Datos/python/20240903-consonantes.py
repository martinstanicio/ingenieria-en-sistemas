# AyED
# Autor: Martín Stanicio
# Fecha: 03/09/2024


def consonantes(frase: str) -> int:
    ans = 0

    for i in range(0, len(frase)):
        caracter = frase[i]
        codigo = ord(caracter)

        if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
            if (
                caracter != "a"
                and caracter != "A"
                and caracter != "e"
                and caracter != "E"
                and caracter != "i"
                and caracter != "I"
                and caracter != "o"
                and caracter != "O"
                and caracter != "u"
                and caracter != "U"
            ):
                ans += 1

    return ans
