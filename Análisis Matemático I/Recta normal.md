---
aliases:
  - Vector normal
created: 2024-07-05 21:51:04
modified: 2025-05-20 19:07:50
title: Recta normal
---

# Recta normal

Una recta **perpendicular** a la [[Recta tangente]].

$$
- \frac{1}{f'(x)}
$$

> [!tip]
> La [[Pendiente]] $m$ de la [[Recta normal]] es **opuesta** e **inversa** a la de la [[Recta tangente]].

---

Si se busca encontrar el [[Recta normal|Vector normal]] de una superficie $z = f(x, y)$ en el punto $(x_0, y_0, z_0)$, es tan sencillo como calcular el [[Vector gradiente]] de la [[Función implícita]] $F(x, y, z) = z - f(x, y)$, ya que el mismo siempre es [[Vectores ortogonales|Ortogonal]] a la gráfica de la [[Función implícita]].

$$
\nabla F (x_0, y_0, z_0) =
\left( F_x (x_0, y_0, z_0), F_y (x_0, y_0, z_0), F_z (x_0, y_0, z_0) \right) =
\left\{
    \begin{array}{l}
    x = x_0 + \lambda F_x (x_0, y_0, z_0) \\
    y = y_0 + \lambda F_y (x_0, y_0, z_0) \\
    z = z_0 + \lambda F_z (x_0, y_0, z_0) \\
    \end{array}
\right.
$$
