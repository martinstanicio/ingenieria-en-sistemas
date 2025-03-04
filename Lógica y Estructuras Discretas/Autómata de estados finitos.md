---
aliases:
  - Autómatas de estados finitos
  - AEF
created: 2025-03-04 15:16:59
modified: 2025-03-04 15:36:48
title: Autómata de estados finitos
---

# Autómata de estados finitos

Es un [[Autómata]] con una cantidad finita de [[Lógica y Estructuras Discretas/Estado|Estados]]. Es una quíntupla $M$.

$$
M = \left( I, k, q_0, f, A \right)
$$

- $I$: [[Conjunto]] finito de [[Entradas]] ($I \neq \emptyset$).
- $k$: [[Conjunto]] finito de [[Lógica y Estructuras Discretas/Estado|Estados]] ($k \neq \emptyset$).
- $q_0$: El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial del [[Autómata]] ($q_0 \in k$).
- $f$: [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente, $f: \left( k \times I \right) \to k$. Para cada posible combinación de [[Lógica y Estructuras Discretas/Estado|Estados]] y [[Entradas]], asigna un [[Lógica y Estructuras Discretas/Estado|Estado]].
- $A$: [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] aceptados o finales ($A \subseteq k$).

Sea $L(G)$ el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] asociado a un [[Autómata de estados finitos|AEF]] $M$. Luego se dice que $L(G)$ es el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] ==aceptado== por el [[Autómata de estados finitos|AEF]] y se denota $L(G) = Ac(M)$.
