---
created: 2024-11-18 14:55:31
modified: 2024-12-05 19:33:38
title: Grafo
---

# Grafo

Un [[Grafo]] es una terna de tres elementos.

$$
\left( V, A, \delta \right)
$$

Donde $V \neq \emptyset$ es el [[Conjunto]] cuyos elementos se llaman ==vértices==, $A$ es el [[Conjunto]] cuyos elementos se llaman ==aristas==, $\delta$ es una [[Análisis Matemático I/Función|Función]] llamada ==[[Relación]] de incidencia== $S: A \to X = \set{ \set{u, w}; u,v \in V }$.

> [!tip]
> Los **vértices** son los puntos, las **aristas** son las líneas, y la **relación de incidencia** determina qué par de vértices conecta cada arista.

Si $\delta (a) = \set{u, v}$, se dice que $a$ incide sobre $u$ y $v$; si $\delta (a) = \delta (b)$, se dice que $a$ y $b$ son ==aristas paralelas==; y si $\delta (a) = \set{u, u}$, se dice que $a$ es un ==lazo==.

---

![[grafo.png]]

La tabla que representa a este [[Grafo]] es la siguiente.

| $A$ | $\set{u, w}$ |
| --- | ------------ |
| $a$ | $\set{1, 2}$ |
| $b$ | $\set{2, 2}$ |
| $c$ | $\set{1, 3}$ |
| $d$ | $\set{3, 4}$ |
| $e$ | $\set{3, 4}$ |
| $f$ | $\set{3, 4}$ |
| $g$ | $\set{4, 5}$ |
| $h$ | $\set{5, 5}$ |
| $i$ | $\set{5, 5}$ |

> [!tip]
> [Graph Online](https://graphonline.top/)
