---
created: 2024-05-01 17:34:29
modified: 2024-05-08 01:33:30
title: Composición de relaciones
---

# Composición de relaciones

La composición de dos [[Relación|relaciones]] es el [[Conjunto]] de pares ordenados, donde:

- La primera componente son elementos del conjunto de partida del primer conjunto.
- La segunda componente son elementos del conjunto de llegada del segundo conjunto.

$$
R_1: A \rightarrow B
$$

$$
R_2: B \rightarrow C
$$

$$
R_1 \circ R_2: A \rightarrow C = \{ (x,z): (x \in A) \land (z \in C) \land (\exists y \in B: ((x,y) \in A \times B) \land ((y,z) \in B \times C)) \}
$$
