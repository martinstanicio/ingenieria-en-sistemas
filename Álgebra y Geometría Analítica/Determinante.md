# Determinante

Es una [[Función]] por partes, recursiva, que ==asocia a cada [[Matriz]] **cuadrada** un número==, que nos permite trabajar de una forma más sencilla. Toda matriz tiene ==como máximo un único determinante==, pero multiples matrices pueden compartir el mismo.

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

Si $n\geq3$, $A \in k^{n \times n}$

El determinante de una matriz de $2\times2$ será la diferencia entre la multiplicación de los elementos de la diagonal principal, y la multiplicación de los elementos de la diagonal secundaria. Por ejemplo:

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
