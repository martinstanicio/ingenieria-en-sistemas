---
aliases:
  - Primer principio de inducción
  - Principio de inducción matemática
  - Principio de inducción incompleta
created: 2024-05-17 14:24:28
modified: 2024-07-03 03:28:24
title: Principio de inducción débil
---

# Principio de inducción débil

Se utiliza para probar que un [[Predicados|Predicado]] se cumple para el [[Conjunto]] de los números naturales $\mathbb{N}$.

$$
\left[ P(b) \land \forall k \geq 1: P(k) \Rightarrow P(k + 1) \right] \rightarrow \forall n \geq b: P(n)
$$

Esta expresión puede ser dividida en un ==caso base== y un ==caso inductivo==.

## Caso base

Aquí probamos que $P(n)$ se cumple para $b$, es decir, se cumple $P(b)$.

$$
P(b)
$$

Donde $b$ es el primer elemento del [[Subconjunto]] de los naturales con el que estemos trabajando, que suele ser $1$

## Caso inductivo

Aquí probamos que si $P(n)$ se cumple para un elemento, también ==se cumple para su siguiente==, para todos los elementos mayores o iguales al último elemento del [[Principio de inducción débil#Caso base|caso base]].

$$
\forall k \geq b: P(k) \Rightarrow P(k + 1)
$$

El antecedente se llama ==hipótesis inductiva==: $P(k)$, y el consecuente se llama ==tesis inductiva==: $P(k + 1)$.

> [!caution]
> Si para demostrar la **tesis inductiva** no tuvimos que utilizar la **hipótesis inductiva**, es una señal segura de que en alguna parte, el proceso **tiene un error**.
