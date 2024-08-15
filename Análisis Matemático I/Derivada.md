---
created: 2024-06-14 20:56:27
modified: 2024-08-15 00:16:27
title: Derivada
---

# Derivada

La [[Pendiente]] $m$ de la [[Recta tangente]] de una [[Análisis Matemático I/Función|Función]] en un punto dado $x = c$.

$$
m = f'(c) =
\lim_{x \to c} \frac{f(x) - f(c)}{x - c}
$$

> [!note]
> Existen múltiples nomenclaturas para trabajar con [[Derivada|Derivadas]].
>
> $$
> f'(c) =
> \frac{df}{dx}(c) =
> D_x f(c) =
> D \space f(c)
> $$

Si consideramos $h = x - c$ y $x = c + h$, podemos llegar a la siguiente conclusión.

$$
f'(c) =
\lim_{h \to 0} \frac{f(c + h) - f(c)}{h}
$$

![[derivada.png]]

> [!tip]
> Si una [[Análisis Matemático I/Función|Función]] es **derivable** en $x = c$, podemos afirmar que también es [[Continuidad|Continua]] en $x = c$.
>
> $$
> \exists f'(c) \Rightarrow
> \lim_{x \to c} f(x) = f(c)
> $$
>
> Sin embargo, que una [[Análisis Matemático I/Función|Función]] sea [[Continuidad|Continua]] en un punto, **no significa que sea derivable**.
