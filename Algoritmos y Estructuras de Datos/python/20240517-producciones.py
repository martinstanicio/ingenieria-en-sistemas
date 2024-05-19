# AyED
# Autor: Martín Stanicio
# Fecha: 17/05/2024

numero_horno = 0
toneladas_producidas = 0.0
bandera = True
toneladas_horno_1 = 0.0
toneladas_horno_2 = 0.0
toneladas_horno_3 = 0.0

numero_horno = 0
bandera = True
toneladas_horno_1 = 0.0
toneladas_horno_2 = 0.0
toneladas_horno_3 = 0.0

while bandera:
    toneladas_producidas = float(input("Ingrese las toneladas producidas: "))
    numero_horno = int(input("Ingrese el número de horno: "))
    
    match numero_horno:
        case 1:
            toneladas_horno_1 = toneladas_horno_1 + toneladas_producidas
        case 2:
            toneladas_horno_2 = toneladas_horno_2 + toneladas_producidas
        case 3:
            toneladas_horno_3 = toneladas_horno_3 + toneladas_producidas
        case -1:
            bandera = False

print("Toneladas producidas por el horno 1: ", toneladas_horno_1)
print("Toneladas producidas por el horno 2: ", toneladas_horno_2)
print("Toneladas producidas por el horno 3: ", toneladas_horno_3)