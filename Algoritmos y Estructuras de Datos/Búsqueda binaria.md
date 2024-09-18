---
aliases:
  - Búsqueda dicotómica
created: 2024-09-03 22:31:58
modified: 2024-09-17 21:35:31
title: Búsqueda binaria
---

# Búsqueda binaria

Dado un [[Array|Vector]] [[Ordenamiento|Ordenado]], este [[Algoritmos|Algoritmo]] divide al [[Array|Vector]] en dos subvectores de igual tamaño tantas veces como sea necesario.

> [!important]
> Al elemento que separará a las dos mitades del [[Array|Vector]], lo llamaremos **elemento central**.
> 
> Podemos obtenerlo utilizando la **división entera**.
>
> ``` python
> central = len(vector) // 2
> ```

Si el valor buscado **no existe** en ninguna de las dos mitades, retornamos $-1$. Si está en alguna de las mitades, **volvemos a realizar el mismo proceso**, hasta llegar a un único elemento, que puede o no ser el valor buscado.

> [!tip]
> El beneficio de este tipo de [[Búsqueda]] es que es capaz de generar una [[Salidas|Salida]] realizando un máximo de $\log n$ barridos, menor a otros tipos de [[Búsqueda]].

> [!important]
> El [[Array|Vector]] en cuestión debe estar [[Ordenamiento|Ordenado]].

## Diagrama de flujo

El [[Diagrama de flujo]] se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo(["binary_search(vector, valor)"])
    
	variables["`low = entero
    high = entero
    mid = entero
    ans = entero
    bandera = logica`"]
	
	inicializar["`low = 1
	high = largo(vector)
    ans = -1
    bandera = falso`"]
	
	while{"low <= high y -bandera"}
	mid["mid = (high + low) // 2"]
	if{"valor >= vector[i]"}
	low["bandera = verdadero"]
	elif{"valor = vector[i]"}
	high["ans = ibandera = verdadero"]
	ans["`bandera = ve = verdadero`"]
		
	fin(["retornar ans"])
	
	a[" "]
	b[" "]
	c[" "]
    
	comienzo --> variables --> inicializar --> a --> while
	while -- "Sí" --> mid --> if1
	if1 -- "Sí" --> if2
	if2 -- "Sï" --> if2si --> b
	if2 -- "No" --> b
	b --> c
	if1 -- "No" --> if1no --> c --> a
	while -- "No" --> fin
```

## Python

En [[Python]] se realiza de la siguiente forma.

```python
def binary_search(vector, valor):
    low = 0
    high = len(vector) - 1
    ans = -1
    bandera = False
    
    while low <= high and not bandera:
        mid = (high + low) // 2
        
        if vector[mid] < valor:
            low = mid + 1
        elif vector[mid] > valor:
            high = mid - 1
        else:
            bandera = True
            ans = mid
    
    return ans
```
