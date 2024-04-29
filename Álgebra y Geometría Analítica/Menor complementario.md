# Menor complementario

Sea $A \in k^{n \times n}$, se llama menor *$ij$-ésimo* a la [[Matriz]] $M_{ij} \in k^{n-1 \times n-1}$ que resulta de ==eliminar la fila $i$ y la columna $j$== de $A$. Por ejemplo, para la siguiente matriz:

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

Algunos de los posibles menor complementarios son:

- $M_{23} = \left(\begin{array}{c} -1 & 3 \\ 0 & 5 \end{array}\right)$
- $M_{31} = \left(\begin{array}{c} 3 & 7 \\ 6 & 8 \end{array}\right)$

Una matriz tiene ==$n^2$ menores complementarios posibles==, uno por cada una de sus coordenadas.
