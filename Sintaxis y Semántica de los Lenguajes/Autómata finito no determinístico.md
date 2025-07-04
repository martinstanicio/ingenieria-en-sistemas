---
aliases:
  - AFND
  - Autómatas finitos no determinísticos
  - AEFND
  - Autómata de estados finitos no determinístico
  - Autómatas de estados finitos no determinísticos
created: 2025-03-06 14:40:22
modified: 2025-06-10 22:58:01
title: Autómata finito no determinístico
---

# Autómata finito no determinístico

Un [[Autómata finito no determinístico|AFND]] es un [[Autómata finito]], donde la [[Función de transición]] $\delta$ está definida de la siguiente forma.

$$
\delta: \left( K \times I \right) \to P \left( K \right)
$$

^d6497c

Donde $P \left( K \right)$ es el [[Conjunto potencia]] del [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $K$.

> [!tip]
> La única diferencia con los [[Autómata finito determinístico|AFD]] es que la [[Imagen]] de la [[Función de transición]] está formada por los elementos del [[Conjunto potencia]] de $K$.
> 
> Por lo tanto, dado $K = \set{A, B, C}$, tanto $\emptyset$, $\set{A, C}$, $\set{B}$, y $\set{A, B, C}$ son algunas de las posibles [[Imagen|Imágenes]] de la [[Función de transición]].

## Pasaje de AFND a AFND-λ

Sea un [[Autómata finito no determinístico|AFND]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, luego existe un [[Autómata finito no determinístico lambda|AFND-λ]] $M'$ tal que $L \left( M \right) = L \left( M' \right)$, donde $M' = \left< K, \Sigma, \delta', q_0, F \right>$ y

$$
\delta': K \times \Sigma \cup \set{ \lambda } \to P \left( K \right), \delta' \left( q, a \right) = \delta \left( q, a \right) \land \delta' \left( q, \lambda \right) = \set{ q }
$$

## Teorema de pasaje de GR a AFND

Sea $G = \left( N, T, P, S_0 \right)$ una [[Clasificación de Chomsky#Tipo 3 Regular|Gramática regular]], luego existe $M = \left( I, K, q_0, \delta, F \right)$ un [[Autómata finito no determinístico|AFND]] tal que $L(G) = Ac(M)$ donde:

$$
\begin{array}{c}
    I = T \\
    K = N \cup \set{f} \\
    q_0 = S_0 \\
    \delta (q_i, a) = q_j \space \text{si} \space q_i \to a q_j \in P \\
    \delta (q_i, a) = f \space \text{si} \space q_i \to a \in P \\
    F = \set{f} \\
\end{array}
$$

Donde $f \in F \subseteq K$ será el único [[Lógica y Estructuras Discretas/Estado|Estado]] aceptado, que siempre debemos agregar al formar un [[Autómata finito no determinístico|AFND]].
