---
created: 2024-08-20 20:37:22
modified: 2024-08-20 20:49:54
title: Criterio de la primera derivada
---

# Criterio de la primera derivada

Este criterio nos sirve para determinar [[Extremo relativo|Extremos]]. Dada una [[Análisis Matemático I/Función|Función]] $y = f(x)$, [[Continuidad|Continua]] en $[a, b]$, [[Derivada|Derivable]] en $(a, b)$, y $c$ un [[Punto crítico]].

## Mínimo relativo

Si $f'(x) < 0$ cuando $x < c$, y $f'(x) > 0$ cuando $x > c$, es decir, la [[Análisis Matemático I/Función|Función]] **decrece antes** de $c$, y **crece después** de $c$, entonces $x = c$ es un [[Extremo relativo|Mínimo relativo]] de $y = f(x)$.

Por ejemplo, con $f(x) = x^2$, tenemos un mínimo relativo en $x = 0$.

```desmos-graph
left = -5; right = 5;
top = 5; bottom = -5;
---
f(x) = x^2
f'(x)|dashed
```

## Máximo relativo

Si $f'(x) > 0$ cuando $x < c$, y $f'(x) < 0$ cuando $x > c$, es decir, la [[Análisis Matemático I/Función|Función]] **crece antes** de $c$, y **decrece después** de $c$, entonces $x = c$ es un [[Extremo relativo|Máximo relativo]] de $y = f(x)$.

Por ejemplo, con $f(x) = - x^2$, tenemos un máximo relativo en $x = 0$.

```desmos-graph
left = -5; right = 5;
top = 5; bottom = -5;
---
f(x) = - x^2
f'(x)|dashed
```
