# Representación matricial
Son una forma más concisa de escribir un [[Sistema de ecuaciones lineales (SEL)]].

## Vector de incógnitas
$$
X=
\left( 
    \begin{array}{c}
        x_1 \\
        x_2 \\
        \vdots \\
        x_n
    \end{array} 
\right)^{n\times1}
$$

## Vector de términos independientes
$$
B=
\left( 
    \begin{array}{c}
        b_1 \\
        b_2 \\
        \vdots \\
        b_m
    \end{array}
\right)^{m\times1}
$$

## Matriz de coeficientes
$$
A=
\left( 
    \begin{array}{c}
        a_{11} & a_{12} & \dots & a_{1n} \\
        a_{21} & a_{22} & \dots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \dots & a_{mn} \\
    \end{array}
\right)^{m\times n}
$$

## Expresión matricial del sistema
$$
\begin{align}
AX &= B \\
\left(
    \begin{array}{c}
        a_{11} & a_{12} & \dots & a_{1n} \\
        a_{21} & a_{22} & \dots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \dots & a_{mn} \\
    \end{array}
\right)
\left(
    \begin{array}{c}
        x_1 \\
        x_2 \\
        \vdots \\
        x_n
    \end{array} 
\right)
&=
\left( 
    \begin{array}{c}
        b_1 \\
        b_2 \\
        \vdots \\
        b_m
    \end{array}
\right)
\end{align}
$$

## Matriz ampliada
$$
Ab=
\left( 
    \begin{array}{c}
        a_{11} & a_{12} & \dots & a_{1n} & b_1 \\
        a_{21} & a_{22} & \dots & a_{2n} & b_2 \\
        \vdots & \vdots & \ddots & \vdots & \vdots \\
        a_{m1} & a_{m2} & \dots & a_{mn} & b_m \\
    \end{array}
\right)^{m\times (n+1)}
$$