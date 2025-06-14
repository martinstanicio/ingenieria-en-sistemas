---
aliases:
  - Expresiones regulares
  - ER
  - REGEX
created: 2025-06-10 21:47:38
modified: 2025-06-14 16:14:53
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

El pasaje de una Expresión Regular (ER) a un Autómata Finito Determinístico (AFD) se basa en el **cálculo sistemático de las derivadas de la expresión regular**.

El proceso general implica lo siguiente:

- La expresión regular inicial `u` representa el lenguaje que será aceptado por el **estado inicial** del AFD.
- Al **calcular sistemáticamente las derivadas** de la expresión regular `u` para cada símbolo del alfabeto (``), y luego las derivadas de esas derivadas, se van descubriendo la **estructura del autómata**.
- Cada nueva expresión regular (o "lenguaje" derivado) que surge de este proceso se considera un **estado** en el AFD.
- Las **transiciones** entre estados se definen por estas derivadas: si `∂a(Lx) = Ly`, entonces hay una transición desde el estado `Lx` al estado `Ly` con el símbolo `a`.
- Un **estado es final** si el lenguaje que representa (su expresión regular derivada) **contiene la cadena vacía (``)**; es decir, si `T(Lx)` no es ``.

Este método permite determinar los estados, el estado inicial, las transiciones y los estados finales del AFD directamente a partir de la expresión regular, simulando cómo el autómata procesaría las entradas y qué "parte restante" del lenguaje aún necesitaría reconocer.

## Pasaje de ER a AFND-λ

Sea $r$ una [[Expresión regular|ER]], entonces existe un [[Autómata finito no determinístico lambda|AFND-λ]] que acepta $L \left( r \right)$.

==**FALTA PROCEDIMIENTO (gráficos de disyunción, concatenación y cerradura de kleene)**==
