---
created: 2025-03-03 18:16:21
modified: 2025-03-03 18:29:41
title: K-Equivalencia
---

# K-Equivalencia

Dos [[Lógica y Estructuras Discretas/Estado|Estados]] de una [[Máquina de estados finitos|MEF]] son $0$-equivalentes si tienen la misma [[Salidas|Salida]], y son $k$-equivalentes si tienen la misma [[Salidas|Salida]], y para todo carácter de [[Entradas|Entrada]], sus [[Lógica y Estructuras Discretas/Estado|Estados]] siguientes son $(k - 1)$-equivalentes.

Por lo tanto, para cualquier arreglo de [[Entradas|Entrada]] de longitud menor o igual a $k$, la [[Salidas|Salida]] de la [[Máquina de estados finitos|MEF]] será la misma, independientemente del [[Lógica y Estructuras Discretas/Estado|Estado]] inicial elegido.

## Teorema

Los [[Lógica y Estructuras Discretas/Estado|Estados]] $q_i$ y $q_j$ están en la misma clase de equivalencia $\pi_k$, es decir, son $k$-equivalentes, si y solo si están en el mismo bloque $\pi_{k - 1}$, es decir, ya eran $(k - 1)$-equivalentes, y $\forall a \in I$ (para todo carácter de [[Entradas|Entrada]]) sus [[Lógica y Estructuras Discretas/Estado|Estados]] siguientes están en la misma clase $\pi_{k - 1}$.
