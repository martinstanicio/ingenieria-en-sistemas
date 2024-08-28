---
created: 2024-08-23 17:27:56
modified: 2024-08-25 21:44:12
title: 20240823 - Vectores paralelos
---

# 20240823 - Vectores paralelos

Se ingresan los [[Dato|Datos]] de 2000 deportistas de un club.

- Apellido (cadena)
- Nombre (cadena)
- Edad (entero)
- Peso (real)

Mostrar

- Apellido y nombre de los deportistas que tienen la mayor edad.
- Apellido, nombre y edad de los deportistas cuyo peso es menor al peso promedio.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`apellidos[2000] = cadena
	nombres[2000] = cadena
	edades[2000] = entero
	pesos[2000] = real
	max_edad = entero
	peso_sumatoria = real
	peso_promedio = real`"]
	
	init["max_edad = -1"]
	
	for1{{"i, 0, 2000"}}
	input[/"`apellidos[i]
	nombres[i]
	edades[i]
	pesos[i]`"/]
	calc_max_edad{"edades[i] > max_edad"}
	new_max_edad["max_edad = edades[i]"]
	suma_peso["peso_sumatoria = peso_sumatoria + pesos[i]"]
	
	calc_peso_promedio["peso_promedio = peso_sumatoria / 2000"]
	
	for2{{"i, 0, 2000"}}
	if_max_edad{"edades[i] = max_edad"}
	mostrar_max_edad{{"apellidos[i], nombres[i]"}}
	
	for3{{"i, 0, 2000"}}
	if_menor_a_peso_promedio{"pesos[i] < peso_promedio"}
	mostrar_menor_a_peso_promedio{{"apellidos[i], nombres[i], edades[i]"}}
	
	fin([fin])
	
	a[" "]
	b[" "]
	c[" "]
	d[" "]
	e[" "]
	f[" "]
    
	comienzo --> variables --> init --> for1
	for1 --> a
	for1 --> input --> calc_max_edad
	calc_max_edad -- "Sí" --> new_max_edad --> b
	calc_max_edad -- "No" --> b
	b --> suma_peso --> a --> calc_peso_promedio --> for2
	for2 --> c
	for2 --> if_max_edad
	if_max_edad -- "Sí" --> mostrar_max_edad --> d
	if_max_edad -- "No" --> d
	d --> c --> for3
	for3 --> e
	for3 --> if_menor_a_peso_promedio
	if_menor_a_peso_promedio -- "Sí" --> mostrar_menor_a_peso_promedio --> f
	if_menor_a_peso_promedio -- "No" --> f
	f --> e --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240823-vectores-paralelos.py"
```
