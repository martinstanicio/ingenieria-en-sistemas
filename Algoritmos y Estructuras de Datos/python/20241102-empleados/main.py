# AyED
# Autor: Martín Stanicio
# Fecha: 02/11/2024

target = input("Ingrese el departamento a analizar: ")

empleados = 0
acu_salario = 0.0
promedio_salario = 0.0
min_legajo = 9999999
empleado = [""] * 3

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

        if legajo < min_legajo:
            min_legajo = legajo
            empleado[0] = nombre
            empleado[1] = str(edad)
            empleado[2] = str(salario)

    registro = archivo.readline().strip()

archivo.close()

if empleados > 0:
    promedio_salario = acu_salario / empleados

print(f"Cantidad de empleados: {empleados}")
print(f"Salario promedio: {promedio_salario}")
print(
    f"Empleado con menor legajo: {empleado[0]} - {empleado[1]} - Salario $ {empleado[2]}"
)
