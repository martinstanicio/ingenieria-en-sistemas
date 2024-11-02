# AyED
# Autor: Martín Stanicio
# Fecha: 02/11/2024

target = input("Ingrese el departamento a analizar: ")

empleados = 0
acu_salario = 0.0
promedio_salario = 0.0
min_edad = 9999
joven = [0, "", 0.0]

archivo = open("empleados.dat", "r")
registro = archivo.readline().strip()

while registro != "":
    vector = registro.split(";")

    legajo = int(vector[0])
    nombre = vector[1]
    edad = int(vector[2])
    departamento = vector[3]
    salario = float(vector[4])

    if departamento == target:
        empleados += 1
        acu_salario += salario

        if edad < min_edad:
            min_edad = edad
            joven[0] = legajo
            joven[1] = nombre
            joven[2] = salario

    registro = archivo.readline().strip()

archivo.close()

if empleados > 0:
    promedio_salario = acu_salario / empleados

print(f"Cantidad de empleados: {empleados}")
print(f"Salario promedio: {promedio_salario}")
print(f"Empleado más joven: Legajo {joven[0]} - {joven[1]} - Salario $ {joven[2]}")
