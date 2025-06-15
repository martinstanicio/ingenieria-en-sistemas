---
aliases:
  - AF
  - Autómatas finitos
  - AEF
  - Autómata de estados finitos
  - Autómatas de estados finitos
created: 2025-03-04 15:16:59
modified: 2025-06-14 23:13:08
title: Autómata finito
---

# Autómata finito

Es un [[Autómata]] con una cantidad finita de [[Lógica y Estructuras Discretas/Estado|Estados]]. Es una quíntupla $M$.

$$
M = \left< K, I, \delta, q_0, F \right>
$$

- $K$: [[Conjunto]] finito de [[Lógica y Estructuras Discretas/Estado|Estados]] ($K \neq \emptyset$).
- $I$: [[Alfabeto]] de [[Entradas|Entrada]] ($I \neq \emptyset$), que suele ser $\Sigma$.
- $\delta$: [[Función de transición]].
- $q_0$: El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial del [[Autómata]] ($q_0 \in K$).
- $F$: [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] aceptados o finales ($F \subseteq K$).

## Lenguaje aceptado

Sea $L(G)$ el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] asociado a un [[Autómata finito|AF]] $M$. Luego se dice que $L(G)$ es el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] ==aceptado== por el [[Autómata finito|AF]] y se denota $L(G) = Ac(M)$.

Un arreglo de [[Entradas|Entrada]] $\alpha = x_1, \dots, x_n$, perteneciente a la [[Cerradura de Kleene]] del [[Conjunto]] de [[Entradas]] ($\alpha \in I^*$), pertenece al [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado del [[Autómata finito|AF]] ($\alpha \in Ac(M)$) si se cumple lo siguiente.

1. El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial es el especificado ($q_0 = q_0$).
2. Dado un [[Lógica y Estructuras Discretas/Estado|Estado]] y la [[Entradas|Entrada]] siguiente, la [[Función de transición]] me devuelve siempre el [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente ($\delta (q_{i - 1}, x_i) = q_i$).
3. El [[Lógica y Estructuras Discretas/Estado|Estado]] final es un [[Lógica y Estructuras Discretas/Estado|Estado]] aceptado ($q_n \in F$).
