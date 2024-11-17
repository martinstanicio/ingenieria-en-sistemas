---
aliases:
  - Ring
created: 2024-08-09 13:18:02
modified: 2024-11-17 16:23:57
title: Anillo
---

# Anillo

Una [[Estructura algebráica]] formada por un [[Conjunto]] $R$ y dos [[Operación|Operaciones]] $\#$ y $*$.

$$
\left( R, \#, * \right)
$$

Además, deben cumplirse las siguientes condiciones.

1. La [[Estructura algebráica]] $(R, \#)$ debe ser [[Grupo abeliano]].
2. La [[Estructura algebráica]] $(R, *)$ debe ser [[Semigrupo]].
3. La segunda [[Operación]] debe ser distributiva sobre la primera.

## Divisores de cero

Si en un [[Anillo]] $\left( R, +, \cdot \right)$ con $0$ el [[Elemento neutro]] de $\left( R, + \right)$, si se cumple lo siguiente, decimos que el [[Anillo]] ==no tiene divisores de cero==.

$$
\forall a \in R \forall b \in R: (a \cdot b = 0) \Rightarrow (a = 0 \lor b = 0)
$$

Si existiera un par de elementos $a$ y $b$ cuyo resultado al ser operados es diferente de $0$, entonces decimos que $a$ y $b$ son divisores de cero.
