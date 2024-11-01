---
created: 2024-10-30 11:43:40
modified: 2024-11-01 14:42:33
title: Polinomio de Taylor
---

# Polinomio de Taylor

Es una herramienta para realizar aproximaciones de [[Análisis Matemático I/Función|Funciones]] **complejas**, en el [[Entorno]] de un punto $x = c$, utilizando **polinomios**.

Este polinomio tendrá la siguiente forma, desarrollado en potencias de $x - c$.

$$
P(x) =
a_n (x - c)^n + \dots + a_2 (x - c)^2 + a_1 (x - c)^1 + a_0 =
\sum_{k = 0}^n a_k (x - c)^k
$$

Y será sencillo calcular su [[Término independiente]] $P(c) = a_0$.

> [!tip]
> En el desarrollo estándar, se utiliza $c = 0$.

Para determinar el valor de los coeficientes del polinomio, debemos obtener la [[Derivada]] *k-ésima* de la [[Análisis Matemático I/Función|Función]] original evaluada en $x = c$, y dividirla por $k!$.

$$
p^{(k)}(c) = k! \cdot a_k \Rightarrow a_k = \frac{p^{(k)}(c)}{k!}
$$

## Residuo o error

Un [[Polinomio de Taylor]] nos permite obtener una **aproximación**, por lo que siempre habrá una diferencia con la [[Análisis Matemático I/Función|Función]] original.

$$
f(x) =
\sum_{k = 0}^n \frac{f^{(k)}(c)}{k!} (x - c)^k + \frac{f^{n + 1}(\alpha)}{(n + 1)!} (x - c)^{(n + 1)}
$$

> [!important]
> El error en $x = c$ siempre será $0$.
