# AyED
# Autor: Martín Stanicio
# Fecha: 05/11/2024

vendedores = 40

ventas = [0] * vendedores
importes = [0.0] * vendedores
meses = [0.0] * 12

max_ventas = -1

archivo = open("ventas.txt", "r")
registro = archivo.readline().strip()

while registro != "":
    vector = registro.split(";")

    n = int(vector[0])
    fecha = vector[1]
    importe = float(vector[2])

    mes = int(fecha[3:5])

    ventas[n - 1] += 1
    importes[n - 1] += importe
    meses[mes - 1] += importe

    registro = archivo.readline().strip()

archivo.close()

for i in range(0, vendedores):
    print(f"Ventas realizadas por vendedor {i + 1}: {ventas[i]}")
    print(f"Importe facturado por vendedor {i + 1}: {importes[i]}")

    if ventas[i] > max_ventas:
        max_ventas = ventas[i]

for i in range(0, 12):
    print(f"Importe facturado en el mes {i + 1}: {meses[i]}")

for i in range(0, vendedores):
    if ventas[i] == max_ventas:
        print(f"El vendedor {i + 1} realizó la máxima cantidad de ventas.")
