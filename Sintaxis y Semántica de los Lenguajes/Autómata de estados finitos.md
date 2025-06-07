---
aliases:
  - Autómatas de estados finitos
  - AEF
  - Autómata de estados finitos determinístico
  - AEFD
created: 2025-03-04 15:16:59
modified: 2025-03-06 15:01:46
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

## Lenguaje aceptado

Sea $L(G)$ el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] asociado a un [[Autómata de estados finitos|AEF]] $M$. Luego se dice que $L(G)$ es el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] ==aceptado== por el [[Autómata de estados finitos|AEF]] y se denota $L(G) = Ac(M)$.

Un arreglo de [[Entradas|Entrada]] $\alpha = x_1, \dots, x_n$, perteneciente a la [[Cerradura de Kleene]] del [[Conjunto]] de [[Entradas]] ($\alpha \in I^*$), pertenece al [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado de la [[Autómata de estados finitos|AEF]] ($\alpha \in Ac(M)$) si se cumple lo siguiente.

1. El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial es el especificado ($q_0 = q_0$).
2. Dado un [[Lógica y Estructuras Discretas/Estado|Estado]] y la [[Entradas|Entrada]] siguiente, la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente me devuelve siempre el [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente ($f(q_{i - 1}, x_i) = q_i$).
3. El [[Lógica y Estructuras Discretas/Estado|Estado]] final es un [[Lógica y Estructuras Discretas/Estado|Estado]] aceptado ($q_n \in A$).

## Teorema de equivalencia AEF-GR

Los [[Autómata de estados finitos|Autómatas de estados finitos]] y [[Gramática#Tipo 3 Regular|Gramáticas regulares]] son ==equivalentes==, ya que ambos son representaciones de [[Lógica y Estructuras Discretas/Lenguaje|Lenguajes]] **regulares**.

## Teorema de pasaje de AEF a GR

Sea $M = \left( I, k, q_0, f, A \right)$ un [[Autómata de estados finitos|AEF]] y formamos las siguientes producciones. Si $f(q_i, a) = q_j$ entonces $q_i \to a q_j \in P$, y además si $q_j \in A$ entonces $q_i \to a \in P$. Luego la [[Gramática]] $G = \left( k, I, P, q_0 \right)$ tal que su [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] generado es el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado por la [[Autómata de estados finitos|AEF]].

$$
L(G) = Ac(M)
$$
