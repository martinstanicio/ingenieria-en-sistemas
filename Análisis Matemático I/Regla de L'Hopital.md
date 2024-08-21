---
created: 2024-08-21 00:32:39
modified: 2024-08-21 01:32:53
title: "Regla de L'Hopital"
---

# Regla de L'Hopital

Dadas dos [[Análisis Matemático I/Función|Funciones]] $y = f(x)$ y $y = g(x)$, [[Derivada|Derivables]] en un **intervalo abierto** $(a, b)$. Si existe un punto $c \in (a, b)$, tal que $\forall x \in (a, b) - \set{c}: g'(x) \neq 0$ y $f(c) = g(c) = 0$, y existe $\lim_{x \to c} \frac{f'(x)}{g'(x)}$.

$$
\exists c \in (a, b): \left(
    \left(
        \forall x \in (a, b) - \set{c}: g'(x) \neq 0
    \right) \land
    \left(
        f(c) = g(c) = 0
    \right) \land
    \exists \lim_{x \to c} \frac{f'(x)}{g'(x)}
\right)
$$

Entonces, podemos afirmar que existe $\lim_{x \to c} \frac{f(x)}{g(x)}$, y además, $\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$.

$$
\left(
    \exists \lim_{x \to c} \frac{f(x)}{g(x)}
\right) \land
\left(
    \lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}
\right)
$$

> [!tip]
> En la práctica, cuando encontramos una [[Indeterminación]] de tipo $\frac{0}{0}$ o $\frac{\infty}{\infty}$ en un [[Límite]], la [[Regla de L'Hopital]] nos permite [[Derivada|Derivar]] numerador y denominador, y continuar resolviendo.

## Caso $0 \cdot \infty$

Si al calcular un [[Límite]] nos encontramos una [[Indeterminación]] de tipo $0 \cdot \infty$, podemos utilizar la siguiente igualdad.

$$
\lim_{x \to c} f(x) \cdot g(x) =
\lim_{x \to c} \frac{f(x)}{\frac{1}{g(x)}} =
\lim_{x \to c} \frac{g(x)}{\frac{1}{f(x)}}
$$

De esta forma, llegamos a una [[Indeterminación]] de tipo $\frac{0}{0}$ o $\frac{\infty}{\infty}$, por lo que podemos **intentar** aplicar la [[Regla de L'Hopital]].

## Casos $1^\infty$, $0^0$ y $\infty^0$

En estos casos, deberemos recurrir a la [[Derivación logarítmica]] para llegar a una expresión de la siguiente forma.

$$
\lim_{x \to c} g(x) \cdot \ln(f(x)) = \ln(L)
$$

Para continuar resolviendo, podemos seguir los pasos del [[Regla de L'Hopital#Caso $0 cdot infty$|Caso anterior]] $0 \cdot \infty$ hasta poder **intentar** aplicar la [[Regla de L'Hopital]].
