---
created: 2024-10-01 22:06:16
modified: 2024-10-01 22:11:04
title: Recursividad
---

# Recursividad

Cuando una [[Algoritmos y Estructuras de Datos/Función|Función]] o [[Procedimiento]] se llama a si misma.

Por ejemplo, la secuencia de Fibonacci en [[Python]].

```python
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return (fibonacci(n - 1) + fibonacci(n - 2))
```

## Recursividad directa
Decimos que estamos ante [[Algoritmos y Estructuras de Datos/Recursividad|Recursividad]] **directa** cuando una [[Algoritmos y Estructuras de Datos/Función|Función]] `f` se llama a si misma repetidamente.

## Recursividad indirecta
Decimos que estamos ante [[Algoritmos y Estructuras de Datos/Recursividad|Recursividad]] **indirecta** cuando tenemos una [[Algoritmos y Estructuras de Datos/Función|Función]] `f` que llama a una [[Análisis Matemático I/Función|Función]]