# AyED
# Autor: Martín Stanicio
# Fecha: 02/11/2024

import shutil

target = int(input("ID del cliente a eliminar: "))

shutil.copy("clientes.txt", "backup.txt")

clientes = open("clientes.txt", "r")
backup = open("backup.txt", "w")
registro = clientes.readline().strip()
eliminado = False

while registro != "":
    vector = registro.split(";")
    id_cliente = int(vector[0])
    nombre = vector[1]
    edad = int(vector[2])
    ciudad = vector[3]

    if id_cliente != target:
        backup.write(registro + "\n")
    else:
        eliminado = True
        print(f"Cliente eliminado: {id_cliente} - {nombre} - {edad} - {ciudad}")

    registro = clientes.readline().strip()

clientes.close()
backup.close()

shutil.copy("backup.txt", "clientes.txt")

if not eliminado:
    print(f"No existe un cliente con id: {target}")
