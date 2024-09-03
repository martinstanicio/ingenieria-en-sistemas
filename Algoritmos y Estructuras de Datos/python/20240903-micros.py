# AyED
# Autor: Martín Stanicio
# Fecha: 03/09/2024

continuar = "si"
micros = 20

viajes = [0] * (micros + 1)
acu_pasajeros = [0] * (micros + 1)
max_viajes = 999999
min_viajes = -1

while continuar != "no":
    n_micro = int(input("Numero de micro: "))
    destino = input("Destino: ")
    fecha = input("Fecha: ")
    pasajeros = int(input("Numero de pasajeros: "))

    viajes[n_micro] += 1
    acu_pasajeros[n_micro] += pasajeros

for i in range(1, micros + 1):
    if viajes[i] > max_viajes:
        max_viajes = viajes[i]
    if viajes[i] < min_viajes:
        min_viajes = viajes[i]

for i in range(1, micros + 1):
    print(f"Cantidad de viajes de micro {i}: {viajes[i]}")
    print(f"Pasajeros transportados por micro {i}: {acu_pasajeros[i]}")

for i in range(1, micros + 1):
    if viajes[i] == max_viajes:
        print(f"Micro con max viajes: {i}")
    if viajes[i] == min_viajes:
        print(f"Micro con min viajes: {i}")
