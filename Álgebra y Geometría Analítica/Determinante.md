---
created: 2024-04-28 19:14:54
modified: 2024-05-08 01:33:29
title: Determinante
---

# Determinante

Es una [[Análisis Matemático I/Función]] por partes, recursiva, que ==asocia a cada [[Matriz]] **cuadrada** un número==, que nos permite trabajar de una forma más sencilla. Toda matriz tiene ==como máximo un único determinante==, pero multiples matrices pueden compartir el mismo.

El determinante ==siempre será parte del mismo [[Cuerpo]]== que los elementos de la matriz, es decir $det: k^{n \times n} \rightarrow k$. Por ejemplo, en una matriz $\mathbb{R}^{n \times n}$, el determinante será de $\mathbb{R}$.

Es una función ==por partes==, ya que la función se define de forma diferente para distintos valores del dominio, dependiendo del tamaño de la matriz.

## Casos bases

Son aquellos casos en los que el determinante se calcula siguiendo una cantidad de pasos bien definida.

### Determinante de una matriz $1\times1$

Si $n = 1$, $A \in k^{n \times n}$, el determinante de dicha matriz siempre será ese único elemento. Por ejemplo:

$$
A = (-7), det(A) = a_{11} = -7
$$

### Determinante de una matriz $2\times2$

Si $n = 2$, $A \in k^{n \times n}$, el determinante de dicha matriz será la diferencia entre la multiplicación de los elementos de la diagonal principal, y la multiplicación de los elementos de la diagonal secundaria. Por ejemplo:

$$
A=
\left( 
    \begin{array}{c}
        7 & -1 \\
        2 & 3 \\
    \end{array}
\right),
det(A) = a_{11} \cdot a_{22} - a_{21} \cdot a_{12} = 7 \cdot 3 - (-1 \cdot 2) = 23
$$

## Caso recursivo

Si $n\geq3$, $A \in k^{n \times n}$, el determinante de dicha matriz será la suma de los productos entre las coordenadas de ==una fila o columna y su respectivo adjunto==.

El [[Teorema de Laplace]] nos demuestra que podemos realizar este cálculo utilizando cualquier fila o columna.

![[Teorema de Laplace]]

### Ejemplo

$$
A=
\left( 
    \begin{array}{c}
        1 & -4 & 2 \\
        -2 & 8 & -9 \\
        -1 & 7 & 0 \\
    \end{array}
\right)
$$

Primero calculamos los tres [[Adjunto|adjuntos]] de los elementos de, por ejemplo, la primera fila.

- $M_{11} = \left(\begin{array}{c} 8 & -9 \\ 7 & 0 \end{array}\right) \rightarrow A_{11} = (-1)^{1 + 1} \cdot \left|\begin{array}{c} 8 & -9 \\ 7 & 0 \end{array}\right| = (-1)^2 \cdot 63 = 63$
- $M_{12} = \left(\begin{array}{c} -2 & -9 \\ -1 & 0 \end{array}\right) \rightarrow A_{12} = (-1)^{1 + 2} \cdot \left|\begin{array}{c} -2 & -9 \\ -1 & 0 \end{array}\right| = (-1)^3 \cdot (-9) = 9$
- $M_{13} = \left(\begin{array}{c} -2 & 8 \\ -1 & 7 \end{array}\right) \rightarrow A_{13} = (-1)^{1 + 3} \cdot \left|\begin{array}{c} -2 & 8 \\ -1 & 7 \end{array}\right| = (-1)^4 \cdot (-6) = -6$

Calculamos el determinante.

$$
det(A) = a_{11} \cdot A_{11} + a_{12} \cdot A_{12} + a_{13} \cdot A_{13} = 1 \cdot 63 + (-4) \cdot 9 + 2 \cdot (-6) = 63 - 36 - 12 = 15
$$
