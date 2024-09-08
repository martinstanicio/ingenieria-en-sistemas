---
created: 2024-09-03 19:19:44
modified: 2024-09-08 19:53:26
title: 20240903 - Cantidad de palabras
---

# 20240903 - Cantidad de palabras

Realizar una función llamada `cantidadPalabras` con las siguientes características:

- Recibe como parámetro a `frases` que es un vector de 100 elementos del tipo string.
- Debera retornar al programa principal un vector de 100 elementos del tipo entero con la cantidad de palabras que hay en cada elemento del vector `frases` que recibe como parámetro de entrada.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo(["cantidadPalabras(frases)"])
    
	variables["`palabras[100] = entero
	i = entero
	j = entero
	frase = cadena`"]
	
	for1{{"i, 1, 100"}}
	frase["frase = frases[i]"]
	if1{"largo(frase) = 0"}
	if1si["palabras[i] = 0"]
	for2{{"j, 1, largo(frase)"}}
	if2{"frase[j] = ' '"}
	if2si["palabras[i] = palabras[i] + 1"]
    
    fin(["retornar palabras"])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    
	comienzo --> variables --> for1 --> frase --> if1
	if1 -- "Sí" --> if1si --> a
	if1 -- "No" --> a
	a --> for2 --> if2
	if2 -- "Sí" --> if2si --> b
	if2 -- "No" --> b
	b --> c
	for2 --> c --> d
	for1 --> d --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240903-cantidad-de-palabras.py"
```
