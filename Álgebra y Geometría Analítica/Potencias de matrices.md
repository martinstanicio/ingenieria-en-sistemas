---
created: 2024-11-09 15:55:34
modified: 2024-11-09 16:36:06
title: Potencias de matrices
---

# Potencias de matrices

Existen múltiples métodos para calcular [[Potencias de matrices]], dependiendo del exponente, el tamaño de la [[Matriz]], etc.

## Diagonalización de matrices

Despejando la ecuación obtenida al realizar la [[Diagonalización]] de una matriz, podemos obtener la siguiente fórmula.

$$
A^n = P \cdot D^n \cdot P^{-1}, n \in \mathbb{N}
$$

La diagonal principal de la [[Matriz diagonal]] $D$ está formada por los [[Autovalor|Autovalores]] de $A$, y las columnas de $P$ por sus [[Autovector|Autovectores]].

> [!warning]
> No debemos calcular los [[Autovalor|Autovalores]] y [[Autovector|Autovectores]] de $A^n$, sino simplemente de $A$.

Luego, podemos calcular fácilmente la potencia de una [[Matriz diagonal]], de la siguiente forma.

$$
\begin{pmatrix}
    a & 0 & 0 \\
    0 & b & 0 \\
    0 & 0 & c \\
\end{pmatrix}^n
=
\begin{pmatrix}
    a^n & 0 & 0 \\
    0 & b^n & 0 \\
    0 & 0 & c^n \\
\end{pmatrix}
$$

## Teorema Cayley Hamilton

Para calcular potencias de una [[Matriz]] $A$, el [[Teorema Cayley Hamilton]] nos permite representar $A^n$ como una [[Combinación lineal]] de la [[Matriz]] original $A$ y la [[Matriz identidad]].

Si tomamos el [[Autopolinomio|Polinomio característico]] $p(\lambda)$ y lo evaluamos en $A$, luego podemos despejar el término de mayor grado.

$$
p(A) = N
\Leftrightarrow
A^2 - 4A - 5I = N
\Leftrightarrow
A^2 = 4A + 5I
$$

Luego podemos multiplicar ambos lados de la igualdad por $A$, hasta llegar al exponente deseado.

$$
A^2 = 4A + 5I
\Leftrightarrow
A^3 = 4A^2 + 5A
$$

Y como ya despejamos $A^2$, podemos reemplazar su valor en la ecuación, dejando siempre una [[Combinación lineal]] de la forma $A^n = \alpha A + \beta I$.

$$
A^3 = 4(4A + 5I) + 5A
\Leftrightarrow
A^3 = 21A + 20I
$$

Sin embargo, existe una forma de evitar este proceso repetitivo. Por el [[Teorema Cayley Hamilton]] sabemos que, si $A$ satisface la [[Autoecuación|Ecuación característica]], también lo hace $\lambda$.

$$
A^n = \alpha A + \beta I
\Leftrightarrow
\lambda^n = \alpha \lambda + \beta
$$

Esto nos permite obtener los **coeficientes** $\alpha$ y $\beta$, pudiendo reemplazar directamente en la primera ecuación para obtener $A^n$.
