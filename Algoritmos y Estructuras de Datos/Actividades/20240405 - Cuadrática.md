---
created: 2024-04-05 17:51:50
modified: 2024-05-08 01:33:31
title: 20240405 - Cuadrática
---

# 20240405 - Cuadrática

Se ingresan los términos A,B, y C de la función cuadrática. Hallar las raices y mostrarlas por pantalla.

## Pseudocódigo

```
comienzo

declarar a = real, b = real, c = real

leer(a)
leer(b)
leer(c)

declarar discriminante = real, raiz1 = real, raiz2 = real

discriminante = b^2 - 4 * a * c

raiz1 = (-b + √discriminante) / 2 * a
raiz2 = (-b - √discriminante) / 2 * a

mostrar(raiz1)
mostrar(raiz2)

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables1["`a = real
	b = real
	c = real`"]

	a[/a/]
	b[/b/]
	c[/c/]

	variables2["`discriminante = real
	raiz1 = real
	raiz2 = real`"]

	discriminante["discriminante = b^2 - 4 * a * c"]
	raiz1["raiz1 = (-b + √discriminante) / 2 * a"]
	raiz2["raiz2 = (-b - √discriminante) / 2 * a"]

	mostrar{{"`raiz1
	raiz2`"}}
	
	fin([fin])

	comienzo --> variables1 --> a --> b --> c --> variables2 --> discriminante --> raiz1 --> raiz2 --> mostrar --> fin
```
