---
aliases:
  - Teorema del valor medio
created: 2024-08-20 16:51:33
modified: 2024-08-20 18:38:22
title: Teorema de Lagrange
---

# Teorema de Lagrange

Dada una [[Análisis Matemático I/Función|Función]] $y = f(x)$, [[Continuidad|Continua]] en el **intervalo cerrado** $[a, b]$, y [[Derivada|Derivable]] en el **intervalo abierto** $(a, b)$.

Sabiendo esto, podemos afirmar que **existe al menos un punto** $c \in (a, b)$ tal que su [[Recta tangente]] es **paralela** a la [[Recta secante]] que une a los puntos $(a, f(a))$ y $(b, f(b))$.

![[lagrange.jpg]]

Por lo tanto, la [[Pendiente]] $m = f'(c)$ de la [[Recta tangente]] es igual a la [[Pendiente]] de la [[Recta secante]].

$$
f'(c) = \frac{f(b) - f(a)}{b - a}
$$
