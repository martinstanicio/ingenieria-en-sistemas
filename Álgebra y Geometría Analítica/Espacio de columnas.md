---
created: 2024-06-23 15:01:13
modified: 2024-06-23 15:53:33
title: Espacio de columnas
---

# Espacio de columnas

El [[Espacio vectorial]] de columnas de una [[Matriz]] $A \in \mathbb{R}^{m \times n}$ es el [[Conjunto]] ==generado por los vectores columna== de $A$.

$$
Col(A) = gen\{C_1, \dots, C_n\}
$$

Donde cada $C_i \in \mathbb{R}^m$.

> [!info] Base de $Col(A)$
> Las columnas **pivot** de una [[Matriz escalonada]] $A$ nos indican qué columnas de la **[[Matriz]] original** son [[Conjunto linealmente independiente|Linealmente independientes]] y una [[Base]] de $Col(A)$.

La [[Dimensión]] del [[Espacio de columnas]] también es llamado ==rango por columnas==, y es igual al [[Álgebra y Geometría Analítica/Rango|Rango]] de la [[Matriz]].

$$
dim(Col(A)) = r_C(A) = r(A)
$$

> [!info] Imagen de una matriz
> La [[Imagen]] de una [[Matriz]] $A$ es igual a su [[Espacio de columnas]]
>
> $$Im(A) = Col(A)$$
