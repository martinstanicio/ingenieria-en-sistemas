---
aliases:
  - Combinaciones sin repetición
created: 2025-03-26 19:10:45
modified: 2025-03-31 10:36:24
title: Combinaciones
---

# Combinaciones

Cantidad de grupos de $k$ elementos que se pueden formar dado un [[Conjunto]] de $n$ elementos, donde **el orden no importa**, sin repeticiones.

$$
C_k^n = \left( \begin{array}{c} n \\ k \end{array} \right) = \frac{n!}{k! \cdot (n - k)!} = \frac{P_n}{k!}
$$

> [!tip]
> Si $n = 5$ personas desean formar grupos de $k = 3$, existen $10$ posibles grupos.
>
> $$
> C_k^n = \left( \begin{array}{c} 5 \\ 3 \end{array} \right) = \frac{5!}{3! \cdot (5 - 3)!} = 10
> $$
