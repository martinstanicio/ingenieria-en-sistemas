---
aliases:
  - Derivada de una ER
created: 2025-06-11 13:47:31
modified: 2025-06-11 13:55:25
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
	- $\partial_a \left( uv \right) = \partial_a \left( u \right)v + T \left( u \right) \partial_a \left( v \right)$, donde $T \left( u \right) = \left\{ \begin{array}{l} \emptyset \space \text{si} \space L \left( u \right) \space \text{no contiene a} \space \lambda \\ \set{ \lambda } \space \text{si} \space L \left( u \right) \space \text{contiene a} \space \lambda \\ \end{array} \right.$
	- $\partial_a \left( u^* \right) = \partial_a \left( u \right) u^*$
