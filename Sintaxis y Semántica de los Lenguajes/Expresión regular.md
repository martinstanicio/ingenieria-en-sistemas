---
aliases:
  - Expresiones regulares
  - ER
  - REGEX
created: 2025-06-10 21:47:38
modified: 2025-06-14 17:31:53
title: Expresión regular
---

# Expresión regular

Es un formalismo para expresar un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] ==regular== (tipo 3).

Sea un [[Alfabeto]] $\Sigma$, las [[Expresión regular|ER]] sobre $\Sigma$ y los [[Conjunto|Conjuntos]] que ellas denotan ([[Conjunto regular|Conjuntos regulares]]) son definidos recursivamente de la siguiente forma.

1. $\emptyset$ es una [[Expresión regular|ER]] y denota el [[Conjunto vacío]] $\emptyset$
2. $\lambda$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $\set{ \lambda }$
3. Por cada $a \in \Sigma$, $a$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $\set{ a }$
4. Si $r$ y $s$ son [[Expresión regular|ER]] que denotan los [[Lógica y Estructuras Discretas/Lenguaje|Lenguajes]] $R$ y $S$, entonces:
	- $r + s \Leftrightarrow r / s$ es una [[Expresión regular|ER]] y denota $R \cup S$
	- $rs$ es una [[Expresión regular|ER]] y denota $R \circ S$ (concatenación)
	- $r^*$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $R^*$ ([[Cerradura de Kleene]] de $R$)

> [!tip]
> Por la definición de la [[Cerradura de Kleene]] y la [[Cerradura positiva]], las siguientes expresiones son equivalentes.
>
> $$
> rr^* = r^+
> $$

## Pasaje de ER a AFD

La [[Expresión regular|ER]] inicial $u$ representa el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] que será aceptado por el [[Lógica y Estructuras Discretas/Estado|Estado]] inicial $q_0$ del [[Autómata finito determinístico|AFD]]. Al calcular sistemáticamente las [[Derivada de una expresión regular|Derivadas]] de la [[Expresión regular|ER]] $u$ para cada símbolo del alfabeto $\Sigma$, y luego las [[Derivada de una expresión regular|Derivadas]] de esas [[Derivada de una expresión regular|Derivadas]], se van descubriendo la estructura del [[Autómata finito determinístico|AFD]]. Cada [[Expresión regular|ER]] diferente que surge de este proceso se considera un [[Lógica y Estructuras Discretas/Estado|Estado]] en el [[Autómata finito determinístico|AFD]]. Las transiciones entre [[Lógica y Estructuras Discretas/Estado|Estados]] se definen por estas derivadas: si $D_a \left( L_x \right) = L_y$, entonces hay una transición desde el [[Lógica y Estructuras Discretas/Estado|Estado]] $L_x$ al estado $L_y$ con el símbolo $a$. Un [[Lógica y Estructuras Discretas/Estado|Estado]] es final si el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] que representa (su [[Expresión regular|ER]] derivada) contiene la [[Cadena vacía]] $\lambda$; es decir, si $T \left( L_x \right)$ no es $\emptyset$.

## Pasaje de ER a AFND-λ

Sea $r$ una [[Expresión regular|ER]], entonces existe un [[Autómata finito no determinístico lambda|AFND-λ]] que acepta $L \left( r \right)$.

==**FALTA PROCEDIMIENTO (gráficos de disyunción, concatenación y cerradura de kleene)**==
