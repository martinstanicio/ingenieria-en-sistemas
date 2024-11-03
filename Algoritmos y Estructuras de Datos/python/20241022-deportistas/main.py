target = input("Ingrese el deporte que desea analizar (f, b, v): ")

deportistas = 0
altura_acumulador = 0.0
altura_promedio = 0.0
max_edad = 0

archivo = open("deportistas.txt", "r")
registro = archivo.readline().strip()

while registro != "":
    vector = registro.split(";")
    altura = float(vector[2])
    edad = int(vector[3])
    deporte = vector[4]

    if deporte == target:
        deportistas += 1
        altura_acumulador += altura
        if edad > max_edad:
            max_edad = edad

    registro = archivo.readline().strip()

archivo.close()

if deportistas > 0:
    altura_promedio = altura_acumulador / deportistas

print(f"Deportistas: {deportistas}")
print(f"Promedio de altura: {altura_promedio}")
print(f"Mayor edad: {max_edad}")
