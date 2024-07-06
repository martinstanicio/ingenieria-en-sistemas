# AyED
# Autor: Martín Stanicio
# Fecha: 05/07/2024

cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

palabras = 0

frase = input("Ingrese la frase: ")

for caracter in range(len(frase)):
    match frase[caracter]:
        case "a" | "A":
            cont_a += 1
        case "e" | "E":
            cont_e += 1
        case "i" | "I":
            cont_i += 1
        case "o" | "O":
            cont_o += 1
        case "u" | "U":
            cont_u += 1
        case " ":
            if caracter != 0 and caracter != len(frase) - 1:
                palabras += 1
    
    if caracter == len(frase) - 1:
        palabras += 1

print(f"Cantidad de A: {cont_a}")
print(f"Cantidad de E: {cont_e}")
print(f"Cantidad de I: {cont_i}")
print(f"Cantidad de O: {cont_o}")
print(f"Cantidad de U: {cont_u}")
print(f"Cantidad de palabras: {palabras}")
