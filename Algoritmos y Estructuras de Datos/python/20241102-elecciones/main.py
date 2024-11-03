# AyED
# Autor: Martín Stanicio
# Fecha: 02/11/2024

archivo = open("elecciones.txt", "r")
registro = archivo.readline().strip()
vector = registro.split(";")

max_milei = -1
ciudad_milei = ""
max_massa = -1
ciudad_massa = ""

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

        if z_milei > max_milei:
            max_milei = z_milei
            ciudad_milei = control

        if z_massa > max_massa:
            max_massa = z_massa
            ciudad_massa = control

        control = ciudad
        z_milei = v_milei
        z_massa = v_massa

    registro = archivo.readline().strip()

archivo.close()

print(f"Ciudad: {control}")
print(f"Votos de Milei: {z_milei}")
print(f"Votos de Massa: {z_massa}")

print("")
print(f"Ciudad con mas votos de Milei: {ciudad_milei}")
print(f"Ciudad con mas votos de Massa: {ciudad_massa}")
