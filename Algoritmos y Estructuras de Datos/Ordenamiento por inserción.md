---
aliases:
  - Insertion sort
created: 2024-08-27 21:14:45
modified: 2024-08-27 22:29:37
title: Ordenamiento por inserción
---

# Ordenamiento por inserción

Dado un [[Array|Vector]] de $n$ elementos, para realizar el [[Ordenamiento]], deberemos realizar $n - 1$ *barridos*.

## Concepto

Por ejemplo, con el siguiente [[Array|Vector]].

```python
vector = [10, 5, 30, 7, 15]
```

### Barrido 1

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

### Barrido 2

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

### Barrido 3

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

### Barrido 4

Aquí nuestro elemento fijo será $30$, y nuestro elemento variable será $15$.

```python
vector[fijo] > vector[variable] # True
```

Por lo tanto, intercambiamos los elementos, de la siguiente forma.

```python
vector = [5, 7, 10, 15, 30]
```

## Diagrama de flujo

El [[Diagrama de flujo]] se realiza de la siguiente forma.

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

## Python

En [[Python]] se realiza de la siguiente forma.

```python
elementos = 5
vector = [0] * elementos

for c in range(0, elementos):
    vector[c] = int(input(f"Elemento {c + 1}: "))

elemento_fijo = 0

for barrido in range(0, elementos - 1):
    for elemento_variable in range(elemento_fijo + 1, elementos):
        if vector[elemento_fijo] > vector[elemento_variable]:
            aux = vector[elemento_fijo]
            vector[elemento_fijo] = vector[elemento_variable]
            vector[elemento_variable] = aux
    
    elemento_fijo += 1

for c in range(0, elementos):
    print(vector[c])
```
