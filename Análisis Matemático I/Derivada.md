---
created: 2024-06-14 20:56:27
modified: 2024-08-19 21:08:26
title: Derivada
---

# Derivada

La [[Pendiente]] $m$ de la [[Recta tangente]] de una [[Análisis Matemático I/Función|Función]] en un punto dado $x = c$. La obtenemos calculando el [[Límite]] del [[Cociente incremental]] cuando $x$ tiende a $c$.

$$
m = f'(c) =
\lim_{x \to c} \frac{f(x) - f(c)}{x - c}
$$

> [!note]
> Existen múltiples nomenclaturas para trabajar con [[Derivada|Derivadas]].
>
> $$
> f' =
> \frac{df}{dx} =
> D_x f =
> D \space f
> $$

Si consideramos $h = x - c$ y $x = c + h$, podemos llegar a la siguiente conclusión.

$$
f'(c) =
\lim_{h \to 0} \frac{f(c + h) - f(c)}{h}
$$

> [!warning]
> Es importante que este sea un [[Límite#Límites determinados|Límite determinado]], pues si es un [[Límite#Límites infinitos|Límite infinito]], **no existe** la [[Derivada]] en el punto.

![[derivada.png]]

> [!tip]
> Si una [[Análisis Matemático I/Función|Función]] es **derivable** en $x = c$, entonces es [[Continuidad|Continua]] en $x = c$.
>
> $$
> \exists f'(c) \Rightarrow
> \lim_{x \to c} f(x) = f(c)
> $$
>
> También resulta util su contrarrecíproca, pues, si una [[Análisis Matemático I/Función|Función]] no es [[Continuidad|Continua]] en $x = c$, entonces no es **derivable** en $x = c.
