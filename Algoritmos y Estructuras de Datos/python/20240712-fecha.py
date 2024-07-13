# AyED
# Autor: Martín Stanicio
# Fecha: 12/07/2024

fecha_ingresada = input("Ingrese la fecha: ") # dd/mm/aaaa
dias_a_sumar = 15

dia = int(fecha_ingresada[:2])
mes = mes_final = int(fecha_ingresada[3:5])
anio = anio_final = int(fecha_ingresada[6:])

match mes:
    case 1 | 3 | 5 | 7 | 9 | 10 | 12:
        dias_del_mes = 31
    case 4 | 6 | 9 | 11:
        dias_del_mes = 30
    case 2:
        dias_del_mes = 28

dia_calculado = dia + dias_a_sumar

if dia_calculado > dias_del_mes:
    dia_final = dia_calculado - dias_del_mes
    mes_final = mes % 12 + 1
    
    if mes_final == 1:
        anio_final += 1
else:
    dia_final = dia_calculado

dia_cadena = ("" if dia_final >= 10 else "0") + str(dia_final)
mes_cadena = ("" if mes_final >= 10 else "0") + str(mes_final)
anio_cadena = str(anio_final)

fecha_final = dia_cadena + "/" + mes_cadena + "/" + anio_cadena
print(fecha_final)
