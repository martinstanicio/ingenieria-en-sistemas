---
created: 2024-09-24 22:27:52
modified: 2024-09-26 14:22:48
title: 20240924 - Matriz aleatoria
---

# 20240924 - Matriz aleatoria

Cargar una [[Vector multidimensional|Matriz]] de $4 \times 5$ con números aleatorios comprendidos en $[100, 400]$ cargando por fila.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`matriz[4, 5] = entero
	i = entero
	j = entero`"]
	
	for1{{"i, 0, 4"}}
	for2{{"j, 0, 5"}}
	random["matriz[i, j] = aleatorio(100, 400)"]
	
	fin([fin])
    
    a[" "]
    b[" "]
    
	comienzo --> variables --> for1 --> for2 --> random --> a
	for2 --> a --> b
	for1 --> b --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240924-matriz-aleatoria.py"
```
	