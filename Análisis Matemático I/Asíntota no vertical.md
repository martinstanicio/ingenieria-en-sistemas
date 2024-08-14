---
created: 2024-05-25 14:03:04
modified: 2024-08-14 00:52:40
title: Asíntota no vertical
---

# Asíntota no vertical

Si se cumple que las [[Imagen|Imágenes]] de una [[Análisis Matemático I/Función|Función]] $y = f(x)$ se acercan tanto como uno quiera al número $b$, con **$x$ lo suficientemente grande** (ya sea $+\infty$ o $-\infty$), la **recta $y = mx + b$ es asíntota** al gráfico de $y = f(x)$.

$$
\lim\limits_{x \to +\infty} f(x) = mx + b \Rightarrow y = b \text{ es asíntota horizontal para } x \rightarrow +\infty
$$

$$
\lim\limits_{x \to -\infty} f(x) = mx + b \Rightarrow y = b \text{ es asíntota horizontal para }  x \rightarrow -\infty
$$

> [!note]
> Si se cumple que ambos límites tienden al mismo punto.
>
> $$
> \lim\limits_{x \to +\infty} f(x) = \lim\limits_{x \to -\infty} f(x) = mx + b
> $$
>
> Podemos escribirlo en una sola expresión.
>
> $$
> \lim\limits_{x \to \infty} f(x) = mx + b
> $$

![[asintotas.png]]

## Pendiente

Para calcular la [[Pendiente]] $m$ de la [[Asíntota no vertical]], debemos realizar el siguiente cálculo.

$$
m = \lim\limits_{x \rightarrow \infty} \frac{f(x)}{x}
$$

> [!tip]
> Si la pendiente es $m = 0$, estamos ante una **asíntota horizontal**. Caso contrario, es una **asíntota oblicua**.

## Ordenada al origen

Para calcular la ordenada al origen $b$ de la [[Asíntota no vertical]], debemos realizar el siguiente cálculo.

$$
b = \lim\limits_{x \rightarrow \infty} (f(x) - mx)
$$
