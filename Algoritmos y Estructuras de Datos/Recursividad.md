---
created: 2024-10-01 22:06:16
modified: 2024-10-04 17:55:29
title: Recursividad
---

# Recursividad

Cuando una [[Algoritmos y Estructuras de Datos/Función|Función]] o [[Procedimiento]] se llama a si misma.

> [!important]
> Toda [[Algoritmos y Estructuras de Datos/Función|Función]] [[Algoritmos y Estructuras de Datos/Recursividad|Recursiva]] debe tener una **condición de salida**, para que no se ejecute infinitamente.
> 
> Además, debe tener una **parte recursiva**.

Por ejemplo, algunas [[Algoritmos y Estructuras de Datos/Función|Funciones]] [[Algoritmos y Estructuras de Datos/Recursividad|Recursivas]] en [[Python]].

```python
def fibonacci(n: int):
    if n <= 1:
        ans = n
    else:
        ans = fibonacci(n - 1) + fibonacci(n - 2)
    
    return ans

def factorial(n: int):
    if n == 0:
        ans = 1
    else:
        ans = n * factorial(n - 1)
    
    return ans

def potencia(n: float, m: int):
    if m != 0:
        ans = n * potencia(n, m - 1)
    else:
        ans = 1
    
    return ans
```

## Recursividad directa

Decimos que estamos ante [[Algoritmos y Estructuras de Datos/Recursividad|Recursividad]] **directa** cuando una [[Algoritmos y Estructuras de Datos/Función|Función]] `f` se llama a si misma repetidamente.

## Recursividad indirecta

Decimos que estamos ante [[Algoritmos y Estructuras de Datos/Recursividad|Recursividad]] **indirecta** cuando tenemos una [[Algoritmos y Estructuras de Datos/Función|Función]] `f` que llama a una [[Algoritmos y Estructuras de Datos/Función|Función]] `g`, que a su vez llama a la [[Algoritmos y Estructuras de Datos/Función|Función]] `f`.
