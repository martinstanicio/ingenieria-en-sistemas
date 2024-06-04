---
created: 2024-05-07 22:33:15
modified: 2024-06-03 23:57:14
title: Ciclo desde-hasta
---

# Ciclo desde-hasta

Es una [[Estructura de repetición]] que ejecuta una serie de instrucciones dadas un ==número fijo de veces==.

Para esto, utilizamos una [[Variables|Variable]] de control, y le especificamos cuál debe ser su valor inicial y final.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
    for{{"Variable control, Valor inicial, Valor final"}}
    
    A[A]
    B[B]
    C[C]
    
    empty[" "]
    
    X[X]
    
	fin([fin])
    
	comienzo --> for
	for --> A --> B --> C --> empty --> X
	for --> empty
	X --> fin
```

## Python

```python
# Este ciclo se ejecutará 10 veces
for i in range(0, 10): # El intervalo es de la forma [0, 10)
    print(f"El ciclo se ejecutó {i} veces")
```
