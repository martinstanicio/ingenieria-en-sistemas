---
created: 2024-04-16 22:23:00
modified: 2024-05-08 01:33:31
title: 20240416 - Triángulo rectángulo
---

# 20240416 - Triángulo rectángulo

Se ingresan los catetos de un triángulo rectángulo, hallar la hipotenusa.

## Pseudocódigo

```
comienzo

declarar cateto_a = real, cateto_b = real, hipotenusa = entero

leer(cateto_a)
leer(cateto_b)

hipotenusa = √(cateto_a^2 + cateto_b^2)

mostrar(hipotenusa)

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables["`cateto_a = real
	cateto_b = real
	hipotenusa = real`"]

	leer_cateto_a[/"Cateto A"/]
	leer_cateto_b[/"Cateto B"/]

	hipotenusa["hipotenusa = √(cateto_a^2 + cateto_b^2)"]

	mostrar{{"hipotenusa"}}
	
	fin([fin])

	comienzo --> variables --> leer_cateto_a --> leer_cateto_b --> hipotenusa --> mostrar --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240416-triangulo-rectangulo.py"
```
