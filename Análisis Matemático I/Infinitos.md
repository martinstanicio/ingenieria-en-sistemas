---
created: 2024-05-25 14:45:10
modified: 2024-05-25 15:25:03
title: Infinitos
---

# Infinitos

Cuando tenemos $\lim\limits_{x \to \alpha} f(x) = \infty$, podemos decir que $y = f(x)$ es un ==infinito para $x \rightarrow \alpha$==.

> [!info] $x \rightarrow \alpha$
> Cuando tenemos $x \rightarrow \alpha$, equivale a decir $x \rightarrow c \in \mathbb{R}$, $x \rightarrow +\infty$ o $x \rightarrow -\infty$.

Si sabemos que $y = f(x)$ es un infinito para $x \rightarrow \alpha$, entonces $y = k \cdot f(x), k \neq 0$ es un infinito para $x \rightarrow \alpha$.

## Orden de los infinitos

### Infinito de mayor orden ($f(x) \gg g(x)$)

Decimos que un infinito $f(x)$ es de ==mayor orden== que un infinito $g(x)$ si el primero crece más rápidamente que el segundo.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = \infty
$$

### Infinito de menor orden ($f(x) \ll g(x)$)

Decimos que un infinito $f(x)$ es de ==menor orden== que un infinito $g(x)$ si el segundo crece más rápidamente que el primero.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = 0
$$

### Infinitos similares ($f(x) \sim g(x)$)

Decimos que dos infinitos son ==similares== cuando ==son del mismo orden==, es decir, crecen de forma muy similar.

$$
\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = L \in \mathbb{R}, L \neq 0
$$

### Infinitos equivalentes ($f(x) \approx g(x)$)

Decimos que dos infinitos son ==similares== cuando ==son del mismo orden==, es decir, crecen de forma muy similar.
- Si sabemos que $f(x) \approx g(x)$: $\lim\limits_{x \rightarrow \alpha} \frac{f(x)}{g(x)} = L \in \mathbb{R}, L \neq 0$
