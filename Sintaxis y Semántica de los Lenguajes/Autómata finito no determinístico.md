---
aliases:
  - AFND
  - Autómatas finitos no determinísticos
  - AEFND
  - Autómata de estados finitos no determinístico
  - Autómatas de estados finitos no determinísticos
created: 2025-03-06 14:40:22
modified: 2025-06-10 17:45:39
title: Autómata finito no determinístico
---

# Autómata finito no determinístico

Se llama [[Autómata finito no determinístico]] a la quíntupla $M$.

$$
M = \left( I, K, q_0, \delta, F \right)
$$

- $I$: [[Conjunto]] finito de [[Entradas]] ($I \neq \emptyset$), que suele ser el [[Alfabeto]] $\Sigma$.
- $K$: [[Conjunto]] finito de [[Lógica y Estructuras Discretas/Estado|Estados]] ($K \neq \emptyset$).
- $q_0$: El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial del [[Autómata]] ($q_0 \in K$).
- $\delta$: [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente, $\delta: \left( K \times I \right) \to P \left( K \right)$, donde $P(K)$ es el [[Conjunto potencia]] del [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $K$.
- $F$: [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] aceptados o finales ($F \subseteq K$).

> [!tip]
> La única diferencia con los [[Autómata finito|AFD]] es que la [[Imagen]] de la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estados]] está formada por los elementos del [[Conjunto potencia]] de $k$.
> 
> Por lo tanto, dado $K = \set{A, B, C}$, tanto $\emptyset$, $\set{A, C}$, $\set{B}$, y $\set{A, B, C}$ son algunas de las posibles [[Imagen|Imágenes]] de la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estados]].

## Teorema de pasaje de GR a AFND

Sea $G = \left( N, T, P, S_0 \right)$ una [[Gramática#Tipo 3 Regular|Gramática regular]], luego existe $M = \left( I, K, q_0, \delta, F \right)$ un [[Autómata finito no determinístico|AFND]] tal que $L(G) = Ac(M)$ donde:

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

## Teorema de pasaje de AFND a AFD

Sea $M = \left( I, K, q_0, \delta, F \right)$ un [[Autómata finito no determinístico|AFND]]. Luego existe $M' = \left( I', K', {q_0}', \delta', F' \right)$ un [[Autómata finito|AFD]] tal que $Ac(M) = Ac(M')$ donde:

$$
\begin{array}{c}
    I' = I \\
    K' = P(K) \\
    {q_0}' = \set{q_0} \\
    \delta '(X, a) = \left\{
        \begin{array}{c}
            \bigcup_{Y \in X} \delta (Y, a) \\
            \emptyset \space \text{si} \space X = \emptyset
        \end{array}
    \right. \\
    F' = \set{ X \in P(K): x \cap \set{f} \neq \emptyset, f \in F } \\
\end{array}
$$

Como $K' = P(K)$, es decir, $K'$ es el [[Conjunto potencia]] de $K$, muchas veces obtendremos un [[Autómata finito|AFD]] con múltiples [[Lógica y Estructuras Discretas/Estado|Estados]] ==fuente==, es decir, [[Lógica y Estructuras Discretas/Estado|Estados]] a los que no es posible llegar si tomamos un [[Lógica y Estructuras Discretas/Estado|Estado]] inicial diferente. Por lo tanto, todos estos [[Lógica y Estructuras Discretas/Estado|Estados]] fuente, excepto el [[Lógica y Estructuras Discretas/Estado|Estado]] inicial, son redundantes, y podemos omitirlos al momento de formar la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estados]] siguientes y el [[Diagrama de transición|Diagrama de estados]].
