---
created: 2025-06-14 20:21:30
modified: 2025-06-17 14:59:24
title: Lema de bombeo
---

# Lema de bombeo

Dado $\Sigma$ un [[Alfabeto]], se cumple que para todo [[Lenguaje regular]] $L$ sobre $\Sigma$ y $M = \left< K, \Sigma, \delta, q_0, F \right>$ tal que $L \left( M \right) = L$:

$$
\forall p > n, n = \vert K \vert: \forall \alpha \in L, \vert \alpha \vert \geq p \left( \exists x, y, z \in \Sigma^*: \alpha = xyz \land \vert xy \vert \leq p \land \vert y \vert \geq 1 \right)
\Rightarrow
\forall i \geq 0: xyz \in L
$$

==**FALTA COMPLETAR**==


$$
\left( \forall L \right) \left( \exists p \right) \left( \forall \alpha \right): \alpha \in L \land \vert \alpha \vert \geq p \Rightarrow \left[ \exists x, y, z \in \Sigma^*: \alpha = xyz \land \vert xy \vert \leq p \land \vert y \vert \geq 1 \land \left() \right]
$$