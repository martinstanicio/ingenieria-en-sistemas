---
aliases:
  - Insertion sort
created: 2024-08-27 21:14:45
modified: 2024-09-09 02:57:53
title: Ordenamiento por inserción
---

# Ordenamiento por inserción

Dado un [[Vector|Vector]] de $n$ elementos, para realizar el [[Ordenamiento]], deberemos realizar $n - 1$ *barridos*.

Tendremos un **elemento fijo** `i`, y un **elemento variable** `j` que siempre estará a su derecha. Realizamos barridos por el vector, y en el caso de que el elemento fijo sea mayor al elemento variable.

```python
vector[i] > vector[j]
```

Realizamos un intercambio de sus valores.

```python
aux = vector[i]
vector[i] = vector[j]
vector[j] = aux

# En Python
vector[i], vector[j] = vector[j], vector[i]
```

%% 

## Concepto

Por ejemplo, con el siguiente [[Vector|Vector]].

```python
vector = [10, 5, 30, 7, 15]
```

## Barrido 1

Aquí nuestro elemento fijo será $10$, y nuestro elemento variable será $5$.

```python
vector[fijo] > vector[variable] # True
```

Por lo tanto, intercambiamos los elementos, de la siguiente forma.

```python
vector = [5, 10, 30, 7, 15]
```

Ahora nuestro elemento fijo será $5$, y nuestro elemento variable será $30$.

```python
vector[fijo] > vector[variable] # False
```

Por lo tanto, no modificamos el orden.

```python
vector = [5, 10, 30, 7, 15]
```

Ahora nuestro elemento fijo será $5$, y nuestro elemento variable será $7$.

```python
vector[fijo] > vector[variable] # False
```

Por lo tanto, no modificamos el orden.

```python
vector = [5, 10, 30, 7, 15]
```

Ahora nuestro elemento fijo será $5$, y nuestro elemento variable será $15$.

```python
vector[fijo] > vector[variable] # False
```

Por lo tanto, no modificamos el orden.

```python
vector = [5, 10, 30, 7, 15]
```

## Barrido 2

Aquí nuestro elemento fijo será $10$, y nuestro elemento variable será $30$.

> [!note]
> Los elementos anteriores al elemento fijo sabemos que ya están ordenados.

```python
vector[fijo] > vector[variable] # False
```

Por lo tanto, no modificamos el orden.

```python
vector = [5, 10, 30, 7, 15]
```

Ahora nuestro elemento fijo será $10$, y nuestro elemento variable será $7$.

```python
vector[fijo] > vector[variable] # True
```

Por lo tanto, intercambiamos los elementos, de la siguiente forma.

```python
vector = [5, 7, 30, 10, 15]
```

Ahora nuestro elemento fijo será $7$, y nuestro elemento variable será $15$.

```python
vector[fijo] > vector[variable] # False
```

Por lo tanto, no modificamos el orden.

```python
vector = [5, 7, 30, 10, 15]
```

## Barrido 3

Aquí nuestro elemento fijo será $30$, y nuestro elemento variable será $10$.

```python
vector[fijo] > vector[variable] # True
```

Por lo tanto, intercambiamos los elementos, de la siguiente forma.

```python
vector = [5, 7, 10, 30, 15]
```

Ahora nuestro elemento fijo será $10$, y nuestro elemento variable será $15$.

```python
vector[fijo] > vector[variable] # False
```

Por lo tanto, no modificamos el orden.

```python
vector = [5, 7, 10, 30, 15]
```

## Barrido 4

Aquí nuestro elemento fijo será $30$, y nuestro elemento variable será $15$.

```python
vector[fijo] > vector[variable] # True
```

Por lo tanto, intercambiamos los elementos, de la siguiente forma.

```python
vector = [5, 7, 10, 15, 30]
```

# Diagrama de flujo

Diagrama realizado en clase

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`vector[5] = entero
	auxiliar = entero
	elemento_fijo = entero
	elemento_variable = entero
	barrido = entero
	contador = entero`"]
	
	for1{{"c, 1, 6"}}
	input[/"vector[c]"/]
	
	init["`barrido = 0
	elemento_fijo = 0`"]
	
	while1{"barrido < 4"}
	while1_content1["barrido = barrido + 1"]
	while1_content2["elemento_fijo = elemento_fijo + 1"]
	while1_content3["elemento_variable = elemento_fijo"]
	
	while2{"elemento_variable < 5"}
	while2_content1["elemento_variable = elemento_variable + 1"]
	if{"vector[elemento_fijo] > vector[elemento_variable]"}
	intercambio["`auxiliar = vector[elemento_fijo]
	vector[elemento_fijo] = vector[elemento_variable]
	vector[elemento_variable] = auxiliar`"]
	
	for2{{"c, 1, 6"}}
	mostrar{{"vector[c]"}}
	
	fin([fin])
	
	a[" "]
	b[" "]
	c[" "]
	d[" "]
	e[" "]
	f[" "]
    
	comienzo --> variables --> for1
	for1 --> a
	for1 --> input --> a
	a --> init --> e --> while1
	while1 -- "Sí" --> while1_content1 --> while1_content2 --> while1_content3 --> b --> while2 -- "Sí" --> while2_content1 --> if
	if -- "Sí" --> intercambio --> c
	if -- "No" --> c
	c --> d --> b
	while2 -- "No" --> e
	while1 -- "No" --> for2 --> f
	for2 --> mostrar --> f
	f --> fin
```

 %%

## Diagrama de flujo

El [[Diagrama de flujo]] se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo(["insertion_sort(vector)"])
    
	variables["`elementos = entero
	i = entero
	j = entero
	aux = real`"]
	
	elementos["elementos = largo(vector)"]
	
	for1{{"i, 1, elementos"}}
	for2{{"j, i + 1, elementos + 1"}}
	if{"vector[i] > vector[j]"}
	swap["`aux = vector[i]
	vector[i] = vector[j]
	vector[j] = aux`"]
	
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
def insertion_sort(vector):
    elementos = len(vector)
    
    for i in range(0, elementos - 1):
        for j in range(i + 1, elementos):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux
    
    return vector
```
