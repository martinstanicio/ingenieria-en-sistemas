---
aliases:
  - Gramáticas
created: 2025-02-28 16:10:19
modified: 2025-06-07 19:33:30
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

## Clasificación de Chomsky

Siempre buscamos utilizar la ==clasificación que mejor se ajuste== a la [[Gramática]], pues algunas están contenidas dentro de otras.

$$
T3 \subset T2 \subset T1 \subset T0
$$

### Tipo 3: Regular

Una [[Gramática]] $G$ se llama ==regular== o tipo 3 si sus [[Gramática#Producciones|Producciones]] son de la siguiente forma.

$$
\left( A \to aB, A \to a \right)
\lor
\left( A \to Ba, A \to a \right)
/
A, B \in N \land a \in T
$$

### Tipo 2: Libre de contexto

Una [[Gramática]] $G$ se llama libre de contexto, independiente de contexto, o tipo 2 si sus [[Gramática#Producciones|Producciones]] son de la siguiente forma.

$$
\left( A \to \alpha \right)
/
A \in N \land \alpha \in \left( T \cup N \right)^* - \set{\lambda}
$$

Es decir, si todas las [[Gramática#Producciones|Producciones]] se derivan en cualquier combinación de terminales y no terminales, excepto la [[Cadena vacía]] $\lambda$.

### Tipo 1: Sensible al contexto

Una [[Gramática]] $G$ se llama sensible al contexto o tipo 1 si sus [[Gramática#Producciones|Producciones]] son de la siguiente forma.

$$
\left( \alpha A \beta \to \alpha \gamma \beta \right)
/
A \in N \land \alpha, \beta, \gamma \in \left( T \cup N \right)^* - \set{\lambda}
$$

La parte derecha de una producción debe ser, en longitud, mayor o igual que la longitud de la parte izquierda.

### Tipo 0: Recursivamente enumerada

Una [[Gramática]] $G$ se llama tipo 0 en caso contrario.

> [!tip]
> Todas las [[Gramática|Gramáticas]] son de [[Gramática#Tipo 0|Tipo 0]], pero siempre debemos utilizar la clasificación más reducida aplicable.
