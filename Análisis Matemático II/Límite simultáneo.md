---
aliases:
  - Límite doble
  - Límites simultaneos
  - Límites dobles
created: 2025-03-26 15:56:09
modified: 2025-05-19 17:21:11
title: Límite simultáneo
---

# Límite simultáneo

Sea una [[Función real de variable vectorial]] $z = f(x, y)$, un [[Punto de acumulación]] $(a, b)$ del [[Dominio]] de $f$, y un número real $L$.

$$
\lim_{(x, y) \to (a, b)} f(x, y) = L
\Leftrightarrow
\left\{
  \forall \epsilon > 0 \exists \delta > 0:
  0 < \sqrt{\left( x - a \right)^2 + \left( y - b \right)^2} < \delta
  \Rightarrow
  \vert f(x) - L \vert < \epsilon
\right\}
$$

Si esto se cumple, se dice 

> [!note]
> El comportamiento de $f(x, y)$ no es relevante en $(a, b)$, sino únicamente en su [[Entorno reducido]]. La [[Análisis Matemático I/Función|Función]] puede incluso no estar definida en $(a, b)$.
