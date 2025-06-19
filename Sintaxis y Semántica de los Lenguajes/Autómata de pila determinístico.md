---
aliases:
  - Autómatas de pila determinísticos
  - APD
created: 2025-06-15 01:09:26
modified: 2025-06-19 16:47:08
title: Autómata de pila determinístico
---

# Autómata de pila determinístico

Sea un [[Autómata de pila|AP]] $M = \left< K, \Sigma, \Gamma, \delta, q_0, z_0, F \right>$, $M$ es determinístico si se cumple lo siguiente:

1. $\# \left[ \delta \left( q, a, A \right) \right] \leq 1$
2. $\# \left[ \delta \left( q, \lambda, A \right) \right] \leq 1$
3. $\# \left[ \delta \left( q, \lambda, A \right) \right] = 1 \Rightarrow \# \left[ \delta \left( q, a, A \right) \right] = 0$

> [!tip]
> Para cada combinación de [[Lógica y Estructuras Discretas/Estado|Estado]], símbolo del [[Alfabeto]] de [[Entradas|Entrada]] o la [[Cadena vacía]], y símbolo del [[Alfabeto]] de la [[Pila]], debe haber como máximo una transición.
