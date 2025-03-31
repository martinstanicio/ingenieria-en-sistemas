---
created: 2025-03-26 19:24:09
modified: 2025-03-31 11:41:23
title: Permutaciones con repetición
---

# Permutaciones con repetición

Cantidad de formas de ordenar una lista de $n$ elementos, dado un [[Conjunto]] de $m \leq n$ elementos, donde cada elemento $m_i$ se repite $k_i$ veces, de forma que $k_1 + \dots + k_m = n$.

$$
P_n(k_1, \dots, k_m) = \frac{n!}{k_1! \cdot \dots \cdot k_n!}
$$

> [!tip]
> Dada la palabra ANANA, que contiene $m = 2$ letras en $n = 5$ posiciones, sabemos que $m_1 = A \Rightarrow k_1 = 3$ (la A se repite 3 veces), y $m_2 = N \Rightarrow k_2 = 2$ (la N se repite 2 veces); se pueden formar $10$ anagramas.
>
> $$
> P_5(3, 2) = \frac{5!}{3! \cdot 2!} = 10
> $$

> [!warning]
> En clase no le asignamos un nombre a este tema, pero el tema "Permutaciones con repetición" lo asignamos a la fórmula de [[Variaciones con repetición]].
