---
aliases:
  - Autovectores
created: 2024-07-01 19:22:44
modified: 2024-07-01 20:06:55
title: Autovalores
---

# Autovalores

Dada una [[Transformación lineal]] $T: V \rightarrow V$ (es decir, un [[Transformación lineal#Endomorfismo]]), siendo $V$ un [[Espacio vectorial]] de [[Dimensión]] finita, si existe $w \in V - \left\{ \overrightarrow{0} \right\}$ tal que $Aw = \lambda w$ siendo $A$ la [[Matriz]] asociada a $T$ y $\lambda \in k$, $w$ es autovector.

$$
Aw = \lambda w
\Leftrightarrow
(A - \lambda I) \overrightarrow{w} = \overrightarrow{0}
$$

Este [[Sistema de ecuaciones lineales homogéneo (SELH)]] deberá ser [[Sistema incompatible (SI)]], para que existan soluciones diferentes al [[Elemento neutro|Vector nulo]]. Para esto, forzamos al [[Determinante]] a que sea $0$.

$$
|A - \lambda I| = 0
$$

> [!note]
> Un autovector también puede ser llamado **vector propio**, **vector característico** o **eigenvector**.

$$
|A - \lambda I| = \text{p}(\lambda)
$$

Este polinomio recibe el nombre de ==polinomio característico==.

$$
\text{p}(\lambda) = 0
$$

Y esta ecuación recibe el nombre de ==ecuación característica==.

Si calculo el valor numérico de $\text{p}(\lambda)$ con $\lambda = 0$, obtengo el término independiente de $\text{p}(\lambda)$. Calculando $\text{p}(0) = |A|$.

Si $\lambda = 0$ (o sea, es valor propio) entonces $|A| = 0 \therefore \nexists A^-1$.
