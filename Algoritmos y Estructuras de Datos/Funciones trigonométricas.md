---
created: 2024-06-11 21:14:16
modified: 2024-06-11 21:41:10
title: Funciones trigonométricas
---

# Funciones trigonométricas

Para utilizar [[Algoritmos y Estructuras de Datos/Función|funciones]] trigonométricas en [[Python]], debemos ==importar== la [[Biblioteca]] `math`.

> [!warning]
> Las funciones trigonométricas en [[Python]] trabajan con **radianes**.

```python
import math

x = math.sin(2 * math.pi) # seno
y = math.cos(math.pi) # coseno
z = math.tan(3 * math.pi / 4) # tangente
```

## Grados y radianes

Para realizar la ==conversión== de grados a radianes, o viceversa, podemos utilizar las funciones `math.radians` y `math.degrees` respectivamente.

```python
import math

a = math.radians(180) # pi
b = math.degrees(2 * math.pi) # 360°
```

## Funciones adicionales

```python
import math

x = 1 / math.cos(2 * math.pi) # secante
y = 1 / math.sin(math.pi) # cosecante
z = 1 / math.tan(3 * math.pi / 4) # cotangente

a = math.asin(2 * math.pi) # arcoseno
b = math.acos(math.pi) # arcocoseno
c = math.atan(3 * math.pi / 4) # arcotangente
```
