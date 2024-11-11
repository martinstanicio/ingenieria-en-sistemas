---
created: 2024-11-11 17:57:49
modified: 2024-11-11 18:01:47
title: Teorema de descomposición espectral
---

# Teorema de descomposición espectral

Al momento de calcular una [[Proyección]], si la [[Base]] mencionada $B$ es una [[Base ortogonal]], sabemos lo siguiente.

$$
\hat{y} = \alpha_1 w_1 + \dots + \alpha_n w_n
$$

Como es una [[Base ortogonal]], también sabemos lo siguiente.

![[Base ortogonal#^51769b]]

Por lo tanto, podemos calcular $\hat{y}$ utilizando estos datos.

$$
\hat{y} =
\text{proy}_{w_1} u + \dots + \text{proy}_{w_n} u =
\frac{\left< u, w_1 \right>}{\left< w_1, w_1 \right>} w_1 + \dots + \frac{\left< u, w_n \right>}{\left< w_n, w_n \right>}
$$
