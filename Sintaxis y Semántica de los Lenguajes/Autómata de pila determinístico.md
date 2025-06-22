---
aliases:
  - Autómatas de pila determinísticos
  - APD
created: 2025-06-15 01:09:26
modified: 2025-06-22 12:05:23
title: Autómata de pila determinístico
---

# Autómata de pila determinístico

Sea un [[Autómata de pila|AP]] $M = \left< K, \Sigma, \Gamma, \delta, q_0, z_0, F \right>$, $M$ es determinístico si se cumple lo siguiente:

1. $\# \left[ \delta \left( q, a, A \right) \right] \leq 1$
2. $\# \left[ \delta \left( q, \lambda, A \right) \right] \leq 1$
3. $\# \left[ \delta \left( q, \lambda, A \right) \right] = 1 \Rightarrow \# \left[ \delta \left( q, a, A \right) \right] = 0$

> [!tip]
> Para cada combinación de [[Lógica y Estructuras Discretas/Estado|Estado]], símbolo del [[Alfabeto]] de [[Entradas|Entrada]] o la [[Cadena vacía]], y símbolo del [[Alfabeto]] de la [[Pila]], debe haber como máximo una transición.

# Pasaje de APD a GLC

Sea $M = \left< K, \Sigma, \Gamma, \delta, q_0, z_0, F \right>$ un [[Autómata de pila determinístico|APD]], definimos $G = \left< N, T, P, S \right>$ una [[Gramática libre de contexto|GLC]] tal que $L \left( M \right) = L \left( G \right)$.

1. $N = \set{ \left[ t \right]: t \in \left( K \times \Gamma \times K \right) } \cup \set{S}$
2. $T = \Sigma$
3. $P = \emptyset$
4. Para cada $q \in K$:
	1. Agregar a $P$:
		1. $S \to \left[ q_0 \space z_0 \space q \right]$
5. Para cada $q, q_1, q_2, \dots, q_{m + 1} \in K$:
	1. Para cada $a \in \Sigma \cup \set{ \lambda }$:
		1. Para cada $A, B_1, B_2, \dots, B_m \in \Gamma$:
			1. Agregar a $P$:
				1. $\left[ q \space A \space p \right] \to a \left[ q_1 \space B_1 \space q_2 \right] \left[ q_2 \space B_2 \space q_3 \right] \dots \left[ q_m \space B_m \space q_{m + 1} \right]$
   Donde $p = q_{m + 1}$ y $\left( q_1, B_1 B_2 \dots B_m \right) \in \delta \left(q, a, A \right)$
6. Si $\left( p, \lambda \right) \in \delta \left( q, a, A \right)$:
	1. $\left[ q \space A \space p \right] \to a$
