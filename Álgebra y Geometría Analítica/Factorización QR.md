---
created: 2024-11-13 11:52:10
modified: 2024-11-13 12:08:13
title: Factorización QR
---

# Factorización QR

Sea $A \in k^{m \times n}$ una [[Matriz]] con columnas [[Conjunto linealmente independiente|Linealmente independientes]], luego existen [[Matriz|Matrices]] únicas $Q$ y $R$ tal que:

$$
A = QR
$$

> [!tip]
> Si las columnas son [[Conjunto linealmente independiente|Linealmente independientes]], entonces forman una [[Base]] del [[Espacio de columnas]] $\text{Col}(A)$ de la [[Matriz]].

Donde $Q$ es de $m \times n$ cuyas columnas son una [[Base ortonormal]] para el [[Espacio de columnas]] $\text{Col}(A)$. Y $R$ es una [[Matriz triangular]] superior de $n \times n$, con todos los elementos de su diagonal principal positivos.
