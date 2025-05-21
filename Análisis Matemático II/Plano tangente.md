---
created: 2025-05-20 19:06:12
modified: 2025-05-20 19:21:25
title: Plano tangente
---

# Plano tangente

Similar a la [[Recta tangente]], es un [[Plano]] que corta a la superficie en un solo punto (considerando únicamente al [[Entorno]] del punto).

Dada una [[Análisis Matemático I/Función|Función]] $z = f(x, y)$, sabemos que el [[Vector gradiente]] es [[Vectores ortogonales|Ortogonal]] a la superficie de la [[Función implícita]] $F(x, y, z) = z - f(x, y)$. Luego, solo necesitamos un punto del [[Plano]] $p_0 = \left( x_0, y_0, z_0 \right)$ (puede ser el mismo punto donde evaluamos la [[Análisis Matemático I/Función|Función]]), y otro punto genérico $p = \left( x, y, z \right)$

$$
\left( p - p_0 \right) \cdot \nabla F(p_0) = \vec{0}
$$

> [!tip]
> Este [[Producto interno|Producto escalar]] debe ser nulo, ya que los vectores son [[Vectores ortogonales|Ortogonales]]:
> 
> - El [[Vector gradiente]] $\nabla F(p_0)$ es perpendicular al [[Plano tangente]]
> - $p$ y $p_0$ son puntos del [[Plano tangente]], entonces $\left( p - p_0 \right)$ es un vector paralelo a dicho [[Plano]].

Si expandimos los vectores, llegamos a lo siguiente:

$$
\left( x - x_0 \right) \cdot F_x \left( x_0, y_0, z_0 \right) +
\left( y - z_0 \right) \cdot F_y \left( x_0, y_0, z_0 \right) +
\left( z - z_0 \right) \cdot F_z \left( x_0, y_0, z_0 \right) =
0
$$
