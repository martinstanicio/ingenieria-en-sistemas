---
aliases:
  - Matriz
created: 2024-09-17 22:29:06
modified: 2024-09-17 22:36:29
title: Vector multidimensional
---

# Vector multidimensional

Un [[Vector]] ==multidimensional==, es un ==[[Vector]] de [[Vector|Vectores]]==. Por lo tanto, también podemos considerarlas [[Matriz|Matrices]]. Por ejemplo, en [[Python]], una [[Matriz]] bidimensional de $3 \times 3$:

```python
matriz = [[1, 2, 3],
		  [4, 5, 6],
		  [7, 8, 9]]
```

O una [[Matriz]] tridimensional de $2 \times 2 \times 2$:

```python
matriz = [[[1, 2], [3, 4]],
		  [[5, 6], [7, 8]]]
```

## Diagrama de flujo

El [[Diagrama de flujo]] se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declaracion["nombre_matriz[filas, columnas] = tipo_de_dato"]
        
	fin([fin])
    
	comienzo --> declaracion --> fin
```

## Python

En [[Python]] se realiza de la siguiente forma.

```python
nombre_matriz = [valor_inicial] * elementos
```

## Asignación de [[Dato|Datos]]

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declaracion["`matriz[3, 4] = entero
	num = entero
	f = entero
	c = entero`"]
	declaracion["`matriz[3, 4] = entero
	num = entero
	f = entero
	c = entero`"]
	
	for1{{"f, 0, 4"}}
	for2{{"c, 0, "}}
        
	fin([fin])
    
	comienzo --> declaracion --> for1 --> fin
```
