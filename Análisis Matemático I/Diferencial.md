---
aliases:
  - Diferenciabilidad
created: 2024-08-19 15:06:55
modified: 2025-05-20 16:29:50
title: Diferencial
---

# Diferencial

Una [[Análisis Matemático I/Función|Función]] $f$ es [[Diferencial|Diferenciable]] o [[Diferencial|Localmente lineal]] en un punto $P$ si se puede escribir el incremento $\Delta f$ de la [[Análisis Matemático I/Función|Función]] como una [[Combinación lineal]] de los incrementos de las variables independientes, más un término que es despreciable frente al anterior cuando esos incrementos tienden a $0$.

$$
\Delta f =
\nabla f \cdot h + \epsilon(h) \cdot h =
\left( \nabla f + \epsilon(h) \right) \cdot h
$$

- $\nabla f$ es el [[Vector gradiente]] de $f$
- $h$ es el vector cuyas componentes son los incrementos de las variables independientes: $(\Delta x, \Delta y, \dots)$
- $\epsilon(h)$ es el vector que representa el error: $(\epsilon_1 (h), \epsilon_2 (h), \dots)$

> [!caution]
> Mientras mayor sean los incrementos de las variables independientes $h = (\Delta x, \Delta y, \dots) = (dx, dy, \dots)$, mayor será el error $\epsilon(h)$ o diferencia con respecto a la [[Análisis Matemático I/Función|Función]] original.

El incremento de la [[Análisis Matemático I/Función|Función]] en un punto $p = (x_0, y_0, \dots)$ de su [[Dominio]] donde es [[Diferencial|Diferenciable]] es:

$$
f(p + h) = f(p) + \nabla f(p) \cdot h + \epsilon(h) \cdot h
$$

Entonces, el [[Diferencial]] de la [[Análisis Matemático I/Función|Función]] es:

$$
df = \nabla f(p) \cdot h
$$

> [!tip]
> Si estamos trabajando con una [[Función real de variable real]], podemos expresar el [[Diferencial]] como simplemente:
>
> $$
> dy = df = f'(x) \cdot dx
> $$
>
> Esta expresión también nos explica de dónde sale la definición de la [[Derivada]] $\frac{df}{dx}$:
>
> $$
> \frac{df}{dx} = f'(x)
> $$

## Función real de variable real

En el caso de una [[Función real de variable real]], esto nos permite calcular la [[Imagen]] de la [[Recta tangente]] a un punto $\left( x_0, f(x_0) \right)$, para un determinado punto $\left( x_0 + \Delta x, f(x_0 + \Delta x) \right)$.

![[diferencial.png]]

> [!warning]
> Esto es una **aproximación lineal**, por lo que el resultado no es exacto.
>
> $$f(x_0 + \Delta x) \cong f(x_0) + f'(x_0) \cdot \Delta x$$

Por ejemplo, con $f(x) = \sqrt{x}$, sabemos que $f'(x) = \frac{1}{2 \sqrt{x}}$, buscamos aproximar $f(50) = \sqrt{50}$. Tomamos el ==valor más cercano conocido== $f(49) = \sqrt{49} = 7$, por lo que $\Delta x = 1$.

$$
\sqrt{50} \cong \sqrt{49} + \frac{1}{2 \sqrt{49}} \cdot 1 \Rightarrow
\sqrt{50} \cong 7 + \frac{1}{14}
$$

## Función real de variable vectorial

En el caso de una [[Función real de variable vectorial]], esto nos permite encontrar el [[Plano tangente]] a la superficie en un punto $\left( x_0, y_0, f(x_0, y_0) \right)$.

> [!tip]
> Si una [[Función real de variable vectorial]] es [[diferencial|Diferenciable]] en un punto, entonces es [[Continuidad|Continua]] en ese punto, pero **no necesariamente su recíproca**.

### Teorema

Si una [[Función real de variable vectorial]] tiene [[Derivada parcial|Derivadas parciales]] [[Continuidad|Continuas]] $f_x (x,y)$ y $f_y (x,y)$ en un disco $D$, cuyo interior contiene al punto $(a, b)$, entonces $f(x, y)$ es [[Diferencial|Diferenciable]] en $(a, b)$.
