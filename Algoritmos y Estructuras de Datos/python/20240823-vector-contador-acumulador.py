# AyED
# Autor: Martín Stanicio
# Fecha: 23/08/2024

vendedores = 20

continuar = "si"
max_ventas = -1

# sumamos 1 ya que el código de vendedor 0 no existe,
# por lo que necesitamos un elemento extra en el vector
contadores = [0] * (vendedores + 1)
acumuladores = [0.0] * (vendedores + 1)

while continuar != "no":
    codigo = int(input("Código de vendedor: "))
    auto = input("Auto vendido: ")
    importe = float(input("Importe de la venta: "))

    contadores[codigo] += 1
    acumuladores[codigo] += importe

    continuar = input("Desea continuar? ")

for i in range(1, vendedores + 1):
    if contadores[i] > max_ventas:
        max_ventas = contadores[i]

    print(f"Vendedor {i}: {contadores[i]} ventas con un total de $ {acumuladores[i]}")

for i in range(1, vendedores + 1):
    if contadores[i] == max_ventas:
        print(f"El vendedor {i} realizó la mayor cantidad de ventas")
