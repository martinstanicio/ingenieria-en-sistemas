---
created: 2024-08-15 13:57:36
modified: 2024-08-15 14:32:05
title: Reglas de derivación
---

# Reglas de derivación

Reglas para calcular la [[Derivada]] de diferentes [[Análisis Matemático I/Función|Funciones]].

## Múltiplo constante

Dada una [[Análisis Matemático I/Función|Función]] $f(x)$ **derivable** en $x$, y dada $c(x)$ la [[Análisis Matemático I/Función|Función]] resultante de multiplicar una constante $k \in \mathbb{R}$ por $f(x)$.

$$
c(x) = k \cdot f(x) \Rightarrow c'(x) = k \cdot f'(x)
$$

Como podemos ver en la siguiente demostración.

$$
c'(x) =
\lim_{h \to 0} \frac{c(x + h) - c(x)}{h} =
\lim_{h \to 0} \frac{k \cdot f(x + h) - k \cdot f(x)}{h} =
\lim_{h \to 0} \left( k \cdot \frac{f(x + h) - f(x)}{h} \right) =
k \cdot f'(x)
$$

Por ejemplo, con $c(x) = 2 \cdot x^5$, la [[Derivada]] es $c'(x) = 2 \cdot 5x^4 = 10x^4$.

```desmos-graph
c(x) = 2x^5
c'(x)|dashed
```

## Suma

Dada las [[Análisis Matemático I/Función|Funciones]] $f(x)$ y $g(x)$ **derivables** en $x$, y dada $s(x)$ la [[Análisis Matemático I/Función|Función]] resultante de sumar a ambas.

$$
s(x) = f(x) + g(x) \Rightarrow s'(x) = f'(x) + g'(x)
$$

Como podemos ver en la siguiente demostración.

$$
s'(x) =
\lim_{h \to 0} \frac{s(x + h) - s(x)}{h} =
\lim_{h \to 0} \frac{f(x + h) + g(x + h) - f(x) - g(x)}{h} =
\lim_{h \to 0} \frac{f(x + h) + g(x + h) - f(x) - g(x)}{h}
$$

Por ejemplo, con $c(x) = 2 \cdot x^5$, la [[Derivada]] es $c'(x) = 2 \cdot 5x^4 = 10x^4$.

```desmos-graph
c(x) = 2x^5
c'(x)|dashed
```
