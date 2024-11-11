---
created: 2024-11-11 17:33:15
modified: 2024-11-11 17:39:46
title: Base ortogonal
---

# Base ortogonal

Una [[Base]] cuyos vectores son todos [[Vectores ortogonales]].

---

Sea $V$ un [[Espacio Vectorial con Producto Interno]], $W$ un [[Subespacio vectorial]] de $V$. Si $B = \set{u_1, \dots, u_n}$ es una [[Base ortogonal]] de $W$, luego $\forall x \in W$ es posible escribir $x$ como [[Combinación lineal]] de los vectores de $B$.

$$
x = \alpha_1 u_1 + \dots + \alpha_n u_n
$$

Y además, es posible calcular los coeficientes $\alpha_i$ sin necesidad de resolver un [[Sistema de ecuaciones lineales (SEL)]].

$$
\alpha_i =
\frac{\left< x, u_i \right>}{\left< u_i, u_i \right>} =
\frac{\left< x, u_i \right>}{{\Vert u_i \Vert}^2}
$$

^51769b

