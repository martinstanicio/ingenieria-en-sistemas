---
aliases:
  - Gramáticas libres de contexto
  - GLC
created: 2025-06-15 00:58:32
modified: 2025-06-15 19:17:44
title: Gramática libre de contexto
---
	
# Gramática libre de contexto

Una [[Gramática]] considerada ==libre de contexto o tipo 2== según la [[Clasificación de Chomsky]].

> [!important]
> A las [[Lógica y Estructuras Discretas/Cadena|Cadenas]] generadas por una [[Gramática libre de contexto]] se les puede asociar un [[Árbol de derivación]].

## Pasaje de GLC a AP que acepta por pila vacía

Sea una [[Gramática libre de contexto|GLC]] $G = \left< N, T, P, S \right>$, el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] generado por la misma puede ser representado por un [[Autómata de pila|AP]] $M = \left< K, \Sigma, \Gamma, \delta, q_0, z_0, F \right>$ que acepta por [[Pila]] vacía, tal que $L(G) = L(M)$.

Primero definimos el [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] finales $F = \emptyset$; el [[Alfabeto]] de [[Entradas|Entrada]] $\Sigma = T$; el [[Alfabeto]] de la [[Pila]] $\Gamma = N \cup T$; el [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] $K = \set{ q_0 }$; la configuración inicial de la [[Pila]] $z_0 = S$; y finalmente, la [[Función de transición]] $\delta$:

$$
\delta \left( q_0, a, t \right) =
\left\{
    \begin{array}{l}
        \set{ \left( q_0, \alpha \right) }: \left( t \to \alpha \right) \in P \space &\text{si} \space t \in N \land a = \lambda \\
        \set{ \left( q_0, \lambda \right) } \space &\text{si} \space t \in T \land a = t \\
    \end{array}
\right.
$$
