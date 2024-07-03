---
aliases:
  - Segundo principio de inducción
  - Principio de inducción completa
created: 2024-05-17 14:24:28
modified: 2024-07-03 03:23:09
title: Principio de inducción fuerte
---

# Principio de inducción fuerte

Mientras que el [[Principio de inducción matemática|Principio de inducción débil]] solo nos permite utilizar el elemento inmediatamente anterior para nuestra demostración, este principio nos permite utilizar ==cualquier elemento anterior==, pues se asume que ya se ha probado la validez del [[Predicados|Predicado]] para dicho elemento.

$$
\left\{ P(b) \land \forall k \geq 1: \left[ P(b) \land \dots \land P(k) \right] \Rightarrow P(k + 1) \right\} \rightarrow \forall n \geq 1: P(n)
$$

Resulta que $\forall n \geq b: P(n)$.
