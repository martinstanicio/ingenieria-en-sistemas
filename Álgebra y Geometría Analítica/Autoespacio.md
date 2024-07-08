---
aliases:
  - Espacio propio
  - Espacio característico
  - Eigenespacio
created: 2024-07-07 20:08:09
modified: 2024-07-07 20:34:57
title: Autoespacio
---

# Autoespacio

Para obtener los [[Autovector|Autovectores]] o [[Autovalor|Autovalores]] asociados a una [[Transformación lineal]] con [[Matriz]] asociada $A \in k^{n \times n}$, igualamos la ecuación original $Aw = \lambda w$ a $0$ para obtener un [[Sistema de ecuaciones lineales homogéneo (SELH)|SELH]].

$$
(A - \lambda I) \overrightarrow{w} = \overrightarrow{0}
$$

Por lo tanto, para obtener la solución debemos calcular el [[Kernel]] de la [[Matriz#Matriz de coeficientes|Matriz de coeficientes]] $(A - \lambda I)$. Este [[Subespacio vectorial]] $E_\lambda$ recibe el nombre de ==autoespacio==, ==espacio propio==, ==espacio característico== o ==eigenespacio==.

$$
E_\lambda =
\ker(A - \lambda I) =
\left\{ w \in k^n: (A - \lambda I)w = \overrightarrow{0} \right\}
$$

> [!tip]
> Dada $A \in k^{n \times n}$, sabemos que $E_\lambda = \ker(A - \lambda I) \subseteq k^n$.
