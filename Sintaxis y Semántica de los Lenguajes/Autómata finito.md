---
aliases:
  - AF
  - Autómatas finitos
  - AFD
  - Autómata finito determinístico
  - Autómatas finitos determinísticos
  - AEF
  - Autómata de estados finitos
  - Autómatas de estados finitos
  - AEFD
  - Autómata de estados finitos determinístico
  - Autómatas de estados finitos determinísticos
created: 2025-03-04 15:16:59
modified: 2025-06-10 17:44:59
title: Autómata finito
---

# Autómata finito

Es un [[Autómata]] con una cantidad finita de [[Lógica y Estructuras Discretas/Estado|Estados]]. Es una quíntupla $M$.

$$
M = \left( I, K, q_0, \delta, F \right)
$$

- $I$: [[Conjunto]] finito de [[Entradas]] ($I \neq \emptyset$), que suele ser el [[Alfabeto]] $\Sigma$.
- $K$: [[Conjunto]] finito de [[Lógica y Estructuras Discretas/Estado|Estados]] ($K \neq \emptyset$).
- $q_0$: El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial del [[Autómata]] ($q_0 \in K$).
- $\delta$: [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente, $\delta: \left( K \times I \right) \to K$. Para cada posible combinación de [[Lógica y Estructuras Discretas/Estado|Estados]] y [[Entradas]], asigna un [[Lógica y Estructuras Discretas/Estado|Estado]].
- $F$: [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] aceptados o finales ($F \subseteq K$).

## Lenguaje aceptado

Sea $L(G)$ el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] asociado a un [[Autómata finito|AF]] $M$. Luego se dice que $L(G)$ es el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] ==aceptado== por el [[Autómata finito|AF]] y se denota $L(G) = Ac(M)$.

Un arreglo de [[Entradas|Entrada]] $\alpha = x_1, \dots, x_n$, perteneciente a la [[Cerradura de Kleene]] del [[Conjunto]] de [[Entradas]] ($\alpha \in I^*$), pertenece al [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado del [[Autómata finito|AF]] ($\alpha \in Ac(M)$) si se cumple lo siguiente.

1. El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial es el especificado ($q_0 = q_0$).
2. Dado un [[Lógica y Estructuras Discretas/Estado|Estado]] y la [[Entradas|Entrada]] siguiente, la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente me devuelve siempre el [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente ($\delta (q_{i - 1}, x_i) = q_i$).
3. El [[Lógica y Estructuras Discretas/Estado|Estado]] final es un [[Lógica y Estructuras Discretas/Estado|Estado]] aceptado ($q_n \in F$).

## Pasaje de AFD a AFND

## Pasaje de AFD a GR

Sea $M = \left( I, K, q_0, \delta, F \right)$ un [[Autómata finito|AFD]] y formamos las siguientes producciones. Si $\delta (q_i, a) = q_j$ entonces $q_i \to a q_j \in P$, y además si $q_j \in F$ entonces $q_i \to a \in P$. Luego, formamos la [[Gramática]] $G = \left( K, I, P, q_0 \right)$, tal que su [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] generado es el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado por el [[Autómata finito|AFD]].

$$
L(G) = Ac(M)
$$
