---
created: 2024-11-11 17:47:30
modified: 2024-11-13 19:49:13
title: Proyección
---

# Proyección

Sea $V$ un [[Espacio Vectorial con Producto Interno]], $W$ un [[Subespacio vectorial]] de $V$, $B = \set{w_1, \dots, w_n}$ una [[Base]] de $W$, y un vector $u \in V \land u \notin W$.

$$
\exists \hat{y} \in W,
\exists z \in W^\bot:
u = \hat{y} + z
$$

> [!note]
> Dado un vector $u$ cualquiera, el mismo se puede descomponer en un vector que pertenece al [[Subespacio vectorial|Subespacio]] deseado $W$, llamado [[Proyección]] $\hat{y}$; y otro que pertenece a su [[Complemento ortogonal]] $W^\bot$, llamado $z$.

$$
\text{proy}_w u =
\frac{\left< u, w \right>}{\left< w, w \right>} w
$$
