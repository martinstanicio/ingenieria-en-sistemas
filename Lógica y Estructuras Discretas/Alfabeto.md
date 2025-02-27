---
created: 2025-02-27 18:42:06
modified: 2025-02-27 19:48:16
title: Alfabeto
---

# Alfabeto

Es un [[Conjunto]] $\Sigma \neq \emptyset$ cuyos elementos se llaman **letras** o **símbolos**.

> [!important]
> Ningún símbolo puede comenzar con otro símbolo del [[Alfabeto]].

Se utilizan para formar una [[Lógica y Estructuras Discretas/Cadena|Cadena de símbolos]] o simplemente [[Lógica y Estructuras Discretas/Cadena|Cadena]].

## Potencia de $\Sigma$

Sea $n \in \mathbb{N}$:

$$
\Sigma^n = \left\{
    \begin{array}{c}
        \Sigma \space \text{si} \space n = 1 \\
        \left\{ xy: x \in \Sigma \wedge y \in \Sigma^{n - 1} \right\} \space \text{si} \space n > 1 \\
    \end{array} 
\right.
$$

> [!tip]
> $xy$ es una ==concatenación== o ==yuxtaposición== de $x$ e $y$.
