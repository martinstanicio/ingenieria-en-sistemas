---
created: 2024-03-22 17:32:46
modified: 2024-06-28 17:47:48
title: Función
---

# Función

Un bloque de código que puede recibir [[Parámetros]] de [[Entradas|Entrada]], ejecuta las instrucciones dadas, y ==devuelve un único valor== de [[Salidas|Salida]].

## Python

En [[Python]], las funciones se declaran de la siguiente forma.

```python
def suma(x, y):
    r = x + y
    
    return r

t = suma(a, b)
```

> [!tip]
> Para indicar la [[Salidas|Salida]] de un [[Algoritmos y Estructuras de Datos/Función|Función]] en [[Python]], utilizamos la palabra `return`.

## Diagrama de flujo

En un [[Diagrama de flujo]], las funciones se declaran de la siguiente forma.

```mermaid
flowchart TB
    comienzo([comienzo])
        
    suma["t = suma(a, b)"]
    
	fin([fin])
    
	suma_comienzo(["suma(x, y)"])
    
    a["r = x + y"]
    
	suma_retornar(["retornar(r)"])
    
	comienzo --> suma --> fin
	suma_comienzo --> a --> suma_retornar
```
