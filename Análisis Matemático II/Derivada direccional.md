---
created: 2025-05-20 16:37:21
modified: 2025-05-20 16:54:24
title: Derivada direccional
---

# Derivada direccional

Mientras que las [[Derivada parcial|Derivadas parciales]] nos permiten calcular la razón de cambio de la [[Análisis Matemático I/Función|Función]] en la dirección de los ejes $x$ e $y$, la [[Derivada direccional]] $D_u$ nos permite calcular la razón de cambio en ==cualquier dirección==, en un punto dado $p_0$.

$$
D_u f(p_0) =
\lim_{h \to 0} \frac{f(p_0 + h \vec{u}) - f(p_0)}{h}
$$

- $h$ es la distancia entre dos puntos cercanos $p$ y $p_0$ (es la [[Norma]] del vector $\vec{h}$)
- $\vec{u}$ es el [[Versor]] que nos indica la dirección de la [[Derivada direccional]]

## Teorema

Si $f(p)$ es [[Diferencial|Diferenciable]] en $p$ entonces tiene una [[Derivada direccional]] en la dirección del [[Versor]] $\vec{u}$ y su valor es:

$$
D_u f(p) = \nabla f(p) \cdot \vec{u}
$$
## Máxima razón de cambio
Esto significaría encontrar