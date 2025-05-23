---
created: 2024-06-14 21:02:56
modified: 2025-05-23 16:26:58
title: Recta tangente
---

# Recta tangente

Una recta que corta a una [[Análisis Matemático I/Función|Función]] en un **único punto**.

---

Si trabajamos con una [[Función real de variable real]] $y = f(x)$, la [[Recta tangente]] es de la siguiente forma.

$$
y = f(x) + f'(x) \cdot \Delta x
$$

---

Si trabajamos con una [[Función real de variable vectorial]] $z = f(x, y)$, y calculamos la [[Derivada parcial]] respecto de $x$ en un punto $\left( x_0, y_0 \right)$, podemos obtener las ecuaciones paramétricas de la [[Recta tangente]], tomando como parámetro $t = \Delta x = x - x_0$.

$$
\left\{
    \begin{array}{l}
        x = x_0 + t \\
        y = y_0 \\
        z = f \left( x_0, y_0 \right) + f_x \left( x_0, y_0 \right) \cdot t \\
    \end{array}
\right.
$$

Podemos hacer lo mismo, pero con la [[Derivada parcial]] respecto de $y$, tomando $t = \Delta y = y - y_0$

$$
\left\{
    \begin{array}{l}
        x = x_0 \\
        y = y_0 + t \\
        z = f \left( x_0, y_0 \right) + f_y \left( x_0, y_0 \right) \cdot t \\
    \end{array}
\right.
$$
