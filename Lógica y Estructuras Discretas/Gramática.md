---
aliases:
  - Gramáticas
created: 2025-02-28 16:10:19
modified: 2025-06-14 19:56:33
title: Gramática
---

# Gramática

Es una cuaterna a partir de la cual podemos generar un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]].

$$
G = (T, N, P, S)
$$

## Símbolos terminales

$T$ es el [[Conjunto]] de símbolos terminales, que son los símbolos que terminan formando las [[Lógica y Estructuras Discretas/Cadena|Cadenas]] del [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]].

> [!note]
> Este [[Conjunto]] suele coincidir con el [[Alfabeto]] $\Sigma$.

## Símbolos no terminales

$N$ es el [[Conjunto]] de símbolos no terminales, que son el medio que me permite formar símbolos terminales, pero no aparecen en las [[Lógica y Estructuras Discretas/Cadena|Cadenas]] del [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]].

> [!important]
> Un símbolo no puede ser terminal y no terminal a la vez.
>
> $$
> T \cap N = \emptyset
> $$

## Producciones

$P$ es el [[Conjunto]] de producciones, de forma que:

$$
P \subseteq \left[ \left( T \cup N \right)^* - T^* \right] \times \left[ \left( T \cup N \right)^* \right]
$$

Son los pasos a seguir para ==pasar de los símbolos no terminales a los terminales==, partiendo desde el símbolo distinguido.

## Símbolo inicial o distinguido

$S$, $S_0$ o $\sigma$ es el símbolo inicial o distinguido de la [[Gramática]], y $S \in N$.

Es el punto de partida para generar cualquier [[Lógica y Estructuras Discretas/Cadena|Cadena]] del [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]].
