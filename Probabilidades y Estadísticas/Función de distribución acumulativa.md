---
aliases:
  - Funciones de distribución acumulativa
  - Función de distribución acumulada
  - Funciones de distribución acumulada
  - FDA
created: 2025-06-22 20:45:35
modified: 2025-06-24 01:14:13
title: Función de distribución acumulativa
---

# Función de distribución acumulativa

La [[Función de distribución acumulativa]] $F \left( x \right)$ de una [[Variable aleatoria discreta]] $X$ con una [[Función de densidad de probabilidad]] $p \left( x \right)$ se define para cada número $x$ como:

$$
F \left( x \right) = P \left( X \leq x \right) = \sum_{y: y \leq x} p \left( y \right)
$$

> [!tip]
> Para cualquier número $x$, $F \left( x \right)$ es la [[Probabilidad]] de que el valor observado de $X$ será como máximo $x$.

Por ejemplo, dada la siguiente [[Función de distribución acumulativa]], es posible representarla mediante un gráfico.

$$
F \left( y \right) =
\left\{
    \begin{array}{l}
        0 \space &\text{si} \space y < 1 \\
        0.4 \space &\text{si} \space 1 \leq y < 2 \\
        0.7 \space &\text{si} \space 2 \leq y < 3 \\
        0.9 \space &\text{si} \space 3 \leq y < 4 \\
        1 \space &\text{si} \space 4 \leq y \\
    \end{array}
\right.
$$

![[función-de-distribución-acumulativa-1.jpg]]

---

La [[Función de distribución acumulativa]] $F \left( x \right)$ de una [[Variable aleatoria continua]] $X$ se define para cada número $x$ como:

$$
F \left( x \right) =
P \left( X \leq x \right) =
\int_{- \infty}^x f \left( y \right) dy
$$

![[función-de-distribución-acumulativa-2.jpg]] Una [[Función de densidad de probabilidad]] y [[Función de distribución acumulativa]] asociada.

> [!important]
> Si $X$ es una [[Variable aleatoria continua]] con [[Función de densidad de probabilidad]] $f \left( x \right)$ y [[Función de distribución acumulativa]] $F \left( x \right)$, entonces cada $x$ hace posible que la [[Derivada]] $F' \left( x \right)$.
>
> $$
> F' \left( x \right) = f \left( x \right)
> $$
