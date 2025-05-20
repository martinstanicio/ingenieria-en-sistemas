---
aliases:
  - Derivadas parciales
created: 2025-05-20 13:56:50
modified: 2025-05-20 14:11:43
title: Derivada parcial
---

# Derivada parcial

Las [[Derivada parcial|Derivadas parciales]] permiten estudiar el efecto que se produce en una [[Función real de variable vectorial]] al ==variar una variable== independiente, manteniendo ==fijas las demás==.

> [!note]
> Al igual que la [[Derivada]] de una [[Función real de variable real]], representa una razón de cambio.

Dada una [[Análisis Matemático I/Función|Función]] $z = f(x, y)$, si queremos calcular la [[Derivada parcial]] respecto de $x$, debemos mantener la $y$ constante. Entonces, el proceso es similar a calcular la [[Derivada]] de una [[Análisis Matemático I/Función|Función]] de una sola variable.

$$
\frac{\partial z}{\partial x} =
\frac{\partial f}{\partial x} =
f_x \left( x, y \right) =
\lim_{\Delta x \to 0} \frac{f \left( x + \Delta x, y \right) - f \left( x, y \right)}{\Delta x}
$$

> [!tip]
> El símbolo $\partial$ tiene el nombre de *d de Jacobi*.
