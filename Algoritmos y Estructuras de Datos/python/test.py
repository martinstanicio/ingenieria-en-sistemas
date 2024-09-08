elementos = 5
vector = [0] * elementos

for c in range(0, elementos):
    vector[c] = int(input(f"Elemento {c + 1}: "))

for fijo in range(0, elementos - 1):
    for variable in range(fijo + 1, elementos):
        if vector[fijo] > vector[variable]:
            aux = vector[fijo]
            vector[fijo] = vector[variable]
            vector[variable] = aux

for c in range(0, elementos):
    print(vector[c])
