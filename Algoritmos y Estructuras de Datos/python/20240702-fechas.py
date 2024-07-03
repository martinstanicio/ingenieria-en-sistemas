# AyED
# Autor: Martín Stanicio
# Fecha: 02/07/2024


def fecha_a_numero(fecha: str):
    dia = fecha[:2]
    mes = fecha[3:5]
    anio = fecha[6:]

    return int(anio + mes + dia)


# fecha tiene el formato: "dd/mm/aaaa"
fecha_a = input("Ingrese la fecha A: ")
fecha_b = input("Ingrese la fecha B: ")

fecha_a_num = fecha_a_numero(fecha_a)
fecha_b_num = fecha_a_numero(fecha_b)

print(fecha_a if fecha_a_num < fecha_b_num else fecha_b)
