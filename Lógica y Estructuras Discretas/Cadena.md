---
aliases:
  - Cadena de símbolos
  - Cadenas
created: 2025-02-27 19:44:50
modified: 2025-06-07 16:40:57
title: Cadena
---

# Cadena

Si $w \in \Sigma^k$, con $k \geq 1$, entonces $w$ se llama una [[Lógica y Estructuras Discretas/Cadena|Cadena]] de $k$ símbolos del [[Alfabeto]] $\Sigma$.

> [!tip]
> Un [[Conjunto]] ordenado de elementos de un [[Alfabeto]].

## Longitud

Sea $w$ una [[Lógica y Estructuras Discretas/Cadena|Cadena de símbolos]] del [[Alfabeto]] $\Sigma$.

$$
\text{long}(w) =
\Vert w \Vert =
\left\{
    \begin{array}{c}
        0 \space \text{si} \space w = \lambda \\
        1 + \text{long}(w') \space \text{si} \space w = aw' \wedge a \in \Sigma \wedge w' \space \text{una cadena}
    \end{array}
\right.
$$

## Igualdad

Dos [[Lógica y Estructuras Discretas/Cadena|Cadenas]] $w_1 = x_1 \dots x_n$ y $w_2 = y_1 \dots y_m$ son ==iguales== si se cumple lo siguiente.

$$
w_1 = w_2
\Leftrightarrow
n = m \wedge \forall u \in \set{1, \dots, n}: x_i = y_i
$$
