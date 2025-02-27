---
created: 2025-02-27 20:05:08
modified: 2025-02-27 20:05:29
title: Potencia de un alfabeto
---
# Potencia de un alfabeto

Sea $n \in \mathbb{N}$ y un [[Alfabeto]] $\Sigma$:

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
