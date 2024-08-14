---
created: 2024-04-23 13:59:32
modified: 2024-08-14 00:28:46
title: Continuidad
---

# Continuidad

Una [[Análisis Matemático I/Función|Función]] es continua si cuando tomamos dos **puntos cercanos** de su [[Dominio]], sus **[[Imagen|Imágenes]] también serán cercanas**, es decir, ==no hay saltos en la gráfica== de la misma.

> [!tip]
> Una [[Análisis Matemático I/Función|Función]] es **continua** cuando podemos dibujarla sin levantar el lápiz del papel.

En [[Lenguaje formal]], para que $f$ sea continua en $c \in D_f$, se deben cumplir las siguientes condiciones:

- Debe existir [[Imagen]] en el punto analizado: $\exists f(c)$
- Debe existir el [[Límite]] de la [[Análisis Matemático I/Función|Función]] tendiendo al punto analizado: $\exists \lim\limits_{x \rightarrow c} f(x)$
- La [[Imagen]] y el [[Límite]] deben ser iguales: $f(c) = \lim\limits_{x \rightarrow c} f(x)$

## Discontinuidad esencial

Si una [[Análisis Matemático I/Función|Función]] $y = f(x)$ no es continua en un punto $c$, ya que **no existe el [[Límite]]** de $f(x)$ tendiendo a $c$, se dice que tiene una *discontinuidad esencial* en $c$.

$$
\nexists \lim\limits_{x \rightarrow c} f(x)
$$

## Discontinuidad evitable

Si una [[Análisis Matemático I/Función|Función]] $y = f(x)$ no es continua en un punto $c$, ya que **no existe la [[Imagen]]** de $f(x)$, o **no coincide con el [[Límite]]**, se dice que tiene una *discontinuidad evitable* en $c$.

$$
\nexists f(c)
\lor
f(c) \neq \lim\limits_{x \rightarrow c} f(x)
$$
