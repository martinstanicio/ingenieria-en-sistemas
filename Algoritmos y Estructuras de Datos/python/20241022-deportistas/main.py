# El usuario ingresa el deporte cuyas estadísticas queremos analizar. Mostrar:

# - Cantidad de deportistas
# - Promedio de altura de las personas que practican ese deporte
# - Mayor edad de la persona que practica ese deporte

target = input("Ingrese el deporte que desea analizar (f, b, v): ")

deportistas = 0
altura_acumulador = 0.0
altura_promedio = 0.0
max_edad = 0

archivo = open("socios.txt", "r")
registro = archivo.readline()

while registro != "":
    vector = registro.split(";")
    print(vector[0])
    print(vector[1])
    print(vector[2])
    print(vector[3])
    print(vector[4])
    registro = archivo.readline()

archivo.close()
