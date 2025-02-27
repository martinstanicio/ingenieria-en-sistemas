---
created: 2025-02-27 19:07:14
modified: 2025-02-27 19:11:38
title: Longitud de una cadena
---
# Longitud de una cadena

Sea $w$ una [[Cadena]] de símbolos del [[Alfabeto]] $\Sigma$.

$$
\text{long}(w) =
\Vert w \Vert =
\left\{
    \begin{array}{c}
        0 \space \text{si} \space w = \lambda \\
        1 + \text{long}(w') \space \text{si} \space w = aw' \wedge a \in \Sigma \wedge w' \space \text{una cadena}
    \end{array}
\right.
$$
