---
aliases:
  - Función mover
created: 2025-06-10 19:38:16
modified: 2025-06-10 19:42:58
title: Algoritmo mover
---

# Algoritmo mover

Dado un [[Autómata finito no determinístico lambda|AFND-λ]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, este algoritmo define a la [[Análisis Matemático I/Función|Función]] $\text{mover}: P \left( K \right) \times \Sigma \to P \left( K \right)$ para pasar de un [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $T \subseteq K$ a otro [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $L$, mediante un símbolo del [[Alfabeto]] $a \in \Sigma$. Hace uso de la [[Clausura lambda]].

$$
\text{mover} \left( T, a \right) = \text{Cl-}\lambda \left( \set{ x \in \delta \left( t, a \right), t \in T } \right)
$$
