---
created: 2024-11-11 15:40:46
modified: 2024-11-11 16:12:53
title: Complemento ortogonal
---

# Complemento ortogonal

Dado un [[Espacio vectorial]] $V$, y un [[Subespacio vectorial]] del mismo $W$, llamamos [[Complemento ortogonal]] $W^\bot$ al [[Conjunto]] de [[Vectores ortogonales]] a los vectores $W$.

> [!important]
> La suma entre $W$ y $W^\bot$ es [[Suma directa]].
>
> $$
> W \oplus W^\bot = V
> $$
>
> Por lo tanto, si $\dim(V) = n$, podemos afirmar lo siguiente sobre las [[Dimensión|Dimensiones]].
>
> $$
> \dim(W) + \dim(W^\bot) = n
> $$

## Espacios fundamentales

Dada una [[Matriz]] $A \in \mathbb{k}^{m \times n}$, existe una relación de **ortogonalidad** entre ciertos [[Espacio vectorial|Espacios]] fundamentales como $\ker(A)$, $\ker(A^t)$, $\text{Fil}(A)$, $\text{Fil}(A^t)$, $\text{Col}(A)$ y $\text{Fil}(A^t)$.

$$
\left( \ker(A) = \left[ \text{Fil}(A) \right]^\bot \right)
\land
\left( \ker(A^t) = \left[ \text{Col}(A) \right]^\bot = \left[ \text{Fil}(A^t) \right]^\bot \right)
$$
