---
aliases:
  - Expresiones regulares
  - ER
  - REGEX
created: 2025-06-10 21:47:38
modified: 2025-06-10 21:55:28
title: Expresión regular
---

# Expresión regular

Es un formalismo para expresar un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] ==regular== (tipo 3).

Sea un [[Alfabeto]] $\Sigma$, las [[Expresión regular|ER]] sobre $\Sigma$ y los [[Conjunto|Conjuntos]] que ellas denotan ([[Conjunto regular|Conjuntos regulares]]) son definidos recursivamente de la siguiente forma.

1. $\emptyset$ es una [[Expresión regular|ER]] y denota el [[Conjunto vacío]] $\Sigma$
2. $\lambda$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $\set{ \lambda }$
3. Por cada $a \in \Sigma$, $a$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $\set{ a }$
4. Si $r$ y $s$ son [[Expresión regular|ER]] que denotan los [[Lógica y Estructuras Discretas/Lenguaje|Lenguajes]] $R$ y $S$, entonces:
	- $r + s \Leftrightarrow r / s$ es una [[Expresión regular|ER]] y denota $R \cup S$
	- $rs$ es una [[Expresión regular|ER]] y denota $R \circ S$
	- $r^*$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $R^*$ ([[Cerradura de Kleene]] de $R$)

> [!tip]
> Por la definición de la [[Cerradura de Kleene]] y la [[Cerradura positiva]], las siguientes expresiones son equivalentes.
>
> $$
> rr^* = r^+
> $$
