---
aliases:
  - Forma normal
created: 2024-08-13 17:07:52
modified: 2024-08-13 17:51:25
title: Forma canónica
---

# Forma canónica

Se dice que una [[Análisis Matemático I/Función|Función]] booleana $F$ de $n$ variables está representada en su ==forma canónica==, si en cada **término** o **factor** se encuentran **todas las variables una única vez**, en su forma simple o [[Complemento|Complementada]].

$$
F(A, B, C) = A \cdot B \cdot \overline{C} + \overline{A} \cdot \overline{B} \cdot C
$$

<iframe width="560" height="315" src="https://www.youtube.com/embed/3ZTbrJzUpcc?si=KGY9BUh3rs2QJdY7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Existen dos [[Forma canónica|Formas canónicas]] posibles. Para la siguiente [[Tabla de verdades]], por ejemplo:

| A   | B   | C   | F   |               |
| --- | --- | --- | --- | ------------- |
| 0   | 0   | 0   | 0   | $m_0$ o $M_0$ |
| 0   | 0   | 1   | 0   | $m_1$ o $M_1$ |
| 0   | 1   | 0   | 0   | $m_2$ o $M_2$ |
| 0   | 1   | 1   | 1   | $m_3$ o $M_3$ |
| 1   | 0   | 0   | 0   | $m_4$ o $M_4$ |
| 1   | 0   | 1   | 1   | $m_5$ o $M_5$ |
| 1   | 1   | 0   | 1   | $m_6$ o $M_6$ |
| 1   | 1   | 1   | 1   | $m_7$ o $M_7$ |

## Forma Canónica Disyuntiva (FCD)

Cuando la [[Forma canónica]] está formada por [[Minitérmino (m)|Minitérminos]] (**suma de productos**).

> [!tip]
> Para obtenerla, nos fijamos para qué valores de las variables, la [[Salidas|Salida]] de la [[Análisis Matemático I/Función|Función]] es **verdadera** o $1$.

Por ejemplo, para la [[Tabla de verdades]] dada:

$$
F(A, B, C) = \overline{A} B C + A \overline{B} C + A B \overline{C} + ABC
$$

También puede ser expresada como una **sumatoria** de [[Minitérmino (m)|Minitérminos]], donde indicamos las filas donde la [[Análisis Matemático I/Función|Función]] es verdadera.

$$
F(A, B, C) = \sum{m(3, 5, 6, 7)}
$$

## Forma Canónica Conjunta (FCC)

Cuando la [[Forma canónica]] está formada por [[Maxitérmino (M)|Maxitérminos]] (**producto de sumas**).

> [!tip]
> Para obtenerla, nos fijamos para qué valores de las variables, la [[Salidas|Salida]] de la [[Análisis Matemático I/Función|Función]] es **falsa** o $0$.

Por ejemplo, para la [[Tabla de verdades]] dada:

$$
F(A, B, C) =
\left(A + B + C\right)
\left(A + B + \overline{C}\right)
\left(A + \overline{B} + C\right)
\left(\overline{A} + B + C\right)
$$

También puede ser expresada como una **productoria** de [[Maxitérmino (M)|Maxitérminos]], donde indicamos las filas donde la [[Análisis Matemático I/Función|Función]] es falsa.

$$
F(A, B, C) = \prod{M(0, 1, 2, 4)}
$$
