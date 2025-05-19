---
created: 2025-05-19 17:39:10
modified: 2025-05-19 18:11:06
title: Aproximación por parábolas
---

# Aproximación por parábolas

Una de las posibles formas de calcular el valor del [[Límite simultáneo]], es aproximarse mediante parábolas al punto estudiado $(x_0, y_0)$.

> [!danger]
> La [[Aproximación por parábolas]] no nos garantiza la existencia del [[Límite simultáneo]]: es una herramienta para **descartar su existencia**, o para saber cuál sería su valor en el caso de que exista.

Dado que las parábolas son de la forma $y = ax^2 + bx + c$, la ecuación de todas las parábolas que pasan por $(x_0, y_0)$ son de la siguiente forma:

$$
y_0 = ax_0^2 + bx^2 + c
\Rightarrow
y_0 = ax_0^2 + bx^2 + \left( y - ax^2 - bx \right)
\Rightarrow
y = a \left( x^2 - x_0^2 \right) + b \left( x - x_0 \right) + y_0
$$

Buscamos calcular el valor del [[Límite simultáneo]] cuando $(x, y)$ tiende hacia $(x_0, y_0)$, utilizando la ecuación anterior.

$$
\lim_{(x, y) \to (x_0, y_0)} f(x, y) =
\lim_{x \to x_0} f(x, a \left( x^2 - x_0^2 \right) + b \left( x - x_0 \right) + y_0)
$$

> [!important]
> El resultado del [[Límite]], si existiera, no debe depender del valor de los coeficientes $a$ y $b$.
