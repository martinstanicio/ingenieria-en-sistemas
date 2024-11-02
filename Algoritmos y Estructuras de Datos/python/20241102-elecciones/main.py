# AyED
# Autor: Martín Stanicio
# Fecha: 02/11/2024

archivo = open("elecciones.txt", "r")
registro = archivo.readline().strip()
vector = registro.split(";")

z = 0
control = vector[0]

while registro != "":
    vector = registro.split(";")
