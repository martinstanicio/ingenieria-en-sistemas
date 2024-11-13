---
created: 2024-11-13 17:36:13
modified: 2024-11-13 17:44:18
title: Matriz de proyección
---

# Matriz de proyección

Podemos calcular la [[Proyección]]  $\hat{y}$ de un vector $u$ sobre un [[Subespacio vectorial]] $S$, sin necesidad de tener una [[Base ortogonal]] de $S$.

$$
\hat{y} = \text{proy}_S u
$$

Sea $B$ una [[Base]] de $S$, no necesariamente [[Base ortogonal|Ortogonal]], y $A$ una [[Matriz]] cuyas columnas son los vectores de $B$, podemos calcular la [[Matriz de proyección]] $M$ de la siguiente forma.

$$
M = A \cdot \left( A^t A \right)^{-1} \cdot A^t
$$

Y esto nos permite calcular la [[Proyección]] de $u$ sobre $S$ mediante esta operación.

$$
\hat{y} = \text{proy}_S u = M \cdot u
$$
