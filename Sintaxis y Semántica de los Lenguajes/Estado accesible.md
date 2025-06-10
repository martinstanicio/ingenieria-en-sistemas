---
aliases:
  - Estados accesibles
created: 2025-06-10 19:44:00
modified: 2025-06-10 19:47:15
title: Estado accesible
---

# Estado accesible

Sea un [[Autómata finito|AF]] $M = \left( K, \Sigma, \delta, q_0, F \right)$ y $q \in K$, $q$ es un [[Estado accesible]] si existe una [[Lógica y Estructuras Discretas/Cadena|Cadena]] que me permita llegar al mismo, partiendo desde el [[Lógica y Estructuras Discretas/Estado|Estado]] inicial, es decir:

$$
\exists \alpha \in \Sigma^*:
\left( q_0, \alpha \right) \vdash^* \left( q, \lambda \right)
\Leftrightarrow
\delta \left( q_0, \alpha \right) = q
$$

> [!warning]
> $\alpha$ no necesariamente tiene que pertenecer a $L \left( M \right)$.
