---
created: 2024-05-17 14:24:28
modified: 2024-07-03 03:38:18
title: Principio de inducción fuerte modificado
---

# Principio de inducción fuerte modificado

Es igual que el [[Principio de inducción fuerte]], pero nos permite tener tantos elementos en el ==caso base== como sea conveniente.

$$
\left\{ \left[ P(b) \land \dots \land P(b + j) \right] \land \forall k \geq b + j: \left[ P(b) \land \dots \land P(k) \right] \Rightarrow P(k + 1) \right\} \rightarrow \forall n \geq b: P(n)
$$

Donde $b$ es el primer elemento, y $j$ es la cantidad de elementos en el caso base.
