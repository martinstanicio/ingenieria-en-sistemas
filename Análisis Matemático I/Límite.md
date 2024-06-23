---
created: 2024-04-23 14:09:56
modified: 2024-06-23 18:37:41
title: Límite
---

# Límite

El límite de una [[Análisis Matemático I/Función]] en un punto es el ==valor al cual se aproximan las imágenes== de sus puntos cercanos y adyacentes.

Si nos aproximamos por derecha y por izquierda del punto, y la imagen se acerca cada vez más a aquella del punto que estamos analizando, decimos que **el límite existe**.

$$
\left.
    \begin{array}{l}
        \lim\limits_{x \to a^-} f(x) = L \\
        \lim\limits_{x \to a^+} f(x) = L
    \end{array} 
\right\}
\lim\limits_{x \to a} f(x) = L
$$

![[limite.png]]

En este caso, el punto $A$ es límite, pero el punto $B$ no lo es.

## Clasificación de límites

Dependiendo del valor al que se aproxime un límite, podemos clasificarlo de diferentes formas.

### Límites determinados

Son aquellos que se aproximan a un número real $\mathbb{R}$.

### Límites infinitos

Son aquellos que se aproximan a $\infty$ o $-\infty$.

### Límites indeterminados

Son aquellos que se aproximan a un valor indefinido:

- Cero sobre cero: $\frac{0}{0}$
- Infinito sobre infinito: $\frac{\infty}{\infty}$

Cuando encontramos un límite indeterminado, debemos **salvarlo**.

> [!note]
> Escribir la expresión de una **forma equivalente** para poder simplificar y que pase a ser un [[Límite#Límites determinados|Límite determinado]]
