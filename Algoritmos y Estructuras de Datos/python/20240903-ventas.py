# AyED
# Autor: Martín Stanicio
# Fecha: 03/09/2024

vendedores = 30

continuar = "si"
ventas = [0] * vendedores
facturacion = [0.0] * vendedores
promedio = [0.0] * vendedores
max_ventas = -1
max_facturacion = -1.0

while continuar != "no":
    n_vendedor = int(input("Número de vendedor: "))
    n_factura = int(input("Número de factura: "))
    fecha = input("Fecha de venta: ")
    importe = float(input("Importe de venta: "))

    ventas[n_vendedor - 1] += 1
    facturacion[n_vendedor - 1] += importe

    continuar = input("Desea continuar? ")
    print()

for i in range(0, vendedores):
    if ventas[i] != 0:
        promedio[i] = facturacion[i] / ventas[i]

    if ventas[i] > max_ventas:
        max_ventas = ventas[i]

    if facturacion[i] > max_facturacion:
        max_facturacion = facturacion[i]

    print(f"Ventas realizadas por vendedor {i + 1}: {ventas[i]}")
    print(f"Total facturado por vendedor {i + 1}: {facturacion[i]}")
    print(f"Promedio facturado por vendedor {i + 1}: {promedio[i]}")

for i in range(0, vendedores):
    if ventas[i] == max_ventas:
        print(f"El vendedor {i + 1} realizó la máxima cantidad de ventas")

    if facturacion[i] == max_facturacion:
        print(f"El vendedor {i + 1} realizó la máxima facturación")
