---
created: 2024-11-13 19:05:41
modified: 2024-11-13 19:21:34
title: Cuadrados mínimos
---

# Cuadrados mínimos

Dado un [[Sistema de ecuaciones lineales (SEL)]] $AX = b$ que sea [[Sistema incompatible (SI)]], luego $\nexists \overline{x}$ tal que $A \overline{x} = b$. Sin embargo, muchas veces alcanza con hallar $\overline{b}$ que mejor ==aproxime== a $b$ en $\text{Col}(A)$, que en la práctica sería la [[Proyección]] de $b$ sobre $\text{Col}(A)$.

$$
\overline{b} = \text{proy}_{\text{Col}(A)} b
$$

---

Sea $A \in k^{m \times n}$ y $b \in k^m$, se llama solución de [[Cuadrados mínimos]] al vector $\overline{x} \in k^n$ tal que:

$$
\forall x \in k^n:
\Vert A \overline{x} - b \Vert \leq
\Vert Ax - b \Vert
$$

En este caso, la mejor aproximación para $b$ sería $\overline{b} = A \overline{x}$.

> [!warning]
> Como este proceso es una **aproximación**, tenemos un ==error de cuadrados mínimos==.
>
> $$
> e = \Vert \overline{b} - b \Vert
> $$

Para encontrar este valor $\overline{x}$, debemos resolver el siguiente [[Sistema de ecuaciones lineales (SEL)]].

$$
A^t A \overline{x} = A^t b
$$

Además, si las columnas de $A$ son [[Conjunto linealmente independiente|Linealmente independientes]], podemos aplicar el método de la ==pseudoinversa==:

$$
\overline{x} = \left( A^t A \right)^{-1} A^t b
$$
