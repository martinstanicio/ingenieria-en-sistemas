---
created: 2024-06-23 15:01:13
modified: 2024-06-23 15:16:52
title: Espacio de filas
---

# Espacio de filas

El [[Espacio vectorial]] de filas de una [[Matriz]] $A \in \mathbb{R}^{m \times n}$ es el [[Conjunto]] ==generado por los vectores fila== de $A$.

$$
Fil(A) = gen\{F_1, \dots, F_n\}
$$

Donde cada $F_i \in \mathbb{R}^n$.

> [!info] Base de $Fil(A)$
> Las filas **no nulas** de una [[Matriz escalonada]] $A$ son [[Conjunto linealmente independiente|Linealmente independientes]] y son una [[Base]] de $Fil(A)$.

La [[Dimensión]] del [[Espacio de filas]] también es llamado ==rango por filas==, y es igual al [[Rango]] de la [[Matriz]].

$$
dim(Fil(A)) = r_F(A) = r(A)
$$

> [!info] Equivalencia por filas
> Si dos matrices $A$ y $B$ son equivalentes por fila.
>
> $$
> Fil(A) = Fil(B)
> $$
