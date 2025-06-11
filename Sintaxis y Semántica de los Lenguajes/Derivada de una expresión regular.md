---
aliases:
  - Derivada de una ER
created: 2025-06-11 13:47:31
modified: 2025-06-11 14:03:00
title: Derivada de una expresión regular
---

# Derivada de una expresión regular

Podemos definir la [[Derivada]] de una [[Expresión regular]] de la siguiente forma.

1. $\partial_\lambda \left( u \right) = u$, para $u$ una [[Expresión regular|ER]]
2. Para cada $a \in \Sigma$:
	- $\partial_a \left( \emptyset \right) = \emptyset$
	- $\partial_a \left( \lambda \right) = \emptyset$
	- $\partial_a \left( b \right) = \lambda$ si $a = b$
	- $\partial_a \left( b \right) = \emptyset$ si $a \neq b$
3. Si $u$ y $v$ son dos [[Expresión regular|ER]]:
	- $\partial_a \left( u + v \right) = \partial_a \left( u \right) + \partial_a \left( v \right)$
	- $\partial_a \left( uv \right) = \partial_a \left( u \right)v + T \left( u \right) \partial_a \left( v \right)$, donde $T \left( u \right) = \left\{ \begin{array}{c} \emptyset \space \text{si} \space L \left( u \right) \space \text{no contiene a} \space \lambda \\ \set{ \lambda } \space \text{si} \space L \left( u \right) \space \text{contiene a} \space \lambda \\ \end{array} \right.$
	- $\partial_a \left( u^* \right) = \partial_a \left( u \right) u^*$
4. Sea $a \in \Sigma$, $u \in \Sigma^*$: $\partial_{ax} \left( u \right) = \partial_x \left( \partial_a \left( u \right) \right)$

> [!tip]
> Sea el [[Autómata finito determinístico|AFD]] $M = \left< K, \Sigma, \delta, q_0, F \right>$ que acepta el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L = L \left( M \right)$, con el [[Alfabeto]] $\Sigma = \set{ a, b }$.
> 
> Desde $q_0$, $M$ aceptará el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L$, pero desde $q_0$ existe, al menos, una transición por $a$, o por $b$, o dos transiciones, una para $a$ y otra para $b$.
> 
> Luego de una transición por $a$, el [[Autómata finito determinístico|AFD]] $M$ pasa a un [[Lógica y Estructuras Discretas/Estado|Estado]] $q_i$, desde el cual aceptará el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $\partial_a \left( L \right)$. Análogamente, ante una transición por $b$, pasa a un [[Lógica y Estructuras Discretas/Estado|Estado]] $q_k$, donde aceptará el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $\partial_b \left( L \right)$.
