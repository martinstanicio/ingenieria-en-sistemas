---
aliases:
  - Cofactor
---

# Adjunto

Si tenemos una [[Matriz]] $A \in k^{n \times n}$, se llama **adjunto** o **cofactor** *$ij$-ésimo* al número obtenido del producto entre $-1$ elevado a la cantidad de filas más la cantidad de columnas, y el [[Determinante]] del [[Menor complementario]] $ij$:

$$
A_{ij} = (-1)^{i + j} \cdot det(M_{ij})
$$

Por ejemplo, para la siguiente matriz:

$$
A=
\left( 
    \begin{array}{c}
        -1 & 3 & 7 \\
        2 & 6 & 8 \\
        0 & 5 & 3 \\
    \end{array}
\right)
$$

Algunos de los posibles adjuntos son:

- $M_{23} = \left(\begin{array}{c} -1 & 3 \\ 0 & 5 \end{array}\right) \rightarrow A_{23} = (-1)^{2 + 3} \cdot \left|\begin{array}{c} -1 & 3 \\ 0 & 5 \end{array}\right| = (-1)^5 \cdot (-5) = -1(-5) = 5$
- $M_{31} = \left(\begin{array}{c} 3 & 7 \\ 6 & 8 \end{array}\right) \rightarrow A_{31} = (-1)^{3 + 1} \cdot \left|\begin{array}{c} 3 & 7 \\ 6 & 8 \end{array}\right| = (-1)^4 \cdot (-18) = 1(-18) = -18$

Una matriz tiene ==$n^2$ adjuntos posibles==, uno por cada una de sus coordenadas.
