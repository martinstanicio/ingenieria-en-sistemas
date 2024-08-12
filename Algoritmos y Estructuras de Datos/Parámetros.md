---
aliases:
  - Parámetro
created: 2024-06-14 17:22:16
modified: 2024-08-06 21:23:45
title: Parámetros
---

# Parámetros

Son el medio de comunicación entre el [[Programa propio]] y una [[Algoritmos y Estructuras de Datos/Función|Función]], y viceversa.

## Parámetros formales

Son los parámetros definidos en la misma definición de la [[Algoritmos y Estructuras de Datos/Función|Función]], y actúan como [[Variables#Variables locales]] de la misma.

## Parámetros actuales

Son los valores de los parámetros pasados para una ==ejecución específica== de una [[Algoritmos y Estructuras de Datos/Función|Función]]. Suelen ser [[Variables]].

## Parámetros opcionales

Si un [[Parámetros|Parámetro]] es optional, la ejecución de la [[Algoritmos y Estructuras de Datos/Función|Función]] puede realizarse sin necesitad de darle un valor.

> [!important]
> Aunque sea opcional pasar el [[Parámetros|Parámetro]], esto no quiere decir que no existe, sino que **automaticamente** se le asigna un **valor por defecto**.

En [[Python]] podemos hacerlo de la siguiente forma, donde `pfo` es un [[Parámetros|Parámetro]] opcional.

```python
def func(pf: int, pfo: int = 0):
    ...
```
