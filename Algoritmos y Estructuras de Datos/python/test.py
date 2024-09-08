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

    for i in range(1, elementos):
        j = i

        while vector[j - 1] > vector[j] and j > 0:
            aux = vector[j - 1]
            vector[j - 1] = vector[j]
            vector[j] = aux

            j -= 1

    return vector


elementos = 5
vector = [0] * elementos

for c in range(0, elementos):
    # vector[c] = int(input(f"Elemento {c + 1}: "))
    vector[c] = randint(0, 100)

vector = bubble_sort(vector)

for c in range(0, elementos):
    print(vector[c])
