# AyED
# Autor: Martín Stanicio
# Fecha: 09/08/2024

def invertir(vector):
    largo = len(vector)
    ans = [0] * largo
    
    for i in range(largo):
        ans[largo - i - 1] = vector[i]
    
    return ans
