---
created: 2025-03-26 19:24:09
modified: 2025-03-26 19:48:28
title: Anagramas
---

# Anagramas

Nos sirve para saber de cuántas formas diferentes se puede ordenar un [[Conjunto]] de $k$ elementos en $n$ posiciones, donde cada elemento se repite una cierta cantidad $n_k$.

$$
\frac{n!}{n_1! \cdot n_2! \cdot \dots \cdot n_k!}
$$

> [!tip]
> Por ejemplo, la palabra ANANA contiene 2 letras en 5 posiciones, la A se repite 3 veces, y la N se repite 2 veces.
>
> $$
> \frac{5!}{3! \cdot 2!} = 10
> $$
>
> Entonces, se pueden hacer 10 anagramas con dichas letras.
