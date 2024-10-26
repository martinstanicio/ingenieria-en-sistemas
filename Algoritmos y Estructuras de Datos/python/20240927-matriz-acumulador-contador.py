# AyED
# Autor: Martín Stanicio
# Fecha: 27/09/2024


matriz_c = [
    [0] * 10,
    [0] * 10,
    [0] * 10,
    [0] * 10,
]
matriz_a = [
    [0.0] * 10,
    [0.0] * 10,
    [0.0] * 10,
    [0.0] * 10,
]
toneladas = [0.0] * 4
continuar = "si"
max = -1.0

while continuar != "no":
    n = int(input("Nº de sucursal: "))
    fecha = input("Fecha de produccion: ")
    ton = float(input("Toneladas producidas: "))
    h = int(input("Nº de horno: "))
    
    matriz_c[n - 1][h - 1] += 1
    matriz_a[n - 1][h - 1] += ton

for i in range(0, 4):
    for j in range(0, 10):
        print(f"Producciones de sucursal {i + 1} horno {j + 1}: {matriz_c[i][j]}")
        print(f"Toneladas producidas por sucursal {i + 1} horno {j + 1}: {matriz_a[i][j]}")

for i in range(0, 4):    
    for j in range(0, 10):
        toneladas[i] += matriz_a[i][j]
    
    if toneladas[i] > max:
        max = toneladas[i]
    print(f"Toneladas producidas por sucursal {i + 1}: {toneladas[i]}")

for i in range(0, 4):
    if toneladas[i] == max:
        print(f"La sucursal {i + 1} tuvo la maxima produccion alcanzada")

archivo.close()
