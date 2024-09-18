---
created: 2024-09-09 02:36:07
modified: 2024-09-17 21:52:35
title: Búsqueda indexada
---

# Búsqueda indexada

Dado un [[Vector|Vector]] [[Ordenamiento|Ordenado]], este [[Algoritmos|Algoritmo]] compara elemento por elemento hasta encontrar el valor buscado; o hasta que los valores evaluados sean **mayores al valor buscado**, lo que significa que el valor buscado **no existe** y se retornará $-1$.

> [!tip]
> El beneficio de este tipo de [[Búsqueda]] es que en la mayoría de casos, si el valor buscado no existe, es capaz de finalizar la [[Búsqueda]] sin necesidad de recorrer todo el vector.

> [!important]
> El [[Vector|Vector]] en cuestión debe estar [[Ordenamiento|Ordenado]].

## Diagrama de flujo

El [[Diagrama de flujo]] se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo(["indexed_search(vector, valor)"])
    
	variables["`bandera = logica
	ans = real
	i = entero`"]
	
	inicializar["`bandera = falso
	ans = -1
	i = 0`"]
	
	while{"i < largo(vector) y -bandera"}
	contador["i = i + 1"]
	if1{"valor >= vector[i]"}
	if1no["bandera = verdadero"]
	if2{"valor = vector[i]"}
	if2si["`ans = i
	bandera = verdadero`"]
		
	fin(["retornar ans"])
	
	a[" "]
	b[" "]
	c[" "]
    
	comienzo --> variables --> inicializar --> a --> while
	while -- "Sí" --> contador --> if1
	if1 -- "Sí" --> if2
	if2 -- "Sí" --> if2si --> b
	if2 -- "No" --> b
	b --> c
	if1 -- "No" --> if1no --> c --> a
	while -- "No" -------> fin
```

## Python

En [[Python]] se realiza de la siguiente forma.

```python
def indexed_search(vector, valor):
    bandera = False
    ans = -1
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
```
