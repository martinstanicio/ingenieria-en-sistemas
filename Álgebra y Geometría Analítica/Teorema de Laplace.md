---
created: 2024-04-29 14:08:45
modified: 2024-05-08 01:33:29
title: Teorema de Laplace
---

# Teorema de Laplace

Sea una [[Matriz]] $A \in k^{n \times n}$, luego se puede calcular el [[Determinante]] de $A$ desarrollando la definición por cualquier fila o columna.

## Desarrollo por columna $j$

$$
det(A) = \sum_{i=1}^n a_{ij} \cdot A_{ij} = \sum_{i=1}^n a_{ij} \cdot (-1)^{i+j} \cdot |M_{ij}|
$$

## Desarrollo por fila $i$

$$
det(A) = \sum_{j=1}^n a_{ij} \cdot A_{ij} = \sum_{j=1}^n a_{ij} \cdot (-1)^{i+j} \cdot |M_{ij}|
$$
