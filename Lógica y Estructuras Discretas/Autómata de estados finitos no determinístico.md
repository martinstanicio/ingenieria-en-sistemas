---
aliases:
  - Autómatas de estados finitos no determinísticos
  - AEFND
created: 2025-03-06 14:40:22
modified: 2025-03-06 14:50:50
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
Sea $G = \left( N, T, P, S_0 \right)$ una [[Gramática#Tipo 3 Regular|Gramática regular]], luego existe $M = \left( I, k, q_0, f, A \right)$ un [[Autómata de estados finitos no determinístico|AEFND]]