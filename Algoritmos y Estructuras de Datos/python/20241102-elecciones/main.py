# AyED
# Autor: Martín Stanicio
# Fecha: 02/11/2024

archivo = open("elecciones.txt", "r")
registro = archivo.readline().strip()
vector = registro.split(";")

z_milei = 0
z_massa = 0
control = vector[0]

while registro != "":
    vector = registro.split(";")

    ciudad = vector[0]
    n_mesa = int(vector[1])
    v_milei = int(vector[2])
    v_massa = int(vector[3])

    if ciudad == control:
        z_milei += v_milei
        z_massa += v_massa
    else:
        print(f"Ciudad: {control}")
        print(f"Votos de Milei: {z_milei}")
        print(f"Votos de Massa: {z_massa}")
        print("")
        control = ciudad
        z_milei = 0
        z_massa = 0

    registro = archivo.readline().strip()

archivo.close()

print(f"Ciudad: {control}")
print(f"Votos de Milei: {z_milei}")
print(f"Votos de Massa: {z_massa}")
