from random import randint


def linear_search(vector, target) -> int:
    n = len(vector)
    ans = -1
    i = 0
    found = False

    while i < n and not found:
        value = vector[i]

        if value == target:
            ans = i
            found = True

        i += 1

    return ans


def indexed_search(vector, target) -> int:
    n = len(vector)
    ans = -1
    i = 0
    stop = False

    while i < n and not stop:
        value = vector[i]

        if target >= value:
            if target == value:
                ans = i
                stop = True
        else:
            stop = True

        i += 1

    return ans


def insertion_sort(vector):
    n = len(vector)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    return vector


def bubble_sort(vector):
    n = len(vector)

    for _ in range(0, n - 1):
        for i in range(0, n - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

    return vector


def corte_control(vector):
    n = len(vector)
    control = vector[0]
    z = 0

    for i in range(0, n):
        value = vector[i]

        if value == control:
            z += 1
        else:
            print(f"El número {control} se repite {z} veces")
            control = vector[i]
            z = 1

    print(f"El número {control} se repite {z} veces")


numbers = [randint(0, 10) for _ in range(0, 100)]
print(numbers)

print(f"{insertion_sort(numbers)=}")
# print(f"{bubble_sort(numbers)=}")
