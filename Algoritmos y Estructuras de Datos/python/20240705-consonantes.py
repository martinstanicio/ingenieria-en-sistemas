# AyED
# Autor: Martín Stanicio
# Fecha: 05/07/2024

consonantes = 0

frase = input("Ingrese la frase: ")

for caracter in frase:
    if (ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):
        if caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u" and caracter != "A" and caracter != "E" and caracter != "I" and caracter != "O" and caracter != "U":
            consonantes += 1

print(f"Cantidad de consonantes: {consonantes}")
