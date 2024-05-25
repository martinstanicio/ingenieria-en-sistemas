---
created: 2024-05-25 14:45:10
modified: 2024-05-25 16:35:24
title: Infinitos
---

# Infinitos

Cuando tenemos $\lim\limits_{x \to \alpha} f(x) = \infty$, podemos decir que $y = f(x)$ es un ==infinito para $x \rightarrow \alpha$==.

> [!info] $x \rightarrow \alpha$
> Cuando tenemos $x \rightarrow \alpha$, equivale a decir $x \rightarrow c \in \mathbb{R}$, $x \rightarrow +\infty$ o $x \rightarrow -\infty$.

Si sabemos que $y = f(x)$ es un infinito para $x \rightarrow \alpha$, entonces $y = k \cdot f(x), k \neq 0$ es un infinito para $x \rightarrow \alpha$.

## Orden de los infinitos

La *rapidez* con la que crece cada infinito a medida que calculamos su [[Límite]] con $x$ tendiendo a $\alpha$.

$$
\ln^m (x) \ll x^p \ll a^x \ll x! \ll x^{kx}, (m > 0 \wedge p > 0 \wedge a > 1 \wedge k > 0)
$$

> [!info]
> Al multiplicar un infinito por una constante **no nula**, se obtiene un infinito de mismo orden.

### Infinito de mayor orden: $f(x) \gg g(x)$

Decimos que un infinito $f(x)$ es de ==mayor orden== que un infinito $g(x)$ si el primero crece más rápidamente que el segundo.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = \infty
$$

### Infinito de menor orden: $f(x) \ll g(x)$

Decimos que un infinito $f(x)$ es de ==menor orden== que un infinito $g(x)$ si el segundo crece más rápidamente que el primero.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = 0
$$

### Infinitos similares: $f(x) \sim g(x)$

Decimos que dos infinitos son ==similares== cuando ==son del mismo orden==, es decir, crecen de forma muy similar.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = L \in \mathbb{R}, L \neq 0
$$

### Infinitos equivalentes: $f(x) \approx g(x)$

Decimos que dos infinitos son ==equivalentes== cuando ==crecen con exactamente la misma rapidez==.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = L = 1
$$

> [!info]
> Todo factor de una expresión se puede **sustituir** por un infinito **equivalente** sin que esto altere el límite de la expresión.
