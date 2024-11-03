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

    f = vector[0]
    d = vector[1]
    p = int(vector[2])
    n = int(vector[3])

    mes = int(f[5:7])

    viajes[n - 1] += 1
    pasajeros[n - 1] += p

    pasajeros_semestre[1 if mes > 6 else 0] += p

    registro = archivo.readline().strip()

archivo.close()

for i in range(0, micros):
    print(f"Viajes realizados por micro {i + 1}: {viajes[i]}")
    print(f"Pasajeros transportados por micro {i + 1}: {pasajeros[i]}")

for i in range(0, 2):
    print(f"Pasajeros transportados en semestre {i + 1}: {pasajeros_semestre[i]}")
