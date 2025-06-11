---
aliases:
  - AFD
  - Autómatas finitos determinísticos
  - AEFD
  - Autómata de estados finitos determinístico
  - Autómatas de estados finitos determinísticos
created: 2025-06-10 17:49:07
modified: 2025-06-10 23:07:03
title: Autómata finito determinístico
---

# Autómata finito determinístico

Un [[Autómata finito determinístico|AFD]] es un [[Autómata finito]], donde la [[Función de transición]] $\delta$ está definida de la siguiente forma.

$$
\delta: \left( K \times I \right) \to K
$$

^718883

## Pasaje de AFD a AFND

Sea un [[Autómata finito determinístico|AFD]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, luego existe un [[Autómata finito no determinístico|AFND]] $M'$ tal que $L \left( M \right) = L \left( M' \right)$, donde $M' = \left< K, \Sigma, \delta', q_0, F \right>$ y

$$
\delta': K \times \Sigma \to P \left( K \right), \delta' \left( q, a \right) = \set{ \delta \left( q, a \right) }
$$

## Pasaje de AFD a GR

Sea $M = \left( I, K, q_0, \delta, F \right)$ un [[Autómata finito determinístico|AFD]] y formamos las siguientes producciones. Si $\delta (q_i, a) = q_j$ entonces $q_i \to a q_j \in P$, y además si $q_j \in F$ entonces $q_i \to a \in P$. Luego, formamos la [[Gramática]] $G = \left( K, I, P, q_0 \right)$, tal que su [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] generado es el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado por el [[Autómata finito determinístico|AFD]].

$$
L(G) = L(M)
$$

## Pasaje de AFD a ER

Si un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L$ es aceptado por un [[Autómata finito determinístico|AFD]] $M$, entonces $L$ puede ser expresado mediante una [[Expresión regular]].

==**FALTA ALGORITMO DE PASAJE**==
