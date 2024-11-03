# AyED
# Autor: Martín Stanicio
# Fecha: 03/11/2024

micros = 50
viajes = [0] * micros
pasajeros = [0] * micros
pasajeros_semestre = [0] * 2

archivo = open("viajes.txt", "r")
registro = archivo.readline().strip()

while registro != "":
    vector = registro.split(";")

    fecha = vector[0]
    destino = vector[1]
    pasajeros = int(vector[2])
    n = int(vector[3])
