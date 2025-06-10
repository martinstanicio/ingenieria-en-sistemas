---
aliases:
  - Clausura-λ
created: 2025-06-10 18:40:36
modified: 2025-06-10 18:49:17
title: Clausura lambda
---

# Clausura lambda

Sea un [[Autómata finito no determinístico lambda|AFND-λ]] $M$, con un [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $K$ y $q \in K$, se define la [[Clausura lambda]] $\text{Cl-}\lambda: K \to P \left( K \right)$ de la siguiente forma.

$$
\text{Cl-}\lambda \left( q \right) = \set{ q' \in K: \left( q, \lambda \right) \vdash^* \left( q', \lambda \right) }
$$

> [!tip]
> Esto es, en la [[Clausura lambda|Clausura-λ]] de un [[Lógica y Estructuras Discretas/Estado|Estado]] $q$ están todos los [[Lógica y Estructuras Discretas/Estado|Estados]] a los cuales es posible llegar desde $q$ usando transiciones $\lambda$.

---

Dado un [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $Q \subseteq K$, también se puede calcular la [[Clausura lambda]] $\text{Cl-}\lambda: P \left( K \right) \to P \left( K \right)$ del mismo, de la siguiente forma.

$$
\text{Cl-}\lambda \left( Q \right) =
\set{ q' \in K: \exists q \in Q \land \left( q, \lambda \right) \vdash^* \left( q', \lambda \right) } =
\bigcup_{q_i \in Q} \text{Cl-}\lambda \left( q_i \right)
$$
