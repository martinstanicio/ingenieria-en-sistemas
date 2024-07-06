---
created: 2024-07-05 17:23:21
modified: 2024-07-05 17:55:48
title: 20240705 - Mayúsculas
---

# 20240705 - Mayúsculas

Se ingresa una frase desde teclado, mostrar la cantidad de letras mayúsculas.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`mayusculas = entero
	frase = cadena`"]
    
	frase[/horas_trabajadas/]
    
    for{{"letra, 0, largo(frase)"}}
    
    es_mayuscula["mayusculas = mayusculas + 1"]
    
    A[" "]
    mostrar{{"mayusculas"}}
    
	fin([fin])
    
	comienzo --> variables --> frase --> for
	for --> es_mayuscula --> A
	for --> A
	A --> mostrar --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240705-mayusculas.py"
```
