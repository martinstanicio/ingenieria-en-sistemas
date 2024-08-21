---
created: 2024-08-21 00:32:39
modified: 2024-08-21 01:04:41
title: "Regla de L'Hopital"
---

# Regla de L'Hopital

Dadas dos [[Análisis Matemático I/Función|Funciones]] $y = f(x)$ y $y = g(x)$, [[Derivada|Derivables]] en un **intervalo abierto** $(a, b)$. Si existe un punto $c \in (a, b)$, tal que $\forall x \in (a, b) - \set{c}: g'(x) \neq 0$ y $f(c) = g(c) = 0$, y existe $\lim_{x \to c} \frac{f'(x)}{g'(x)}$.

$$
\exists c \in (a, b): \left(
    \left(
        \forall x \in (a, b) - \set{c}: g'(x) \neq 0
    \right) \land
    \left(
        f(c) = g(c) = 0
    \right) \land
    \exists \lim_{x \to c} \frac{f'(x)}{g'(x)}
\right)
$$

Entonces, podemos afirmar que existe $\lim_{x \to c} \frac{f(x)}{g(x)}$, y además, $\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$.

$$
\left(
    \exists \lim_{x \to c} \frac{f(x)}{g(x)}
\right) \land
\left(
    \lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}
\right)
$$

> [!tip]
> En la práctica, cuando encontramos una [[Indeterminación]] de tipo $$ la [[Regla de L'Hopital]]