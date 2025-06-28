---
created: 2025-05-20 16:37:21
modified: 2025-05-20 17:31:43
title: Derivada direccional
---

# Derivada direccional

Mientras que las [[Derivada parcial|Derivadas parciales]] nos permiten calcular la razón de cambio de la [[Análisis Matemático I/Función|Función]] en la dirección de los ejes $x$ e $y$, la [[Derivada direccional]] $D_u$ nos permite calcular la razón de cambio en ==cualquier dirección==, en un punto dado $p_0$.

![[derivada-direccional.jpg]]

$$
D_u f(p_0) =
\lim_{h \to 0} \frac{f(p_0 + h \hat{u}) - f(p_0)}{h}
$$

- $h$ es la distancia entre dos puntos cercanos $p$ y $p_0$ (es la [[Norma]] del vector $\vec{h}$)
- $\hat{u}$ es el [[Versor]] que nos indica la dirección de la [[Derivada direccional]]

## Teorema

Si $f(p)$ es [[Diferencial|Diferenciable]] en $p$ entonces tiene una [[Derivada direccional]] en la dirección del [[Versor]] $\hat{u}$ y su valor es:

$$
D_u f(p) = \nabla f(p) \cdot \hat{u}
$$

## Máxima razón de cambio

Para encontrar la máxima razón de cambio, debemos calcular en qué dirección del [[Versor]] $\hat{u}$, la [[Derivada direccional]] alcanza su valor máximo.

$$
D_u f(p) =
\nabla f(p) \cdot \hat{u} =
\vert \nabla f(p) \vert \cdot \Vert \hat{u} \Vert \cdot \cos \theta =
\vert \nabla f(p) \vert \cdot \cos \theta
$$

- $\theta$ es el ángulo entre el [[Vector gradiente]] y el [[Versor]] $\hat{u}$

> [!tip]
> Debido a que la [[Norma]] de un [[Versor]] siempre es $1$, podemos descartar $\Vert \hat{u} \Vert$.

Como el valor del [[Vector gradiente]] en un punto no varía, el valor de la [[Derivada direccional]] está condicionado por $\cos \theta$. Por lo tanto, la [[Derivada direccional]] alcanzará su valor máximo cuando el [[Versor]] $\hat{u}$ tenga la misma dirección y sentido que el [[Vector gradiente]].

$$
\theta = 0
\Rightarrow
\cos \theta = 1
\Rightarrow
D_u f(p) = \vert \nabla f(p) \vert
$$

## Mínima razón de cambio

De forma análoga, obtendremos la mínima razón de cambio cuando el [[Versor]] $\hat{u}$ tenga la misma dirección, pero sentido opuesto al [[Vector gradiente]].

$$
\theta = \pi
\Rightarrow
\cos \theta = -1
\Rightarrow
D_u f(p) = - \vert \nabla f(p) \vert
$$

> [!important]
> Para las direcciones $\theta = \frac{\pi}{2}$ y $\theta = \frac{3}{2} \pi$, la [[Derivada direccional]] es nula, ya que $\cos \theta = 0$.
