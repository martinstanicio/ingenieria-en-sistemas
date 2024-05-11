# AyED
# Autor: Martín Stanicio
# Fecha: 10/05/2024

cantidad_de_deportistas = 0
cantidad_de_hombres = 0
cantidad_de_mujeres = 0
sumatoria_de_edad = 0
promedio_de_edad = 0.0
continuar = ""
apellido = ""
edad = 0
sexo = ""

cantidad_de_deportistas = 0
continuar = ""
cantidad_de_hombres = 0
cantidad_de_mujeres = 0
sumatoria_de_edad = 0

while continuar != "no":
    try:
        apellido = input("Ingrese el apellido del deportista: ")
        apellido = int(input("Ingrese la edad del deportista: "))
        sexo = input("Ingrese el sexo del deportista (H o M): ")
    except ValueError:
        print("\nPor favor ingrese números válidos")
        continue

    cantidad_de_deportistas = cantidad_de_deportistas + 1
    sumatoria_de_edad = sumatoria_de_edad + edad

    match sexo:
        case "H":
            cantidad_de_hombres = cantidad_de_hombres + 1
        case "M":
            cantidad_de_mujeres = cantidad_de_mujeres + 1
        case _:
            print("Sexo no contemplado")

    continuar = input("Si desea dejar de ingresar deportistas, ingrese 'no': ")


promedio_de_edad = sumatoria_de_edad / cantidad_de_deportistas

print("Cantidad de deportistas: ", cantidad_de_deportistas)
print("Cantidad de hombres: ", cantidad_de_hombres)
print("Cantidad de mujeres: ", cantidad_de_mujeres)
print("Promedio de edad: ", promedio_de_edad)
