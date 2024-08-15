---
created: 2024-08-15 00:55:43
modified: 2024-08-15 01:45:20
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

Como $t = x$ es raíz del polinomio $t^n - x^n$, luego:

$$
f'(x) =
\lim_{t \to x} \frac{(t - x)(t^{n - 1} + x \cdot t^{n - 2} + \dots + x^{n - 1})}{t - x} =
\lim_{t \to x} (t^{n - 1} + x \cdot t^{n - 2} + \dots + x^{n - 1}) =
x^{n - 1} + x^{n - 1} + \dots + x^{n - 1}
$$

Como nos queda un polinomio de grado $n - 1$, tiene $n$ términos.

$$
f'(x) = n \cdot x^{n - 1}
$$

## Función exponencial de base $e$

La [[Derivada]] de una [[Análisis Matemático I/Función|Función]] exponencial $f(x) = e^x$ **siempre será $e^x$**.

$$
f(x) = e^x \Rightarrow f'(x) = e^x
$$

```desmos-graph
f(x) = e^x
f'(x)|dashed
```

Como podemos ver en la siguiente demostración.

$$
f'(x) =
\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} =
\lim_{h \to 0} \frac{e^{x + h} - e^x}{h} =
\lim_{h \to 0} \frac{e^x (e^h - 1)}{h}
$$

Utilizamos uno de los [[Infinitésimos#Infinitésimos equivalentes notables]], con $h \to 0$, es $e^h - 1 \approx h$.

$$
f'(x) =
\lim_{h \to 0} \frac{e^x \cdot h}{h} =
e^x
$$

## Función logaritmo natural

La [[Derivada]] de la [[Análisis Matemático I/Función|Función]] $f(x) = \ln x$ **siempre será $\frac{1}{x}$**.

$$
f(x) = \ln x \Rightarrow f'(x) = \frac{1}{x}
$$

```desmos-graph
f(x) = \ln x
f'(x)|dashed
```

Como podemos ver en la siguiente demostración.

$$
f'(x) =
\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} =
\lim_{h \to 0} \frac{\ln (x + h) - \ln x}{h} =
\lim_{h \to 0} \left( \frac{1}{h} \cdot \ln \left(\frac{x + h}{x}\right) \right)
$$

Continuamos aplicando **propiedad de logaritmos**.

$$
f'(x) =
\lim_{h \to 0} \ln \left[ \left(\frac{x + h}{x}\right)^\frac{1}{h} \right] =
\lim_{h \to 0} \ln \left[ \left(1 + \frac{h}{x}\right)^\frac{1}{h} \right] =
\lim_{h \to 0} \ln \left\{ \left[ \left(1 + \frac{h}{x}\right)^\frac{x}{h} \right]^\frac{1}{x} \right\}
$$

Como ya sabemos, con $x \to 0$, la expresión $\left(1 + \frac{1}{x}\right)^x$ tiende a 

$$
f'(x) =
\ln e^\frac{1}{x}
$$
