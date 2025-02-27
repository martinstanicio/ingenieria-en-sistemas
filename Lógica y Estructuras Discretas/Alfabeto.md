---
created: 2025-02-27 18:42:06
modified: 2025-02-27 18:58:34
title: Alfabeto
---

# Alfabeto

Es un [[Conjunto]] $\Sigma \neq \emptyset$ cuyos elementos se llaman **letras** o **símbolos**.

> [!important]
> Ningún símbolo puede comenzar con otro símbolo del [[Alfabeto]].

Se utilizan para formar ==cadenas de símbolos== o simplemente [[Cadena|Cadenas]].

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

Si $w \in \Sigma^k$, con $k \geq 1$, entonces $w$ se llama una [[Cadena]] de $k$ símbolos de $\Sigma$.

> [!note]
> Dado un [[Alfabeto]] $\Sigma$, se define $\Sigma^0 = \left\{ \lambda \right\}$, donde $\lambda$ representa a la ==[[Cadena]] vacía==, de forma que $\lambda 