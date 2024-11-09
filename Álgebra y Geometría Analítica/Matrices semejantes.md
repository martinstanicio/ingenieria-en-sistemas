---
aliases:
  - Matrices similares
created: 2024-07-10 13:33:23
modified: 2024-11-09 14:40:51
title: Matrices semejantes
---

# Matrices semejantes

Sean $A$ y $B$, [[Matriz|matrices]] de $K^{n \times n}$, son ==semejantes== si $\exists C \in K^{n \times n}$, una [[Matriz inversible]] tal que se cumple lo siguiente.

$$
AC = CB
\Leftrightarrow
B = C^{-1} A C
$$

> [!important]
> Si dos [[Matriz|matrices]] son semejantes, es decir, $A \sim B$, podemos decir lo siguiente.
> 1. Tienen el mismo [[Autopolinomio|Polinomio característico]], y tienen los mismos [[Autovalor|autovalores]].
> 2. Sus [[Álgebra y Geometría Analítica/Rango|Rangos]] son iguales ($r_A = r_B$).
> 3. Sus [[Determinante|Determinantes]] son iguales ($\det(A) = \det(B)$).
