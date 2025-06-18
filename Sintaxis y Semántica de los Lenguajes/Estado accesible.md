---
aliases:
  - Estados accesibles
  - Estado alcanzable
  - Estados alcanzables
created: 2025-06-18 00:58:05
modified: 2025-06-18 01:04:54
title: Estado accesible
---

# Estado accesible

Dado un [[Autómata finito]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, el [[Lógica y Estructuras Discretas/Estado|Estado]] $q \in K$ es [[Estado accesible|Accesible]] si es posible llegar al mismo partiendo desde el [[Lógica y Estructuras Discretas/Estado|Estado]] inicial.

$$
\exists \alpha \in \Sigma^*: \left( q_0, \alpha \right) \vdash^* \left( q, \lambda \right)
$$

> [!warning]
> La [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha$ no necesariamente tiene que pertenecer a $L \left( M \right)$
