---
created: 2024-10-30 11:43:40
modified: 2024-10-30 11:48:17
title: Polinomios de Taylor
---

# Polinomios de Taylor

Son una herramienta para realizar aproximaciones de [[Análisis Matemático I/Función|Funciones complejas]], en el [[Entorno]]

Cualquier polinomio se puede desarrollar en potencias de $x - c$.

$$
P(x) =
a_n (x - c)^n + \dots + a_2 (x - c)^2 + a_1 (x - c)^1 + a_0 =
\sum_{k = 0}^n a_k (x - c)^k
$$

Y será sencillo calcular $P(c) = a_0$.

> [!tip]
> En el desarrollo estándar, se utiliza $c = 0$.

$$
p^{(k)}(c) = k! \cdot a_k \Rightarrow a_k = \frac{p^{(k)}(c)}{k!}
$$
