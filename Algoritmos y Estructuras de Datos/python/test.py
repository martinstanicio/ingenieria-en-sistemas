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


elementos = 5
vector = [0] * elementos

for c in range(0, elementos):
    # vector[c] = int(input(f"Elemento {c + 1}: "))
    vector[c] = randint(0, 100)

vector = insertion_sort(vector)

for c in range(0, elementos):
    print(vector[c])
