---
created: 2025-06-07 16:23:11
modified: 2025-06-07 16:26:42
title: Relación de composición
---
# Relación de composición

Sean $A$, $B$, $C$ tres [[Conjunto|Conjuntos]] y $R$, $G$ dos relaciones tal que:

$$
\left( R: A \to B \right)
\land
\left( G: B \to C \right)
$$

Luego la [[Relación de composición]] $R \circ G$ se define como:

$$
R \circ G =
\set{
    \left( a, c \right), a \in A, c \in C:
    \left( \exists b \in B \land aRb \land bGc \right)
}
$$
