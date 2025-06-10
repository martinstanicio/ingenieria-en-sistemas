---
created: 2025-06-10 20:05:52
modified: 2025-06-10 20:18:21
title: Indistinguibilidad de orden k
---

# Indistinguibilidad de orden k

Sea un [[Autómata finito determinístico|AFD]] $M = \left( K, \Sigma, \delta, q_0, F \right)$ y sean los [[Lógica y Estructuras Discretas/Estado|Estados]] $p, q \in K$, $p \equiv_k q$ son [[Indistinguibilidad|Estados indistinguibles]] para [[Lógica y Estructuras Discretas/Cadena|Cadenas]] de longitud menor o igual que $k$ si y solo si:

$$
\forall \alpha, \vert \alpha \vert \leq k:
\delta \left( p, \alpha \right) \in F
\Leftrightarrow
\delta \left( q, \alpha \right) \in F
$$

> [!important]
> Existe $\alpha$ que ==distingue== a $q$ de $r$ si $\delta \left( q, \alpha \right) \in F \Leftrightarrow \delta \left( r, \alpha \right) \notin F$, es decir, cuando se consume $\alpha$ desde $q$, se llega a un [[Lógica y Estructuras Discretas/Estado|Estado]] final, pero si se hace desde $r$, se llega a un [[Lógica y Estructuras Discretas/Estado|Estado]] no final.

La [[Indistinguibilidad de orden k]] tiene una serie de propiedades importantes:

1. $\equiv_k$ es una [[Relación de equivalencia]]
2. $\equiv_{k + 1} \subseteq \equiv_k$ (si dos [[Lógica y Estructuras Discretas/Estado|Estados]] son $\left( k + 1 \right)$-equivalentes, entonces son $k$-equivalentes)
3. $p \equiv_{k + 1} r \Leftrightarrow p \equiv_k r \land \forall a \in \Sigma: \delta \left( p, a \right) \equiv_k \delta \left( r, a \right)$
4. $\left( \equiv_k = \equiv_{k + 1} \right) \Rightarrow \forall j\geq 0: \left( \equiv_k = \equiv_{k + j} \right)$
