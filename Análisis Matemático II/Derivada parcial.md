---
aliases:
  - Derivadas parciales
created: 2025-05-20 13:56:50
modified: 2025-05-20 14:28:27
title: Derivada parcial
---

# Derivada parcial

Las [[Derivada parcial|Derivadas parciales]] permiten estudiar el efecto que se produce en una [[Función real de variable vectorial]] al ==variar una variable== independiente, manteniendo ==fijas las demás==.

> [!note]
> Al igual que la [[Derivada]] de una [[Función real de variable real]], representa la [[Pendiente]] de la [[Recta tangente]] a la curva en un punto.
> 
> ![[derivada-parcial.jpg]]
> 
> Esta curva es la curva de [[Intersección (∩)]] de la superficie con el [[Plano]] que contiene a la dirección dada. En el caso de la [[Derivada parcial]] respecto a $x$, el [[Plano]] es paralelo al [[Plano]] $xz$.

Dada una [[Análisis Matemático I/Función|Función]] $z = f(x, y)$, si queremos calcular la [[Derivada parcial]] respecto de $x$, debemos mantener la $y$ constante. Entonces, el proceso es similar a calcular la [[Derivada]] de una [[Análisis Matemático I/Función|Función]] de una sola variable.

$$
\frac{\partial z}{\partial x} =
\frac{\partial f}{\partial x} =
f_x \left( x, y \right) =
\lim_{\Delta x \to 0} \frac{f \left( x + \Delta x, y \right) - f \left( x, y \right)}{\Delta x}
$$

> [!tip]
> Podemos usar las [[Reglas de derivación]], simplemente considerando a $y$ (en este caso) como una constante.

---

Por ejemplo, dada la [[Función real de variable vectorial]] $f(x, y) = 3 x^2 y + x y^2$, podemos calcular su [[Derivada parcial]] respecto a $x$:

$$
\frac{\partial f}{\partial x} =
f_x \left( x, y \right) =
6xy + y^2
$$

También podemos calcular su [[Derivada parcial]] respecto a $y$:

$$
\frac{\partial f}{\partial y} =
f_y \left( x, y \right) =
3x^2 + 2xy
$$
