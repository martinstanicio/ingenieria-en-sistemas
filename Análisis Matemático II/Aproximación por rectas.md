---
created: 2025-05-19 17:39:10
modified: 2025-05-19 17:47:05
title: Aproximación por rectas
---

# Aproximación por rectas

Una de las posibles formas de calcular el valor del [[Límite simultáneo]], es aproximarse mediante líneas rectas al punto estudiado $(x_0, y_0)$.

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
> El resultado del [[Límite]], si existiera, no debe depender ni de la [[Pendiente]] $m$, pues eso significaría que 