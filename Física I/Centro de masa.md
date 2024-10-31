---
created: 2024-10-31 10:55:59
modified: 2024-10-31 12:20:40
title: Centro de masa
---

# Centro de masa

Es el punto en un **sistema de partículas** en el cual se puede considerar que está concentrada toda la masa, con el fin de analizar su [[Movimiento]].

> [!important]
> Este punto se comporta como si todas las [[Fuerza|Fuerzas]] externas estuvieran actuando sobre él.

## Posición

Para un sistema de partículas, podemos calcular la **posición** del [[Centro de masa]] $\vec{R}$ mediante la siguiente fórmula.

$$
\vec{R} =
\frac{\sum_{i=1}^n m_i \vec{r}_i}{\sum_{i=1}^n m_i} =
\frac{\sum_{i=1}^n m_i \vec{r}_i}{M}
$$

O en el caso de un cuerpo continuo, la siguiente fórmula.

$$
\vec{R} =
\frac{1}{M} \int \vec{r} \, dm
$$

Donde:

- $m_i$ es la masa de cada partícula.
- $M$ es la masa total del cuerpo.
- $\vec{r}_i$ es el vector de posición de cada partícula.
- $n$ es el número total de partículas.
- $dm$ es un elemento infinitesimal de masa en el cuerpo.

## Velocidad

Para un sistema de partículas, podemos calcular la **velocidad** del [[Centro de masa]] $\vec{V}$ mediante la siguiente fórmula.

> [!tip]
> La velocidad del centro de masa $\vec{V}$ se obtiene [[Derivada|Derivando]] la **posición** del centro de masa respecto al **tiempo**.

$$
\vec{V} =
\frac{d\vec{R}}{dt} =
\frac{\sum_{i=1}^n m_i \vec{v}_i}{\sum_{i=1}^n m_i} =
\frac{\sum_{i=1}^n m_i \vec{v}_i}{M}
$$

Donde:

- $\vec{v}_i$ es la velocidad de cada partícula.
