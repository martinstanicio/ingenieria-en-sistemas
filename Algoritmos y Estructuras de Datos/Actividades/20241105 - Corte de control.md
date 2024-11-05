---
created: 2024-11-05 10:18:31
modified: 2024-11-05 10:33:32
title: 20241105 - Corte de control
---

# 20241105 - Corte de control

Se tiene un [[Vector]] del tipo entero de 1000 elementos el cual se encuentra cargado y ordenado. Mostrar la cantidad de veces que se repite cada número.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo(["corte_de_control(vector)"])
    
	declarar["`n = entero
	z = entero
	control = entero
	i = entero
	e = entero`"]
	inicializar["`n = largo(vector)
	z = 0
	control = vector[1]`"]
	
	for{{"i, 1, n + 1"}}
	e["e = vector[i]"]
	
	if{"e = control"}
	z["z = z + 1"]
	mostrar1{{"`control
	z`"}}
	reset["`z = 1
	control = e`"]
	
	mostrar2{{"`control
	z`"}}
    
    fin([fin])
    
    a[" "]
    b[" "]
    
	comienzo --> declarar --> inicializar --> for --> e --> if
	if -- "Sí" --> z --> a
	if -- "No" --> mostrar1 --> reset --> a
	a --> b
	for --> b --> mostrar2 --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241105-corte-de-control.py"
```
