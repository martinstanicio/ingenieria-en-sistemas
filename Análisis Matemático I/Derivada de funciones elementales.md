---
created: 2024-08-15 00:55:43
modified: 2024-08-15 01:08:40
title: Derivada de funciones elementales
---

# Derivada de funciones elementales

Calculo de la [[Derivada]] de [[Análisis Matemático I/Función|Funciones]] **elementales**.

## Función constante

La [[Derivada]] de una [[Análisis Matemático I/Función|Función]] constante $f(x) = k$, con $k \in \mathbb{R}$, **siempre será $0$**.

$$
f(x) = k \Rightarrow f'(x) = 0
$$

Por ejemplo, con $f(x) = 1 \Rightarrow f'(x) = 0$.

```desmos-graph
top = 5; bottom = -5
---
f(x) = 1x^0
f'(x)|dashed
```

Como podemos ver en la siguiente demostración.

$$
f'(x) =
\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} =
\lim_{h \to 0} \frac{k - k}{h} =
\lim_{h \to 0} 0 =
0
$$

## Función potencial con exponente natural

La [[Derivada]] de una [[Análisis Matemático I/Función|Función]] exponencial $f(x) = x^n$, con $n \in \mathbb{N}$, **siempre será $n \cdot x^{n - 1}$**.

$$
f(x) = x^n \Rightarrow f'(x) = n \cdot x^{n - 1}
$$

Por ejemplo, con $f(x) = x^2 \Rightarrow f'(x) = 2x$.

```desmos-graph
f(x) = x^2
f'(x)|dashed
```

Como podemos ver en la siguiente demostración.

$$
f'(x) =
\lim_{t \to x} \frac{f(t) - f(x)}{t - x} =
\lim_{t \to x} \frac{t^n - x^n}{t - x}
$$
