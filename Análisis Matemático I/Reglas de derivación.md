---
created: 2024-08-15 13:57:36
modified: 2024-08-15 15:32:25
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
\lim_{h \to 0} \left( \frac{f(x + h) - f(x)}{h} + \frac{g(x + h) - g(x)}{h} \right) =
f'(x) + g'(x)
$$

Por ejemplo, con $s(x) = \ln x + x^2$, la [[Derivada]] es $s'(x) = \frac{1}{x} + 2x$.

```desmos-graph
s(x) = \ln x + x^2
s'(x)|dashed
```

## Resta

Dada las [[Análisis Matemático I/Función|Funciones]] $f(x)$ y $g(x)$ **derivables** en $x$, y dada $r(x)$ la [[Análisis Matemático I/Función|Función]] resultante de restar a ambas.

$$
r(x) = f(x) - g(x) \Rightarrow r'(x) = f'(x) - g'(x)
$$

Como podemos ver en la siguiente demostración.

$$
r'(x) =
\left[ f(x) - g(x) \right]' =
\left[ f(x) + (-1) \cdot g(x) \right]'
$$

Como podemos ver, podemos derivar $(-1) \cdot g(x)$ mediante la regla de [[Reglas de derivación#Múltiplo constante|Múltiplo constante]], y continuar derivando mediante la regla de [[Reglas de derivación#Suma|Suma]].

$$
r'(x) =
f'(x) + (-1) \cdot g'(x) =
f'(x) - g'(x)
$$

Por ejemplo, con $r(x) = \ln x - x^2$, la [[Derivada]] es $r'(x) = \frac{1}{x} - 2x$.

```desmos-graph
s(x) = \ln x - x^2
s'(x)|dashed
```

## Producto

Dada las [[Análisis Matemático I/Función|Funciones]] $f(x)$ y $g(x)$ **derivables** en $x$, y dada $p(x)$ la [[Análisis Matemático I/Función|Función]] resultante de su producto.

$$
p(x) = f(x) \cdot g(x) \Rightarrow p'(x) = f'(x) \cdot g(x) + f(x) \cdot g'(x)
$$

Como podemos ver en la siguiente demostración.

$$
p'(x) =
\lim_{h \to 0} \frac{p(x + h) - p(x)}{h} =
\lim_{h \to 0} \frac{f(x + h) \cdot g(x + h) - f(x) \cdot g(x)}{h}
$$

Para continuar resolviendo, **sumamos y restamos** $f(x) \cdot g(x + h)$ dentro del numerador.

$$
p'(x) =
\lim_{h \to 0} \frac{f(x + h) \cdot g(x + h) - f(x) \cdot g(x + h) + f(x) \cdot g(x + h) - f(x) \cdot g(x)}{h} =
\lim_{h \to 0} \left[ \frac{f(x + h) - f(x)}{h} \cdot g(x + h) + f(x) \cdot \frac{g(x + h) - g(x)}{h} \right] =
f'(x) \cdot g(x) + f(x) \cdot g'(x)
$$

> [!important]
> Si fuera necesario calcular la [[Derivada]] de un producto de 3 o más [[Análisis Matemático I/Función|Funciones]].
>
> $$
> \left( f(x) \cdot g(x) \cdot h(x) \right)'
> $$
>
> Podriamos agrupar $p(x) = f(x) \cdot g(x)$ para poder aplicar esta regla.
>
> $$
> \left( p(x) \cdot h(x) \right)'
> $$

Por ejemplo, con $p(x) = e^x \cdot \sin x$, la [[Derivada]] es $p'(x) = e^x \cdot \sin x + e^x \cdot \cos x = e^x \cdot (\sin x + \cos x)$.

```desmos-graph
p(x) = e^x \cdot \sin x
p'(x)|dashed
```

## Inverso multiplicativo

Dada una [[Análisis Matemático I/Función|Función]] $f(x)$ **derivable** en $x$, y dada $i(x)$, su inversa con $f(x) \neq 0$.

$$
i(x) = \frac{1}{f(x)} \Rightarrow i'(x) = - \frac{f'(x)}{f^2(x)}
$$

Como podemos ver en la siguiente demostración.

$$
i'(x) =
\lim_{h \to 0} \frac{i(x + h) - i(x)}{h} =
\lim_{h \to 0} \frac{\frac{1}{f(x + h)} - \frac{1}{f(x)}}{h}
$$

Realizamos un cálculo auxiliar con $\frac{1}{f(x + h)} - \frac{1}{f(x)}$.

$$
\frac{1}{f(x + h)} - \frac{1}{f(x)} =
\frac{f(x) - f(x + h)}{f(x + h) \cdot f(x)} =
- \frac{f(x + h) - f(x)}{f(x + h) \cdot f(x)}
$$

Continuamos calculando el [[Límite]].

$$
i'(x) =
\lim_{h \to 0} \left( - \frac{f(x + h) - f(x)}{f(x + h) \cdot f(x)} \cdot \frac{1}{h} \right) =
\lim_{h \to 0} \left( - \frac{f(x + h) - f(x)}{h} \cdot \frac{1}{f(x + h) \cdot f(x)} \right) =
- f'(x) \cdot \frac{1}{f(x) \cdot f(x)} =
- \frac{f'(x)}{f^2(x)}
$$

Por ejemplo, con $i(x) = \frac{1}{x^2}$, la [[Derivada]] es $i'(x) = \frac{2x}{x^4} = \frac{2}{x^3}$.

```desmos-graph
i(x) = \frac{1}{x^2}
i'(x)|dashed
```

## Cociente

Dada las [[Análisis Matemático I/Función|Funciones]] $f(x)$ y $g(x)$ **derivables** en $x$, y dada $p(x)$ la [[Análisis Matemático I/Función|Función]] resultante de su cociente.

$$
c(x) = \frac{f(x)}{g(x)} \Rightarrow c'(x) = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{g^2(x)}
$$

Como podemos ver en la siguiente demostración.

$$
c'(x) =
\left( f(x) \cdot \frac{1}{g(x)} \right)'
$$

Utilizamos la regla del [[Reglas de derivación#Producto|Producto]].

$$
c'(x) =
f'(x) \cdot \frac{1}{g(x)} + f(x) \cdot \left( \frac{1}{g(x)} \right)'
$$

Utilizamos la regla del [[Reglas de derivación#Inverso multiplicativo|Inverso multiplicativo]].

$$
c'(x) =
\frac{f'(x)}{g(x)} + f(x) \cdot \left( - \frac{1}{g(x)} \right)
$$

Para continuar resolviendo, **sumamos y restamos** $f(x) \cdot g(x + h)$ dentro del numerador.

$$
p'(x) =
\lim_{h \to 0} \frac{f(x + h) \cdot g(x + h) - f(x) \cdot g(x + h) + f(x) \cdot g(x + h) - f(x) \cdot g(x)}{h} =
\lim_{h \to 0} \left[ \frac{f(x + h) - f(x)}{h} \cdot g(x + h) + f(x) \cdot \frac{g(x + h) - g(x)}{h} \right] =
f'(x) \cdot g(x) + f(x) \cdot g'(x)
$$

> [!important]
> Si fuera necesario calcular la [[Derivada]] de un producto de 3 o más [[Análisis Matemático I/Función|Funciones]].
>
> $$
> \left( f(x) \cdot g(x) \cdot h(x) \right)'
> $$
>
> Podriamos agrupar $p(x) = f(x) \cdot g(x)$ para poder aplicar esta regla.
>
> $$
> \left( p(x) \cdot h(x) \right)'
> $$

Por ejemplo, con $p(x) = e^x \cdot \sin x$, la [[Derivada]] es $p'(x) = e^x \cdot \sin x + e^x \cdot \cos x = e^x \cdot (\sin x + \cos x)$.

```desmos-graph
p(x) = e^x \cdot \sin x
p'(x)|dashed
```
