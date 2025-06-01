---
aliases:
  - Hessiano
  - Matriz Hessiana
created: 2025-05-20 19:57:25
modified: 2025-05-31 21:23:28
title: Teorema de las segundas derivadas parciales
---

# Teorema de las segundas derivadas parciales

Un criterio que nos permite identificar [[Extremo relativo|Extremos locales]] y [[Punto silla|Puntos silla]] en los [[Punto estacionario|Puntos estacionarios]] de [[Función real de variable vectorial|Funciones reales de variable vectorial]].

Primero, se debe calcular el [[Teorema de las segundas derivadas parciales|Hessiano]] o [[Teorema de las segundas derivadas parciales|Matriz Hessiana]].

$$
H =
D =
\left\vert
    \begin{array}{c}
        f_{xx} & f_{xy} \\
        f_{yx} & f_{yy} \\
    \end{array}
\right\vert =
f_{xx} \cdot f_{yy} - f_{xy}^2
$$

- Si $H > 0$ el punto es un [[Extremo relativo|Extremo local]]
	- Si $f_{xx} > 0$ es un **mínimo**
	- Si $f_{xx} < 0$ es un **máximo**
- Si $H < 0$ el punto es un [[Punto silla]]
- Si $H = 0$ **no es suficiente** para determinar si el punto es un [[Extremo relativo|Extremo local]]
