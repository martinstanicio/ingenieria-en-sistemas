---
created: 2024-08-20 22:08:29
modified: 2024-08-20 22:40:16
title: 20240820 - Empleados
---

# 20240820 - Empleados

Se ingresan los datos de 500 empleados:

- Legajo
- Apellido
- Edad
- Sueldo

Mostrar legajo, apellido y sueldo de las personas que tienen la mayor edad

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`legajos[500] = entero
	apellidos[500] = cadena
	edades[500] = entero
	sueldos[500] = real
	max_edad = entero
	i = entero`"]
	max_edad["max_edad = -1"]
	
	for1{{"i, 0, 500"}}
	input[/"`legajos[i]
	apellidos[i]
	edades[i]
	sueldos[i]`"/]
	
	for2{{"i, 0, 500"}}
	if2{"edades[i] > max_edad"}
	new_max["max_edad = edades[i]"]
	
	for3{{"i, 0, 500"}}
	if3{"edades[i] = max_edad"}
	mostrar{{"`legajos[i]
	apellidos[i]
	sueldos[i]`"}}
	
	a[" "]
	b[" "]
	c[" "]
	d[" "]
	e[" "]
    
    fin([fin])
    
	comienzo --> variables --> max_edad --> for1
	for1 --> input --> a
	for1 --> a
	a --> for2
	for2 --> if2
	for2 --> c
	if2 -- Sí --> new_max --> b
	if2 -- No --> b
	b --> c --> for3
	
	for3 --> if3
	for3 --> e
	if3 -- Sí --> mostrar --> d
	if3 -- No --> d
	d --> e --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240820-empleados.py"
```
