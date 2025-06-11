---
aliases:
  - Estados indistinguibles
created: 2025-06-10 19:51:41
modified: 2025-06-10 22:10:32
title: Indistinguibilidad
---

# Indistinguibilidad

Sea el [[Autómata finito determinístico|AFD]] $M = \left( K, \Sigma, \delta, q_0, F \right)$, los [[Lógica y Estructuras Discretas/Estado|Estados]] $q, r \in K$, y la [[Relación de equivalencia]] de [[Indistinguibilidad]] $\equiv$, se cumple que $q \equiv r$ ($q$ es indistinguible de $r$) si:

$$
\forall \alpha \in \Sigma^*:
\hat{\delta} \left( q, \alpha \right) \in F
\Leftrightarrow
\hat{\delta} \left( r, \alpha \right) \in F
$$

> [!note]
> $\hat{\delta}$ es la [[Función de transición extendida]].

La [[Indistinguibilidad]] tiene dos propiedades importantes:

1. $q \equiv r \Rightarrow \forall \alpha \in \Sigma^*: \delta \left( q, \alpha \right) \equiv \delta \left( r, \alpha \right)$
2. $\equiv$ es una [[Relación de equivalencia]]
