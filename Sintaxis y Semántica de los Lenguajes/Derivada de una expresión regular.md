---
aliases:
  - Derivada de una ER
created: 2025-06-11 13:47:31
modified: 2025-06-14 16:23:08
title: Derivada de una expresión regular
---

# Derivada de una expresión regular

Podemos definir la [[Derivada]] de una [[Expresión regular]] de la siguiente forma.

1. $D_\lambda \left( u \right) = u$, para $u$ una [[Expresión regular|ER]]
2. Para cada $a \in \Sigma$:
	- $D_a \left( \emptyset \right) = \emptyset$
	- $D_a \left( \lambda \right) = \emptyset$
	- $D_a \left( b \right) = \lambda$ si $a = b$
	- $D_a \left( b \right) = \emptyset$ si $a \neq b$
3. Si $u$ y $v$ son dos [[Expresión regular|ER]]:
	- $D_a \left( u + v \right) = D_a \left( u \right) + D_a \left( v \right)$
	- $D_a \left( uv \right) = D_a \left( u \right)v + T \left( u \right) D_a \left( v \right)$, donde $T \left( u \right) = \left\{ \begin{array}{c} \emptyset \space \text{si} \space L \left( u \right) \space \text{no contiene a} \space \lambda \\ \set{ \lambda } \space \text{si} \space L \left( u \right) \space \text{contiene a} \space \lambda \\ \end{array} \right.$
	- $D_a \left( u^* \right) = D_a \left( u \right) u^*$
4. Sea $a \in \Sigma$, $u \in \Sigma^*$: $D_{ax} \left( u \right) = D_x \left( D_a \left( u \right) \right)$

> [!note]
> También se puede utilizar el símbolo de [[Derivada parcial]] $\partial_x \left( u \right)$.

> [!tip]
> La [[Derivada de una expresión regular|Derivada de una ER]] $u$ respecto a un símbolo $a$, denotada $D_a \left( u \right)$, es el [[Conjunto]] de [[Lógica y Estructuras Discretas/Cadena|Cadenas]] $\beta$ tales que $a \beta$ pertenece al [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L$ definido por la [[Expresión regular|ER]].
> 
> Si hacemos el pasaje a un [[Autómata finito determinístico|AFD]], serían las [[Lógica y Estructuras Discretas/Cadena|Cadenas]] aceptadas del mismo, luego de pasar del [[Lógica y Estructuras Discretas/Estado|Estado]] inicial $q_0$ a un [[Lógica y Estructuras Discretas/Estado|Estado]] $q_i$, mediante el símbolo $a$.
