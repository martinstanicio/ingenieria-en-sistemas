# AyED
# Autor: Martín Stanicio
# Fecha: 03/11/2024


from random import randint


def bubble_sort(vector):
    n = len(vector)

    for _ in range(0, n - 1):
        for i in range(0, n - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

    return vector


def binary_search(vector, target: int) -> int:
    n = len(vector)
    ans = -1

    high = n - 1
    low = 0
    found = False

    while not found and target >= vector[low] and target <= vector[high]:
        mid = (high + low) // 2

        if vector[mid] == target:
            ans = mid
            found = True
        elif target > vector[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return ans


elementos = 10
vector = [0] * elementos

for i in range(0, elementos):
    vector[i] = randint(100, 999)

vector = bubble_sort(vector)

for i in range(0, elementos):
    if i > 0:
        print(", ", end="")
    print(vector[i], end="")
print()

target = int(input("Ingrese el número de ID a buscar: "))
ans = binary_search(vector, target)

if ans == -1:
    print(f"No se ha encontrado ningún artículo con ID {target}.")
else:
    print(f"El artículo está en la posición {ans}.")
