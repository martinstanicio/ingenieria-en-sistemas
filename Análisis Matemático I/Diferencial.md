---
created: 2024-08-19 15:06:55
modified: 2024-08-23 12:12:09
title: Diferencial
---

# Diferencial

El [[Diferencial]] $df = dy$ nos permite realizar una **aproximación lineal** de cómo cambia $y = f(x)$ a medida que cambia el valor de $x$. Este cambio $\Delta x = x - x_0$ se llama $dx$.

> [!important]
> El [[Diferencial]] de una [[Análisis Matemático I/Función|Función]] es **único**.

> [!caution]
> Mientras mayor sea $dx = \Delta x$, **mayor será el error** $\epsilon$ o diferencia con respecto a la [[Análisis Matemático I/Función|Función]] original. Por lo tanto, el [[Diferencial]] $df = dy$ es más útil mientras más pequeño sea $dx = \Delta x$.

Si una [[Análisis Matemático I/Función|Función]] es [[Derivada|Derivable]] en $x$, entonces es **diferenciable**, y podemos encontrar el $df = dy$ correspondiente de la siguiente forma.

$$
df = f'(x) \cdot dx \Leftrightarrow \frac{df}{dx} = f'(x)
$$

Como podemos ver, lo que hacemos es calcular la [[Imagen]] de la [[Recta tangente]] a $f(x_0)$, para un determinado valor $x_0 + \Delta x$.

![[diferencial.png]]

> [!tip]
> Debido a que esto es una **aproximación lineal**, el resultado no es exacto.
>
> $$df \cong \Delta f$$
>
> Para obtener este valor aproximado de la [[Análisis Matemático I/Función|Función]] $f(x)$ en $x_0 + \Delta x$, realizamos lo siguiente.
>
> $$f(x_0 + \Delta x) \cong f(x_0) + f'(x_0) \cdot \Delta x$$

Por ejemplo, con $f(x) = \sqrt{x}$, sabemos que $f'(x) = \frac{1}{2 \sqrt{x}}$, buscamos aproximar $f(50) = \sqrt{50}$. Tomamos el ==valor más cercano conocido== $f(49) = \sqrt{49} = 7$, por lo que $\Delta x = 1$.

$$
\sqrt{50} \cong \sqrt{49} + \frac{1}{2 \sqrt{49}} \cdot 1 \Rightarrow
\sqrt{50} \cong 7 + \frac{1}{14}
$$
