# AyED
# Autor: Martín Stanicio
# Fecha: 25/06/2024

from ingresar import ingresar
from calcular import calcular
from mostrar import mostrar

masa, altura, velocidad = ingresar()
mecanica = calcular(masa, altura, velocidad)

mostrar(mecanica)
