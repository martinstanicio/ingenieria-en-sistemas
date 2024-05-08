---
created: 2024-04-09 21:02:32
modified: 2024-05-08 01:33:31
title: 20240409 - Circunferencia
---

# 20240409 - Circunferencia

Se ingresa el radio de una circunferencia. Calcular el área y perímetro.

## Pseudocódigo

```
comienzo

declarar pi = real, radio = real, perimetro = real, area = real

pi = 3.14

leer(radio)

perimetro = 2 * pi * radio
area = pi * radio^2

mostrar(perimetro)
mostrar(area)

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables["`pi = real
	radio = real
	perimetro = real
	area = real`"]

	pi["pi = 3.14"]

	leer[/radio/]

	perimetro["perimetro = 2 * pi * radio"]
	area["area = pi * radio^2"]

	mostrar{{"`perimetro
	area`"}}
	
	fin([fin])

	comienzo --> variables --> pi --> leer --> perimetro --> area --> mostrar --> fin
```
