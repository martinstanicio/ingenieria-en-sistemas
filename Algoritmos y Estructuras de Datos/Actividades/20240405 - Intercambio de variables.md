---
created: 2024-04-05 19:52:34
modified: 2024-05-08 01:33:31
title: 20240405 - Intercambio de variables
---

# 20240405 - Intercambio de variables

Se ingresan dos números reales en las variables `a` y `b` respectivamente. Realizar un algoritmo para intercambiar los contenidos y mostrarlos por pantalla.

## Pseudocódigo

```
comienzo

declarar a = real, b = real, c = real

leer(a)
leer(b)

c = a
a = b
b = c

mostrar(a)
mostrar(b)

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables["`a = real
	b = real
	c = real`"]

	leerA[/a/]
	leerB[/b/]
	
	c["c = a"]
	a["a = b"]
	b["b = c"]

	mostrar{{"`a
	b`"}}
	
	fin([fin])

	comienzo --> variables --> leerA --> leerB --> c --> a --> b --> mostrar --> fin
```
