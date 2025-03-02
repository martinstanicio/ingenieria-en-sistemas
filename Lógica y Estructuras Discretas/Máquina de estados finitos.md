---
aliases:
  - MEF
created: 2025-03-01 20:56:30
modified: 2025-03-01 21:49:42
title: Máquina de estados finitos
---

# Máquina de estados finitos

Es una [[Máquina]] con una cantidad finita de [[Lógica y Estructuras Discretas/Estado|Estados]]. Es una séxtupla $M$.

$$
M = \left( I, O, k, q_0, f, g \right)
$$

- $I$: [[Conjunto]] finito de [[Entradas]] ($I \neq \emptyset$).
- $O$: [[Conjunto]] finito de [[Salidas]] ($O \neq \emptyset$).
- $k$: [[Conjunto]] finito de [[Lógica y Estructuras Discretas/Estado|Estados]] ($k \neq \emptyset$).
- $q_0$: El [[Lógica y Estructuras Discretas/Estado|Estado]] inicial de la [[Máquina]] ($q_0 \in k$).
- $f$: [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente, $f: \left( k \times I \right) \to k$. Para cada posible combinación de [[Lógica y Estructuras Discretas/Estado|Estados]] y [[Entradas]], asigna un [[Lógica y Estructuras Discretas/Estado|Estado]].
- $g$: [[Análisis Matemático I/Función|Función]] de [[Salidas|Salida]], $g: k \to O$ para [[Máquina de Moore|Máquinas de Moore]] y $g: \left( k \times I \right) \to O$ para [[Máquina de Mealy|Máquinas de Mealy]]. Para cada posible combinación de [[Lógica y Estructuras Discretas/Estado|Estados]] y [[Entradas]], asigna una [[Salidas|Salida]]. Para las [[Máquina de Moore|Máquinas de Moore]] solo se tiene en cuenta el [[Lógica y Estructuras Discretas/Estado|Estado]].
