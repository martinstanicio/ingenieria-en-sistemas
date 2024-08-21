# AyED
# Autor: Martín Stanicio
# Fecha: 20/08/2024

elementos = 5
vector = [""] * elementos
registro = input("Ingresar datos: ")
largo = len(registro)

x = e = 0

while x < largo:
    if registro[x] == ";":
        e += 1
    else:
        vector[e] += registro[x]

    x += 1

for i in range(0, elementos):
    print(vector[i])
