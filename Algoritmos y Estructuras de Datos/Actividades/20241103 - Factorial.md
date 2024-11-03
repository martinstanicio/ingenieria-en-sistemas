---
created: 2024-11-03 18:03:18
modified: 2024-11-03 19:07:54
title: 20241103 - Factorial
---

# 20241103 - Factorial

Diseñe una [[Algoritmos y Estructuras de Datos/Función|Función]] [[Algoritmos y Estructuras de Datos/Recursividad|Recursiva]] para calcular el factorial de un número entero pasado como parámetro. Sabemos que:

- El factorial de $0$ es $1$ y el factorial de $1$ es $1$.
- $n! = n \cdot (n - 1)!$.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo(["factorial(n)"])
    
	declarar["ans = entero"]
	inicializar["ans = 1"]
	
	if{"n > 1"}
	ans["ans = n * factorial(n - 1)"]
    
    fin(["retornar ans"])
    
    a[" "]
    
	comienzo --> declarar --> inicializar --> if
	if -- "Sí" --> ans --> a
	if -- "No" --> a
	a --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241103-factorial.py"
```
