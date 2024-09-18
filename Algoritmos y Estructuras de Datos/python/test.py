filas = 3
columnas = 4
matriz = [[0 for _ in range(columnas)] for _ in range(filas)]


for f in range(0, filas):
    for c in range(0, columnas):
        num = int(input("Número: "))
        matriz[f][c] = num
