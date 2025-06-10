---
aliases:
  - AFND-λ
  - Autómatas finitos no determinísticos lambda
  - AEFND-λ
  - Autómata de estados finitos no determinístico lambda
  - Autómatas de estados finitos no determinísticos lambda
created: 2025-03-06 14:40:22
modified: 2025-06-10 18:40:36
title: Autómata finito no determinístico lambda
---

# Autómata finito no determinístico lambda

Un [[Autómata finito no determinístico lambda|AFND-λ]] es un [[Autómata finito]], donde la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estados]] siguientes $\delta$ está definida de la siguiente forma.

$$
\delta: K \times \Sigma \cup \set{ \lambda } \to P \left( K \right)
$$

> [!tip]
> Es decir, existen transiciones que nos permiten pasar de un [[Lógica y Estructuras Discretas/Estado|Estado]] a otro, sin consumir nada de la [[Lógica y Estructuras Discretas/Cadena|Cadena]] (ya que como $\lambda$ es la [[Cadena vacía]], consumir $\lambda$ es lo mismo que no consumir nada).

## Pasaje de AFND-λ a AFD

Sea un [[Autómata finito no determinístico|AFND]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, luego existe un [[Autómata finito no determinístico lambda|AFND-λ]] $M'$ tal que $L \left( M \right) = L \left( M' \right)$, donde $M' = \left< K, \Sigma, \delta', q_0, F \right>$ y

$$
\delta': K \times \Sigma \cup \set{ \lambda } \to P \left( K \right), \delta' \left( q, a \right) = \delta \left( q, a \right) \land \delta' \left( q, \lambda \right) = \set{ q }
$$
