---
created: 2025-05-19 17:39:10
modified: 2025-05-19 17:57:35
title: Aproximación por rectas
---

# Aproximación por rectas

Una de las posibles formas de calcular el valor del [[Límite simultáneo]], es aproximarse mediante líneas rectas al punto estudiado $(x_0, y_0)$.

> [!danger]
> La [[Aproximación por rectas]] no nos garantiza la existencia del [[Límite simultáneo]]: es una herramienta para **descartar su existencia**, o para saber cuál sería su valor en el caso de que exista.

Sabemos que la ecuación de todas las rectas que pasan por $(x_0, y_0)$ son de la siguiente forma:

$$
y - y_0 = m (x - x_0)
\Rightarrow
y = mx - mx_0 + y_0
$$

Buscamos calcular el valor del [[Límite simultáneo]] cuando $(x, y)$ tiende hacia $(x_0, y_0)$, utilizando la ecuación anterior.

$$
\lim_{(x, y) \to (x_0, y_0)} f(x, y) =
\lim_{x \to x_0} f(x, mx - mx_0 + y_0)
$$

> [!important]
> El resultado del [[Límite]], si existiera, no debe depender del valor de la [[Pendiente]] $m$.
