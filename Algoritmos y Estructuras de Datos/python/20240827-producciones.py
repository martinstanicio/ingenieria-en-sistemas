# AyED
# Autor: Martín Stanicio
# Fecha: 27/08/2024

sucursales = 15

toneladas_producidas = [0.0] * (sucursales + 1)
cantidad_producciones = [0] * (sucursales + 1)
promedio_produccion = [0.0] * (sucursales + 1)
toneladas_por_mes = [0.0] * 13 # 12 meses, pero el mes 0 no existe
max_ton = -1.0
max_ton_repeticiones = 0
continuar = "si"

while continuar != "no":
    numero_sucursal = int(input("Numero de sucursal: "))
    ton = float(input("Toneladas producidas: "))
    fecha_produccion = input("Fecha de produccion: ")
    
    toneladas_producidas[numero_sucursal] += ton
    cantidad_producciones[numero_sucursal] += 1
    mes_produccion = int(fecha_produccion[3:5])
    toneladas_por_mes[mes_produccion] += ton
    
    continuar = input("Desea continuar? ")

for i in range(1, sucursales + 1):
    if cantidad_producciones[i] != 0:
        promedio_produccion[i] = toneladas_producidas[i] / cantidad_producciones[i]
    
    if toneladas_producidas[i] > max_ton:
        max_ton = toneladas_producidas[i]

for i in range(1, sucursales + 1):
    if toneladas_producidas[i] == max_ton:
        max_ton_repeticiones += 1

for i in range(1, sucursales + 1):
    print(f"Toneladas producidas por sucursal {i}: {toneladas_producidas[i]}")
    print(f"Cantidad de producciones por sucursal {i}: {cantidad_producciones[i]}")
    print(f"Promedio de toneladas producidas por sucursal {i}: {promedio_produccion[i]}")

print(f"Numero de sucursales con la maxima produccion: {max_ton_repeticiones}")

for i in range(1, 13):
    print(f"Toneladas producidas en mes {i}: {toneladas_por_mes[i]}")
