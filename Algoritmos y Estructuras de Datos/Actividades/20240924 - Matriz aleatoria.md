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
	comienzo(["fila_mayor_total(matriz)"])
    
	variables["`totales[50] = real
	max = entero
	i = entero
	j = entero`"]
	inicializar["`max = 0`"]
	for1{{"i, 0, 50"}}
	totales["totales[i] = 0.0"]
	
	for2{{"i, 0, 50"}}
	for3{{"j, 0, 50"}}
	acu["totales[i] = totales[i] + matriz[i, j]"]
	
	if{"totales[i] > totales[max]"}
	max["max = i"]
    
    fin(["retornar max"])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    
	comienzo --> variables --> inicializar --> for1 --> totales --> a
	for1 --> a --> for2 --> for3 --> acu --> b
	for3 --> b --> if
	if -- "Sí" --> max --> c
	if -- "No" --> c
	c --> d
	for2 --> d --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240924-matriz-aleatoria.py"
```
