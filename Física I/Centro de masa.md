---
created: 2024-10-31 10:55:59
modified: 2024-10-31 10:59:11
title: Centro de masa
---
# Centro de masa

Es el punto en un **sistema de partículas** en el cual se puede considerar que está concentrada toda la masa, con el fin de analizar su [[Movimiento]].

> [!important]
> Este punto se comporta como si todas las [[Fuerza|Fuerzas]] externas estuvieran actuando sobre él.

## Fórmula para calcular la posición del centro de masa

Para un sistema discreto de partículas, la posición del centro de masa (\( \vec{R} \)) se calcula mediante la siguiente fórmula:

\[

\vec{R} = \frac{\sum_{i=1}^n m_i \vec{r}_i}{\sum_{i=1}^n m_i}

\]

donde:

- \( m_i \) es la masa de cada partícula.
- \( \vec{r}_i \) es el vector de posición de cada partícula.
- \( n \) es el número total de partículas.

En el caso de un cuerpo continuo, esta fórmula se convierte en una integral:

\[

\vec{R} = \frac{1}{M} \int \vec{r} \, dm

\]

donde:

- \( M \) es la masa total del cuerpo.
- \( dm \) es un elemento infinitesimal de masa en el cuerpo.

## Velocidad del centro de masa

La velocidad del centro de masa (\( \vec{V} \)) se obtiene derivando la posición del centro de masa respecto al tiempo:

\[

\vec{V} = \frac{d\vec{R}}{dt} = \frac{\sum_{i=1}^n m_i \vec{v}_i}{\sum_{i=1}^n m_i}

\]

donde \( \vec{v}_i \) es la velocidad de cada partícula.
