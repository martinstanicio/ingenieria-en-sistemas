---
aliases:
  - GR
created: 2025-06-14 19:56:35
modified: 2025-06-14 20:02:07
title: Gramática regular
---

# Gramática regular

Una [[Gramática]] considerada ==regular o tipo 3== según la [[Clasificación de Chomsky]].

## Pasaje de GR a AFND-λ

Sea una [[Gramática]] regular $G = \left< N, T, P, S \right>$, el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] generado por la misma puede ser representado por un [[Autómata finito determinístico|AFD]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, tal que $L(G) = L(M)$.

1. Hacer $K = N \cup \set{ f }$
2. Para cada derivación $\left( A \to aB \right) \in P$:
	1. Agregar $B$ a $\delta \left( A, a \right)$
3. Para cada derivación $\left( A \to a \right) \in P$:
	1. Agregar $f$ a $\delta \left( A, a \right)$
4. Si existe derivación $\left( S \to \lambda \right) \in P$:
	1. Agregar $f$ a $\delta \left( S, \lambda \right)$
5. Hacer $F = \set{ f }$
