---
created: 2024-04-22 11:45:25
modified: 2024-05-08 01:33:29
title: Operaciones con matrices
---

# Operaciones con matrices

Existen ciertas condiciones para realizar operaciones con [[Matriz|matrices]].

## Suma

Dos matrices solo puede sumarse si ==tienen el mismo tamaño==.

$$
A^{2 \times 3} \land B^{2 \times 3}\Rightarrow A + B \in \mathbb{R}^{2 \times 3}
$$

Cada elemento se suma con el elemento que esté en su misma posición pero en la otra matriz.

$$
A+B=
\left( 
    \begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
    \end{array}
\right)
+
\left( 
    \begin{array}{c}
        7 & 8 & 9 \\
        10 & 11 & 12 \\
    \end{array}
\right)
=
\left( 
    \begin{array}{c}
        8 & 10 & 12 \\
        14 & 16 & 18 \\
    \end{array}
\right)
$$

## Multiplicación por un escalar

Se aplica ==distributiva de la multiplicación entre un escalar y un vector==.

$$
A \in \mathbb{R}^{2 \times 3} \land \alpha \in \mathbb{R}\Rightarrow
\alpha A =
\alpha
\left( 
    \begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
    \end{array}
\right)
=
\left( 
    \begin{array}{c}
        \alpha1 & \alpha2 & \alpha3 \\
        \alpha4 & \alpha5 & \alpha6 \\
    \end{array}
\right)
$$

## Trasposición

Se invierten las filas y columnas.

$$
A\in\mathbb{R}^{2 \times 3} \Rightarrow A^t \in\mathbb{R}^{3 \times 2}
$$

Por ejemplo.

$$
A^t=
\left( 
    \begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
    \end{array}
\right)^t
=
\left( 
    \begin{array}{c}
        1 & 4 \\
        2 & 5 \\
        3 & 6 \\
    \end{array}
\right)
$$

## Producto de matrices

Para que sea posible, ==el número de columnas de la primera, debe ser igual al número de filas de la segunda==. La matriz resultante tendrá la misma cantidad de filas que la primera, y la misma cantidad de columnas que la segunda.

$$
A^{m \times n} \land B^{n \times p}\Rightarrow AB \in \mathbb{R}^{m \times p}
$$

Por ejemplo, para $AB^t$:

$$
AB^t=
\left( 
    \begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
    \end{array}
\right)
\left( 
    \begin{array}{c}
        7 & 8 & 9 \\
        10 & 11 & 12 \\
    \end{array}
\right)^t
=
\left( 
    \begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
    \end{array}
\right)
\left( 
    \begin{array}{c}
        7 & 10 \\
        8 & 11 \\
        9 & 12 \\
    \end{array}
\right)
=
C^{2\times2}
$$

Ahora calculamos cada uno de los 4 elementos de $C$.

- $C_{11} = \left(\begin{array}{c}1 & 2 & 3\end{array}\right) \left(\begin{array}{c}7 \\ 8 \\ 9 \end{array}\right) = 1(7) + 2(8) + 3(9) = 50$
- $C_{21} = \left(\begin{array}{c}4 & 5 & 6\end{array}\right) \left(\begin{array}{c}7 \\ 8 \\ 9 \end{array}\right) = 4(7) + 5(8) + 6(9) = 122$
- $C_{12} = \left(\begin{array}{c}1 & 2 & 3\end{array}\right) \left(\begin{array}{c}10 \\ 11 \\ 12 \end{array}\right) = 1(10) + 2(11) + 3(12) = 68$
- $C_{22} = \left(\begin{array}{c}4 & 5 & 6\end{array}\right) \left(\begin{array}{c}10 \\ 11 \\ 12 \end{array}\right) = 4(10) + 5(11) + 6(12) = 167$

$$
AB^t = C =
\left( 
    \begin{array}{c}
        50 & 68 \\
        122 & 167 \\
    \end{array}
\right)
$$

La multiplicación de matrices ==no es [[Conmutatividad|conmutativa]]==.
