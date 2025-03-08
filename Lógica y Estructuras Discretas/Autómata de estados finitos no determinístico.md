---
aliases:
  - Autómatas de estados finitos no determinísticos
  - AEFND
created: 2025-03-06 14:40:22
modified: 2025-03-08 16:01:34
title: Autómata de estados finitos no determinístico
---

# Autómata de estados finitos no determinístico

Se llama [[Autómata de estados finitos no determinístico]] a la quíntupla $M$.

$$
M = \left( I, k, q_0, f, A \right)
$$

- $I$: [[Conjunto]] finito de [[Entradas]] ($I \neq \emptyset$).
- $k$: [[Conjunto]] finito de [[Lógica y Estructuras Discretas/Estado|Estados]] ($k \neq \emptyset$).
- $q_0$: El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial del [[Autómata]] ($q_0 \in k$).
- $f$: [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente, $f: \left( k \times I \right) \to P \left( k \right)$, donde $P(k)$ es el [[Conjunto potencia]] del [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $k$.
- $A$: [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] aceptados o finales ($A \subseteq k$).

> [!tip]
> La única diferencia con los [[Autómata de estados finitos|AEFD]] es que la [[Imagen]] de la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estados]] está formada por los elementos del [[Conjunto potencia]] de $k$.
> 
> Por lo tanto, dado $k = \set{A, B, F}$, tanto $\emptyset$, $\set{A, F}$, $\set{B}$, y $\set{A, B, F}$ son algunas de las posibles [[Imagen|Imágenes]] de la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estados]].

## Teorema de pasaje de GR a AEFND

Sea $G = \left( N, T, P, S_0 \right)$ una [[Gramática#Tipo 3 Regular|Gramática regular]], luego existe $M = \left( I, k, q_0, f, A \right)$ un [[Autómata de estados finitos no determinístico|AEFND]] tal que $L(G) = Ac(M)$ donde:

$$
\begin{array}{c}
    I = T \\
    k = N \cup \set{F} \\
    q_0 = S_0 \\
    f(q_i, a) = q_j \space \text{si} \space q_i \to a q_j \in P \\
    f(q_i, a) = F \space \text{si} \space q_i \to a \in P \\
    A = \set{F} \\
\end{array}
$$

Donde $F$ será el único [[Lógica y Estructuras Discretas/Estado|Estado]] aceptado, que siempre debemos agregar al formar un [[Autómata de estados finitos no determinístico|AEFND]].

## Teorema de pasaje de AEFND a AEF

Sea $M = \left( I, k, q_0, f, A \right)$ un [[Autómata de estados finitos no determinístico|AEFND]]. Luego existe $M' = \left( I', k', {q_0}' f', A' \right)$ un [[Autómata de estados finitos|AEF]] tal que $Ac(M) = Ac(M')$ donde:

$$
\begin{array}{c}
    I' = I \\
    k' = P(k) \\
    {q_0}' = \set{q_0} \\
    f'(X, a) = \left\{
        \begin{array}{c}
            \bigcup_{Y \in X} f(Y, a) \\
            \emptyset \space \text{si} \space X = \emptyset
        \end{array}
    \right. \\
    A' = \set{ X \in P(k): x \cap \set{F} \neq \emptyset, F \in A } \\
\end{array}
$$

Como $k' = P(k)$, es decir, $k'$ es el [[Conjunto potencia]] de $k$, muchas veces obtendremos un [[Autómata de estados finitos|AEF]] con múltiples [[Lógica y Estructuras Discretas/Estado|Estados]] ==fuente==, es decir, [[Lógica y Estructuras Discretas/Estado|Estados]] a los que no es posible llegar si tomamos un [[Lógica y Estructuras Discretas/Estado|Estado]] inicial diferente. Por lo tanto, todos estos [[Lógica y Estructuras Discretas/Estado|Estados]] fuente, excepto el [[Lógica y Estructuras Discretas/Estado|Estado]] inicial, son redundantes, y podemos omitirlos al momento de formar la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estados]] siguientes y el [[Diagrama de estados]].
