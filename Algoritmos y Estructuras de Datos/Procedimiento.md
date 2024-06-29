---
created: 2024-03-22 17:32:46
modified: 2024-06-28 17:45:40
title: Procedimiento
---

# Procedimiento

Un [[Conjunto]] de sentencias que recibe **parámetros** de [[Entradas|Entrada]], ejecuta las instrucciones dadas, y, a diferencia de una [[Análisis Matemático I/Función|Función]], puede tener una ==única [[Salidas|Salida]], múltiples, o ninguna==.

## Python

En [[Python]], los procedimientos se declaran y se utilizan de la siguente forma.

```python
def procedimiento(p1, p2, p3)
    ...
    return r1, r2, r3

x, y, z = procedimiento(v1, v2, v3)
```

## Diagrama de flujo

En un [[Diagrama de flujo]], los procedimientos se declaran y se utilizan de la siguente forma.

```mermaid
flowchart TB
    comienzo([comienzo])
        
    M1["x, y, z = M1(v1, v2, v3)"]
    
	fin([fin])
    
	M1_comienzo(["M1(p1, p2, p3)"])
    
    a["..."]
    
	M1_retornar(["retornar(r1, r2, r3)"])
    
	comienzo --> M1 --> fin
	M1_comienzo --> a --> M1_retornar
```
