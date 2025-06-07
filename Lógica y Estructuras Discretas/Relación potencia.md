---
created: 2025-06-07 16:29:52
modified: 2025-06-07 16:33:35
title: Relación potencia
---

# Relación potencia

Una [[Relación]] $R: A \to A$ es una [[Relación potencia]] si se cumple lo siguiente.

$$
R^n =
\left\{
    \begin{array}{r}
        id_A \space \text{si} \space n = 0 \\
        R \circ R^{n - 1} \space \text{si} \space n > 0 \\
    \end{array}
\right.
$$

> [!note]
> $R \circ R^{n - 1}$ es una [[Relación de composición]].
