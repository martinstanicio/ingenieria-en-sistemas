---
aliases:
  - Control por ruptura
created: 2024-09-03 21:06:59
modified: 2024-09-09 03:18:37
title: Corte de control
---

# Corte de control

Determinar la cantidad de veces que se repite un [[Dato]] en un [[Array|Vector]].

```python
vector = [5, 10, 5, 15, 5]
```

Para esto realizamos un [[Ordenamiento]] del [[Array|Vector]].

```python
vector = [5, 5, 5, 10, 15]
```

Luego, utilizando un [[Estructura de repetición|Bucle]], aumentamos un [[Contador]] cada vez que se repite la [[Variables|Variable]] de **control**. Una vez que ya no se repite, estamos ante un **corte de control**, y debemos mostrar la cantidad de veces $z$ que se repite un número $x$.

## Diagrama de flujo

El [[Diagrama de flujo]] se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo(["bubble_sort(vector)"])
    
	variables["`elementos = entero
	_ = entero
	i = entero
	aux = real`"]
	
	elementos["elementos = largo(vector)"]
	
	for1{{"_, 1, elementos"}}
	for2{{"i, 1, elementos"}}
	if{"vector[i] > vector[i + 1]"}
	swap["`aux = vector[i]
	vector[i] = vector[i + 1]
	vector[i + 1] = aux`"]
	
	fin(["retornar vector"])
	
	a[" "]
	b[" "]
	c[" "]
    
	comienzo --> variables --> elementos --> for1 --> for2 --> if
	if -- "Sí" --> swap --> a
	if -- "No" --> a
	a --> b
	for2 --> b --> c
	for1 --> c --> fin
```

## Python

En [[Python]] se realiza de la siguiente forma.

```python
def bubble_sort(vector):
    elementos = len(vector)
    
    for _ in range(0, elementos - 1):
        for i in range(0, elementos - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux
                
    return vector
```
