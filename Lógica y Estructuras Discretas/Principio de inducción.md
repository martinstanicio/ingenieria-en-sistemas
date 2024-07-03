---
created: 2024-05-17 14:24:28
modified: 2024-07-03 00:55:58
title: Principio de inducción
---

# Principio de inducción

Se utiliza para probar que un [[Predicados|Predicado]] se cumple para el [[Conjunto]] de los números naturales $\mathbb{N}$.

$$
\left[ P(1) \land \forall k \geq 1: P(k) \Rightarrow P(k + 1) \right] \rightarrow \forall n \geq 1: P(n)
$$

Esta expresión puede ser dividida en un ==caso base== y un ==caso inductivo==.

## Caso base

Aquí probamos que $P(n)$ se cumple para $1$, es decir, se cumple $P(1)$.

$$
P(1)
$$

## Caso inductivo

Aquí probamos que si $P(n)$ se cumple para un elemento, también ==se cumple para su siguiente==, para todos los elementos mayores al último elemento del [[Principio de inducción#Caso base|caso base]].

$$
\forall k \geq 1: P(k) \Rightarrow P(k + 1)
$$

El antecedente se llama ==hipótesis inductiva==: $P(k)$, y el consecuente se llama ==tesis inductiva==: $P(k + 1)$.

> [!caution]
> Si para demostrar la **tesis inductiva** no tuvimos que utilizar la **hipótesis inductiva**, es una señal segura de que en alguna parte, el proceso **tiene un error**.
