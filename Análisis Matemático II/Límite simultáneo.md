---
aliases:
  - Límite doble
  - Límites simultaneos
  - Límites dobles
created: 2025-03-26 15:56:09
modified: 2025-05-19 18:14:55
title: Límite simultáneo
---

# Límite simultáneo

Sea una [[Función real de variable vectorial]] $z = f(x, y)$, un [[Punto de acumulación]] $(a, b)$ del [[Dominio]] de $f$, y un número real $L$.

> [!note]
> El comportamiento de $f(x, y)$ no es relevante en $(a, b)$, sino únicamente en su [[Entorno reducido]]. La [[Análisis Matemático I/Función|Función]] puede incluso no estar definida en $(a, b)$.

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

Si esto se cumple, se dice que el valor del [[Límite simultáneo]] de la [[Análisis Matemático I/Función|Función]] $z = f(x, y)$ al tender $(x, y)$ hacia $(a, b)$ es $L$.

> [!warning]
> Si el [[Límite simultáneo]] existe, debe ser **único**.
> 
> Entoneces, si el resultado del [[Límite]] no es el mismo para ==todas las trayectorias posibles==, el [[Límite simultáneo]] no existe.
