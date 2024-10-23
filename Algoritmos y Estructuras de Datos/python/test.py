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
