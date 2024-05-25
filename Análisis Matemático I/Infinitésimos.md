---
created: 2024-05-25 16:25:55
modified: 2024-05-25 17:16:54
title: Infinitésimos
---

# Infinitésimos

Cuando tenemos $\lim\limits_{x \to \alpha} f(x) = 0$, podemos decir que $y = f(x)$ es un ==infinitésimo para $x \rightarrow \alpha$==.

> [!info] $x \rightarrow \alpha$
> Cuando tenemos $x \rightarrow \alpha$, equivale a decir $x \rightarrow c \in \mathbb{R}$, $x \rightarrow +\infty$ o $x \rightarrow -\infty$.

## Orden de los infinitésimos

La *rapidez* con la que cada infinitésimo se aproxima a cero a medida que calculamos su [[Límite]] con $x$ tendiendo a $\alpha$.

$$
\ln^m (x) \ll x^p \ll a^x \ll x! \ll x^{kx}, (m > 0 \wedge p > 0 \wedge a > 1 \wedge k > 0)
$$

### Infinitésimo de mayor orden: $f(x) \gg g(x)$

Decimos que un infinitésimo $f(x)$ es de ==mayor orden== que un infinitésimo $g(x)$ si el primero se aproxima a cero más rápidamente que el segundo.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = 0
$$

### Infinitésimo de menor orden: $f(x) \ll g(x)$

Decimos que un infinitésimo $f(x)$ es de ==menor orden== que un infinitésimo $g(x)$ si el segundo se aproxima a cero más rápidamente que el primero.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = \infty
$$

### Infinitésimos similares: $f(x) \sim g(x)$

Decimos que dos infinitésimos son ==similares== cuando ==son del mismo orden==, es decir, se aproximan a cero de forma muy similar.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = L \in \mathbb{R}, L \neq 0
$$

### Infinitésimos equivalentes: $f(x) \approx g(x)$

Decimos que dos infinitésimo son ==equivalentes== cuando ==se aproximan a cero con exactamente la misma rapidez==.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = L = 1
$$

> [!info]
> Todo factor de una expresión se puede **sustituir** por un infinitésimo **equivalente** sin que esto altere el límite de la expresión.

## Infinitésimos equivalentes conocidos

Existen una serie de [[Infinitésimos#Infinitésimos equivalentes $f(x) approx g(x)$|infinitésimos equivalentes]] notables.

Con $x \rightarrow 0$:

- $e^x - 1 \approx x$
- $a^x - 1 \approx x \cdot \ln a, a > 0$
- $\sin x \approx x$
- $\tan x \approx x$
- $1 - \cos x \approx \frac{x^2}{2}$
- $\arcsin x \approx x$
- $\arctan x \approx x$
- $\ln(x + 1) \approx x$

Con $x \rightarrow 1$:

- $\ln(x) \approx x - 1$
- $x^a - 1 \approx a(x - 1), a \neq 0$
