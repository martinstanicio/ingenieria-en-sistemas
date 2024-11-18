---
aliases:
  - Grado
created: 2024-11-18 15:09:46
modified: 2024-11-18 15:33:28
title: Valencia
---

# Valencia

Dado un ==vértice== $u \in V$ de un [[Grafo]], se llama [[Valencia]] a la cantidad de ==aristas que inciden en $u$==.

$$
\text{val}(u) =
\text{gr}(u) =
\deg (u)
$$

> [!tip]
> La [[Valencia]] de un vértice es igual a la cantidad de veces que aparece en la tabla de la **relación de incidencia**.

En un [[Dígrafo]], la [[Valencia]] de un vértice es la suma de su [[Invalencia]] y su [[Exvalencia]].

$$
\text{val}(u) =
\text{inval}(u) + \text{exval}(u)
$$

---

La [[Valencia]] de un [[Grafo]] es la sumatoria de las [[Valencia|Valencias]] de sus vértices.

> [!important]
> La [[Valencia]] de un [[Grafo]] siempre es el ==doble de la cantidad de aristas==.
