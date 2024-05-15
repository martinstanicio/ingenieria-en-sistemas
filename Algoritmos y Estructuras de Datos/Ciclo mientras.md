---
created: 2024-05-07 22:33:21
modified: 2024-05-14 21:14:27
title: Ciclo mientras
---

# Ciclo mientras

Es una [[Estructura de repetición]] que ejecuta una serie de instrucciones dadas **mientras** se cumpla una condición.

Para evitar que se vuelva un ciclo infinito, podemos utilizar diferentes estrategias:

- Utilizar un [[Acumulador]]
- Controlar con una opción a continuar
- Controlar con valor centinela
- Controlar con una [[Bandera]]

```mermaid
flowchart TB
	comienzo([comienzo])
    
    condicion{{"Condición"}}
    
    A[A]
    B[B]
    C[C]
    
    X[X]
    
	fin([fin])
    
	comienzo --> condicion
	condicion -- Sí --> A --> B --> C --> condicion
	condicion -- No --> X ---> fin
```

## Python

```python
c = 0

while c < 4:
    c = c + 1
    print(f"El ciclo se ejecutó {c} veces")
```
