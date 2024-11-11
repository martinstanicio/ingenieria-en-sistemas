---
aliases:
  - Producto interior usual
created: 2024-11-11 13:27:41
modified: 2024-11-11 13:43:04
title: Producto interno usual
---

# Producto interno usual

La definición del [[Producto interno]] cuando no está especificado.

## Espacio real

Dado $V$ un [[Espacio vectorial]] de forma $V = \mathbb{R}^n$, y los vectores $\forall x, y \in V$.

$$
x = \left( x_1, \dots, x_n \right) \land
y = \left( y_1, \dots, y_n \right) \Rightarrow
\left< x, y \right> =
x_1 \cdot y_1 + \dots + x_n \cdot y_n
$$

## Espacio complejo

Dado $V$ un [[Espacio vectorial]] de forma $V = \mathbb{C}^n$, y los vectores $\forall x, y \in V$.

$$
x = \left( x_1, \dots, x_n \right) \land
y = \left( y_1, \dots, y_n \right) \Rightarrow
\left< x, y \right> =
x_1 \cdot \overline{y_1} + \dots + x_n \cdot \overline{y_n}
$$

## Producto interno de funciones

Dado $V$ un [[Espacio vectorial]] de forma $V = F: [a, b] \to \mathbb{R}$, el [[Conjunto]] de las [[Análisis Matemático I/Función|Funciones]] [[Continuidad|Continuas]] en el intervalo $[ a, b ]$, y las [[Análisis Matemático I/Función|Funciones]] $f = f(x)$ y $g = g(x)$.

$$
\left< f, g \right> =
\int_a^b f(x) \cdot g(x) \cdot dx
$$

Debemos calcular la [[Integral]] del producto de las [[Análisis Matemático I/Función|Funciones]].

## Producto interno de matrices

Dado $V$ un [[Espacio vectorial]] de forma $V = \mathbb{R}^{m \times n}$, y las matrices $\forall A, B \in \mathbb{R}^{m \times n}$.

$$
\left< A, B \right> =
tr \left( A \cdot B^t \right)
$$

Debemos calcular la [[Traza]].
