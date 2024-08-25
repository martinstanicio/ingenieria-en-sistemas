---
created: 2024-08-23 18:06:10
modified: 2024-08-23 18:45:22
title: 20240823 - Vector contador y acumulador
---

# 20240823 - Vector contador y acumulador

Se ingresa con opción a continuar las ventas realizadas por distintos vendedores de una empresa automotriz:

- Código de vendedor (entero)
- Auto (cadena)
- Importe (real)

El código de vendedor es un número entre 1 y 20

Mostrar:

- Cantidad de ventas realizadas por cada vendedor
- Total de importe facturado por cada vendedor 
- Código de vendedor con más ventas (puede repetirse)

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`codigo = entero
	auto = cadena
	importe = real
	continuar = cadena
	contadores[21] = entero
	acumuladores[21] = real
	max_ventas = entero`"]
	
	init["`continuar = 'Sí'
	max_ventas = -1`"]
	while{"continuar <> 'no'"}
	input[/"`codigo
	auto
	importe`"/]
	contador["contadores[codigo] += 1"]
	acumulador["acumuladores[codigo] += importe"]
	continuar[/"continuar"/]
	
	for1{{"i, 1, 21"}}
	if1{"contadores[i] > max_ventas"}
	max["max_ventas = contadores[i]"]
	vendedor{{"i"}}
	ventas{{"contadores[i]"}}
	total{{"acumuladores[i]"}}
	
	for2{{"i, 1, 21"}}
	if2{"contadores[i] = max_ventas"}
	mostrar{{"i"}}
    
    fin([fin])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    
	comienzo --> variables --> init --> while
	while -- "Sí" --> input --> contador --> acumulador --> continuar --> while
	while -- "No" --> for1
	for1 --> if1
	for1 --> a
	if1 -- "Sí" --> max --> b
	if1 -- "No" --> b
	b --> vendedor --> ventas --> total --> a --> for2
	for2 --> if2
	for2 --> d
	if2 -- "Sí" --> mostrar --> c
	if2 -- "No" --> c
	c --> d --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240823-vector-contador-acumulador.py"
```
