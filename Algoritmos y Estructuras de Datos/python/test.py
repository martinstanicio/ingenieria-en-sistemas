from random import randint


def insertion_sort(vector):
    elementos = len(vector)

    for i in range(0, elementos - 1):
        for j in range(i + 1, elementos):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    return vector


def bubble_sort(vector):
    elementos = len(vector)

    for _ in range(0, elementos - 1):
        for i in range(0, elementos - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

    return vector


def indexed_search(vector, valor):
    bandera = False
    ans = -1.0
    i = 0

    while i < len(vector) and not bandera:
        i += 1

        if valor >= vector[i]:
            if valor == vector[i]:
                ans = i
                bandera = True
        else:
            bandera = True

    return ans


elementos = 5
vector = [0] * elementos

for c in range(0, elementos):
    # vector[c] = int(input(f"Elemento {c + 1}: "))
    vector[c] = randint(0, 10)

print(vector)
print(indexed_search(vector, 5))
