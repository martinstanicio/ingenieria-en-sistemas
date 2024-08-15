---
created: 2024-08-15 00:55:43
modified: 2024-08-15 02:31:20
title: Derivada de funciones elementales
---

# Derivada de funciones elementales

Calculo de la [[Derivada]] de [[Análisis Matemático I/Función|Funciones]] **elementales**.

| $f$                     | $f'$                   |
| ----------------------- | ---------------------- |
| $k$                     | $0$                    |
| $x^n, n \in \mathbb{N}$ | $n \cdot x^{n - 1}$    |
| $e^x$                   | $e^x$                  |
| $\ln x$                 | $\frac{1}{x}$          |
| $\sin x$                | $\cos x$               |
| $\cos x$                | $- \sin x$             |
| $\frac{1}{x}$           | $- \frac{1}{x^2}$      |
| $\sqrt{x}$              | $\frac{1}{2 \sqrt{x}}$ |

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

Como ya sabemos, con $x \to 0$, la expresión $\left(1 + \frac{1}{x}\right)^x$ tiende a $e$.

$$
f'(x) =
\ln e^\frac{1}{x} =
\frac{1}{x}
$$

## Función seno

La [[Derivada]] de la [[Análisis Matemático I/Función|Función]] $f(x) = \sin x$ **siempre será $\cos x$**.

$$
f(x) = \sin x \Rightarrow f'(x) = \cos x
$$

```desmos-graph
f(x) = \sin x
f'(x)|dashed
```

Como podemos ver en la siguiente demostración.

$$
f'(x) =
\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} =
\lim_{h \to 0} \frac{\sin (x + h) - \sin x}{h}
$$

Aplicamos la propiedad que nos da el resultado del **seno de una suma**: $\sin (x + h) = \sin x \cdot \cos h + \cos x \cdot \sin h$.

$$
f'(x) =
\lim_{h \to 0} \frac{\sin x \cdot \cos h + \cos x \cdot \sin h - \sin x}{h} =
\lim_{h \to 0} \frac{\sin x \left(\cos h - 1 \right) + \cos x \cdot \sin h}{h} =
\lim_{h \to 0} \left( \frac{\sin x \left(\cos h - 1 \right)}{h} + \frac{\cos x \cdot \sin h}{h} \right)
$$

Utilizamos uno de los [[Infinitésimos#Infinitésimos equivalentes notables]], con $h \to 0$, es $\sin h \approx h$.

$$
f'(x) =
\lim_{h \to 0} \left( \frac{\sin x \left(\cos h - 1 \right)}{h} + \frac{\cos x \cdot h}{h} \right) =
\lim_{h \to 0} \left( \sin x \cdot \frac{\cos h - 1}{h} + \cos x \right)
$$

Analizamos el factor $\frac{\cos h - 1}{h}$ por separado.

$$
\frac{\cos h - 1}{h} =
\frac{\cos h - 1}{h} \cdot \frac{\cos h + 1}{\cos h + 1} =
\frac{\cos^2 h - 1}{h(\cos h + 1)} =
\frac{- \sin^2 h}{h(\cos h + 1)} =
\frac{- \sin h \cdot \sin h}{h(\cos h + 1)}
$$

Continuamos calculando el [[Límite]].

$$
f'(x) =
\lim_{h \to 0} \left( \sin x \cdot \frac{- \sin h \cdot \sin h}{h(\cos h + 1)} + \cos x \right)
$$

Utilizamos el mismo [[Infinitésimos#Infinitésimos equivalentes $f(x) approx g(x)$|Infinitésimo equivalente]] mencionado previamente: $\sin h \approx h$.

$$
f'(x) =
\lim_{h \to 0} \left( \sin x \cdot \frac{- h \cdot \sin h}{h(\cos h + 1)} + \cos x \right) =
\lim_{h \to 0} \left( \sin x \cdot \frac{- \sin h}{\cos h + 1} + \cos x \right) =
\sin x \cdot \frac{0}{2} + \cos x =
\cos x
$$

## Función coseno

La [[Derivada]] de la [[Análisis Matemático I/Función|Función]] $f(x) = \cos x$ **siempre será $- \sin x$**.

$$
f(x) = \cos x \Rightarrow f'(x) = - \sin x
$$

```desmos-graph
f(x) = \cos x
f'(x)|dashed
```

Como podemos ver en la siguiente demostración.

$$
f'(x) =
\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} =
\lim_{h \to 0} \frac{\cos (x + h) - \cos x}{h}
$$

Aplicamos la propiedad que nos da el resultado del **coseno de una suma**: $\cos (x + h) = \cos x \cdot \cos h - \sin x \cdot \sin h$.

$$
f'(x) =
\lim_{h \to 0} \frac{\cos x \cdot \cos h - \sin x \cdot \sin h - \cos x}{h} =
\lim_{h \to 0} \frac{\cos x (\cos h - 1) - \sin x \cdot \sin h}{h} =
\lim_{h \to 0} \left( \cos x \cdot \frac{\cos h - 1}{h} - \frac{\sin x \cdot \sin h}{h} \right)
$$

Utilizamos uno de los [[Infinitésimos#Infinitésimos equivalentes notables]], con $h \to 0$, es $\sin h \approx h$.

$$
f'(x) =
\lim_{h \to 0} \left( \cos x \cdot \frac{\cos h - 1}{h} - \frac{\sin x \cdot h}{h} \right) =
\lim_{h \to 0} \left( \cos x \cdot \frac{\cos h - 1}{h} - \sin x \right)
$$

Analizamos el factor $\frac{\cos h - 1}{h}$ por separado.

$$
\frac{\cos h - 1}{h} =
\frac{\cos h - 1}{h} \cdot \frac{\cos h + 1}{\cos h + 1} =
\frac{\cos^2 h - 1}{h(\cos h + 1)} =
\frac{- \sin^2 h}{h(\cos h + 1)} =
\frac{- \sin h \cdot \sin h}{h(\cos h + 1)}
$$

Continuamos calculando el [[Límite]].

$$
f'(x) =
\lim_{h \to 0} \left( \cos x \cdot \frac{- \sin h \cdot \sin h}{h(\cos h + 1)} - \sin x \right)
$$

Utilizamos el mismo [[Infinitésimos#Infinitésimos equivalentes $f(x) approx g(x)$|Infinitésimo equivalente]] mencionado previamente: $\sin h \approx h$.

$$
f'(x) =
\lim_{h \to 0} \left( \cos x \cdot \frac{- h \cdot \sin h}{h(\cos h + 1)} - \sin x \right) =
\lim_{h \to 0} \left( \cos x \cdot \frac{- \sin h}{\cos h + 1} - \sin x \right) =
\cos x \cdot \frac{0}{2} - \sin x =
- \sin x
$$
