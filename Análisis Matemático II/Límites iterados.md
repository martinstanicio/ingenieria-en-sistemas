---
aliases:
  - Límites reiterados
created: 2025-03-26 16:17:17
modified: 2025-05-19 18:28:01
title: Límites iterados
---

# Límites iterados

Una de las posibles formas de calcular el valor del [[Límite simultáneo]], es mediante el cálculo de sus [[Límites iterados]].

> [!danger]
> Los [[Límites iterados]] no nos garantizan la existencia del [[Límite simultáneo]]: es una herramienta para **descartar su existencia**, o para saber cuál sería su valor en el caso de que exista.

Se hace tender una variable hacia su [[Límite]], manteniendo constante la otra; luego, se hace tender la otra variable hacia su [[Límite]].

$$
L_1 = \lim_{x \to a} \left( \lim_{x \neq a, y \to b} f(x, y) \right)
\land
L_2 = \lim_{y \to b} \left( \lim_{y \neq b, x \to a} f(x, y) \right)
$$

Si ambos [[Límite|Límites]] existen, y también existe el [[Límite simultáneo]], se verifica lo siguiente.

$$
L = L_1 = L_2
$$

Si los [[Límites iterados]] existen y son distintos, el [[Límite simultáneo]] ==no existe==.

> [!warning]
> Si los [[Límites iterados]] existen y son iguales, o alguno de ellos no existe, **no se puede afirmar nada** sobre la existencia del [[Límite simultáneo]].
