---
aliases:
  - Funciones de transición extendidas
  - Función de estado siguiente extendida
  - Función de estados siguientes extendida
  - Funciones de estado siguiente extendidas
  - Funciones de estados siguientes extendidas
created: 2025-06-10 22:04:18
modified: 2025-06-10 22:18:20
title: Función de transición extendida
---

# Función de transición extendida

Sea un [[Autómata finito]] $M = \left( K, I, \delta, q_0, F \right)$, la [[Función de transición extendida]] $\hat{\delta}$ define el [[Lógica y Estructuras Discretas/Estado|Estado]] o [[Lógica y Estructuras Discretas/Estado|Estados]] resultantes al consumir una cadena $\alpha \in I^*$, desde un cierto [[Lógica y Estructuras Discretas/Estado|Estado]] $q \in K$.

$$
\hat{\delta} \left( q, \alpha \right) =
\left\{
    \begin{array}{c}
        \delta \left( q, a \right) \space \text{si} \space \alpha = a \\
        \hat{\delta} \left( \delta \left( q, a \right), \alpha' \right) \space \text{si} \space \alpha = a \alpha' \\
    \end{array}
\right.
$$

Donde $\alpha, \alpha' \in I^*$ y $a \in I$.

> [!important]
> La diferencia fundamental es que mientras la [[Función de transición]] $\delta$ solo acepta un elemento $a \in I$ a la vez, la [[Función de transición extendida]] $\hat{\delta}$ acepta una [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha \in I^*$.
