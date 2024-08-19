---
created: 2024-08-15 13:57:36
modified: 2024-08-19 16:23:05
title: Reglas de diferenciación
---

# Reglas de diferenciación

Reglas para calcular el [[Diferencial]] de diferentes [[Análisis Matemático I/Función|Funciones]].

## Suma

Dada las [[Análisis Matemático I/Función|Funciones]] $y = f(x)$ y $z = f(x)$ **derivables** en $x$.

$$
d(y + x) = dy + dz
$$

Como podemos ver en la siguiente demostración.

$$
d(y + z) =
(y + z)' \cdot dx =
(y' + z') \cdot dx =
y' \cdot dx + z' \cdot dx =
dy + dz
$$

## Producto

Dada las [[Análisis Matemático I/Función|Funciones]] $y = f(x)$ y $z = f(x)$ **derivables** en $x$.

$$
d(y \cdot x) = z \cdot dy + y \cdot dz
$$

Como podemos ver en la siguiente demostración.

$$
d(y \cdot z) =
(y \cdot z)' \cdot dx =
(y' \cdot z + y \cdot z') \cdot dx =
z \cdot y' \cdot dx + y \cdot z' \cdot dx =
z \cdot dy + y \cdot dz
$$
