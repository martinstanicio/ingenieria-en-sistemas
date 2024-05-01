# 20240430 - Tipo de triángulo

Se ingresan los 3 lados de un triángulo, mostrar qué tipo de triángulo es según sus lados.

## Pseudocódigo

```
comienzo

declarar ladoA = real, ladoB = real, ladoC = real

leer(ladoA)
leer(ladoB)
leer(ladoC)

si ladoA == ladoB entonces
    si ladoA == ladoC entonces
        mostrar("Equilatero")
    sino
        mostrar("Isosceles")
sino
    si ladoA == ladoC entonces
        mostrar("Isosceles")
    sino
        si ladoB == ladoC entonces
            mostrar("Isosceles")
        sino
            mostrar("Escaleno")
    fin si
fin si

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables["`numero1 = real
	numero2 = real
	numero3 = real
	numero4 = real
	numero_mayor = real`"]

	leer1[/numero1/]
    leer2[/numero2/]
    leer3[/numero3/]
    leer4[/numero4/]

    numero_mayor[numero_mayor = numero1]

    si2{numero2 >= numero_mayor}
	mayor2["numero_mayor = numero2"]

    si3{numero3 >= numero_mayor}
	mayor3["numero_mayor = numero3"]

    si4{numero4 >= numero_mayor}
	mayor4["numero_mayor = numero4"]

    mostrar{{"numero_mayor"}}

	fin([fin])

	comienzo --> variables --> leer1 --> leer2 --> leer3 --> leer4 --> numero_mayor --> si2
	si2 -- Sí --> mayor2 --> si3
	si2 -- No --> si3
	si3 -- Sí --> mayor3 --> si4
	si3 -- No --> si4
	si4 -- Sí --> mayor4 --> mostrar
	si4 -- No --> mostrar
	
	mostrar --> fin
```

## Código

```python
# AyED
# Autor: Martín Stanicio
# Fecha: 30/04/2024

ladoA = 0.0
ladoB = 0.0
ladoC = 0.0

try:
    numero1 = float(input("Ingrese el lado A: "))
    numero2 = float(input("Ingrese el lado B: "))
    numero3 = float(input("Ingrese el lado C: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

if ladoA == ladoB:
    if ladoA == ladoC:
        mostrar("Equilatero")
    else:
        mostrar("Isosceles")
else:
    if ladoA == ladoC:
        mostrar("Isosceles")
    else:
        si ladoB == ladoC entonces
            mostrar("Isosceles")
        sino
            mostrar("Escaleno")
    fin si
fin si
```
