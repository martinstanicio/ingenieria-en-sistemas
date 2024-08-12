# AyED
# Autor: Martín Stanicio
# Fecha: 09/08/2024

elementos = 5
numeros = [0] * elementos
suma = 0

for i in range(elementos):
    numero = int(input('Ingrese Numero entero: '))
    numeros[i] = numero
    suma += numero

promedio = suma / elementos
print(f"El promedio es: {promedio}")

for i in range(elementos):
    if numeros[i] > promedio:
        print(f"El numero {numeros[i]} en posicion {i} es mayor")
