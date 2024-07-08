---
aliases:
  - Vector propio
  - Vector característico
  - Eigenvector
created: 2024-07-07 19:00:40
modified: 2024-07-07 21:20:44
title: Autovector
---

# Autovector

Dada una [[Transformación lineal]] $T: V \rightarrow V$ (es decir, un [[Transformación lineal#Endomorfismo|Endomorfismo]]), siendo $V$ un [[Espacio vectorial]] de ==[[Dimensión]] finita== $n$, si existe $w \in V - \left\{ \overrightarrow{0} \right\}$ tal que:

$$
Aw = \lambda w
$$

Donde:

- $A$ es la [[Matriz]] asociada a $T$
- $\lambda \in k$, un escalar.
- $w$ es un vector diferente al [[Elemento neutro|Vector nulo]] y $w \in \mathbb{C}^n$

Podemos afirmar que $\lambda$ es [[Autovalor]] de $T$, y $w$ es el [[Autovector]] asociado a $\lambda$.

> [!important]
> Para que un vector $w$ sea [[Autovector]], debe pertenecer al [[Autoespacio]], pero ser diferente del [[Elemento neutro|Vector nulo]].
>
> $$
> w \in E_\lambda - \left\{ \overrightarrow{0} \right\}
> $$

## Cálculo de $w$

Igualando la ecuación original al [[Elemento neutro|Vector nulo]], obtenemos lo siguiente.

$$
(A - \lambda I) \overrightarrow{w} = \overrightarrow{0}
$$

Este [[Sistema de ecuaciones lineales homogéneo (SELH)]] deberá ser [[Sistema compatible (SC)#Sistema compatible indeterminado (SCI)]], para que existan ==soluciones diferentes al [[Elemento neutro|Vector nulo]]==. Para esto, forzamos al [[Determinante]] de la [[Matriz#Matriz de coeficientes|Matriz de coeficientes]] a que sea $0$.

$$
|A - \lambda I| = 0
$$
