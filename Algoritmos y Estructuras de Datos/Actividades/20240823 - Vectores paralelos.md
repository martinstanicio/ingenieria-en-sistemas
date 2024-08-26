---
created: 2024-08-23 17:27:56
modified: 2024-08-23 17:50:06
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
	peso_promedio = real`"]
	
	init["max_edad = -1"]
	
	for{{"i, 0, 2000"}}
	input[/"`apellidos[i]
	nombres[i]
	edades[i]
	pesos[i]`"/]
	max_edad_calc{""}
    
    fin([fin])
    
	comienzo --> variables --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240823-vectores-paralelos.py"
```
