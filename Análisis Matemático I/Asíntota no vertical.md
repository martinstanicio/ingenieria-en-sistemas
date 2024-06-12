---
created: 2024-05-25 14:03:04
modified: 2024-05-25 18:33:54
title: Asíntota no vertical
---

# Asíntota no vertical

Si se cumple que las imágenes de una [[Análisis Matemático I/Función]] $y = f(x)$ se acercan tanto como uno quiera al número $b$ con $x$ lo suficientemente grande (ya sea $+\infty$ o $-\infty$), la recta $y = b$ es asíntota al gráfico de $y = f(x)$.

$$
\lim\limits_{x \to +\infty} f(x) = b \Rightarrow y = b \text{ es asíntota horizontal para } x \rightarrow +\infty
$$

$$
\lim\limits_{x \to -\infty} f(x) = b \Rightarrow y = b \text{ es asíntota horizontal para }  x \rightarrow -\infty
$$

> [!info]
> Si se cumple que $\lim\limits_{x \to +\infty} f(x) = \lim\limits_{x \to -\infty} f(x) = b$, podemos expresarlo como $\lim\limits_{x \to \infty} f(x) = b$.

## Pendiente

Para calcular la pendiente $m$ de la asíntota no vertical, debemos realizar el siguiente cálculo.

$$
m = \lim\limits_{x \rightarrow \infty} \frac{f(x)}{x}
$$

> [!info] Asíntota horizontal
> Si la pendiente es $m = 0$, estamos ante una **asíntota horizontal**.

## Ordenada al origen

Para calcular la ordenada al origen $b$ de la asíntota no vertical, debemos realizar el siguiente cálculo.

$$
b = \lim\limits_{x \rightarrow \infty} (f(x) - mx)
$$
