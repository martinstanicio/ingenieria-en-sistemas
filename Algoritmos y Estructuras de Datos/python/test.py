from random import randint


def insertion_sort(vector):
    elementos = len(vector)

    for fijo in range(0, elementos - 1):
        for variable in range(fijo + 1, elementos):
            if vector[fijo] > vector[variable]:
                aux = vector[fijo]
                vector[fijo] = vector[variable]
                vector[variable] = aux

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


elementos = 5
vector = [0] * elementos

for c in range(0, elementos):
    # vector[c] = int(input(f"Elemento {c + 1}: "))
    vector[c] = randint(0, 100)

vector = bubble_sort(vector)

for c in range(0, elementos):
    print(vector[c])
