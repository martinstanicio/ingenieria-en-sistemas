---
created: 2024-11-11 18:41:47
modified: 2024-11-13 11:49:02
title: Proceso de Gram-Schmidt
---

# Proceso de Gram-Schmidt

Sea $V$ un [[Espacio Vectorial con Producto Interno]], luego es posible hallar una [[Base ortogonal]] $B$ para $B$.

> [!note]
> De la misma forma que un [[Espacio vectorial]] tiene infinitas [[Base|Bases]], también existen infinitas [[Base ortogonal|Bases ortogonales]].

El [[Proceso de Gram-Schmidt]] nos permite convertir una [[Base]] $B = \set{w_1, \dots, w_n}$ de $V$ en una [[Base ortogonal]] $B' = \set{u_1, \dots, u_n}$, también de $V$.

---

Para calcular cada uno de los vectores $u_i$, debemos calcular las [[Proyección|Proyecciones]] del vector sobre los calculados anteriormente.

$$
\array{
u_1 = w_1 \\
u_2 = w_2 - \text{proy}_{u_1} w_2 \\
u_3 = w_3 - \text{proy}_{u_1} w_3 - \text{proy}_{u_2} w_3 \\
\dots \\
u_n = w_n - \text{proy}_{u_1} w_n - \dots - \text{proy}_{u_{n - 1}} w_n \\
}
$$

> [!tip]
> Si quisieramos calcular una [[Base ortonormal]] $B'' = \set{x_1, \dots, x_n}$, debemos dividir a cada vector por su [[Norma]].
>
> $$
> \array{
> x_1 = \frac{u_1}{\Vert u_1 \Vert} \\
> \dots \\
> x_n = \frac{u_n}{\Vert u_n \Vert} \\
> }
> $$
