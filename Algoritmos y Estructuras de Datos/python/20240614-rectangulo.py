# AyED
# Autor: Martín Stanicio
# Fecha: 14/06/2024

def rectangulo(largo: int, altura: int):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print("*"*largo)
        else:
            print("*" + " "*(largo - 2) + "*")
            
rectangulo(4, 5)
