---
aliases:
  - Función mover
created: 2025-06-10 19:38:16
modified: 2025-06-22 12:12:50
title: Algoritmo mover
---

# Algoritmo mover

Dado un [[Autómata finito no determinístico lambda|AFND-λ]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, este algoritmo define a la [[Análisis Matemático I/Función|Función]] $\text{mover}: P \left( K \right) \times \Sigma \to P \left( K \right)$ para pasar de un [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $T \subseteq K$ a otro [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $L$, mediante un símbolo del [[Alfabeto]] $a \in \Sigma$. Hace uso de la [[Clausura lambda]].

$$
\text{mover} \left( T, a \right) = \text{Cl-}\lambda \left( \set{ x \in \delta \left( t, a \right), t \in T } \right)
$$

> [!tip]
> Devuelve el [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] a los cuales es posible llegar, partiendo desde cualquier [[Lógica y Estructuras Discretas/Estado|Estado]] $t \in T$, y consumiendo $a$; incluyendo la [[Clausura lambda|Clausura-λ]] de cada uno de los [[Lógica y Estructuras Discretas/Estado|Estados]] resultantes.
