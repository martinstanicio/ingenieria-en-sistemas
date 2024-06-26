# AyED
# Autor: Martín Stanicio
# Fecha: 25/06/2024

from ingresar import ingresar
from calcular import calcular
from mostrar import mostrar

apellido, horas_trabajadas, valor_hora, premio = ingresar()
sueldo = calcular(horas_trabajadas, valor_hora, premio)

mostrar(apellido, sueldo)
