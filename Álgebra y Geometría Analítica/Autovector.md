---
aliases:
  - Vector propio
  - Vector característico
  - Eigenvector
created: 2024-07-07 19:00:40
modified: 2024-07-07 19:33:32
title: Autovector
---

# Autovector

Dada una [[Transformación lineal]] $T: V \rightarrow V$ (es decir, un [[Transformación lineal#Endomorfismo|Endomorfismo]]), siendo $V$ un [[Espacio vectorial]] de ==[[Dimensión]] finita==, si existe $w \in V - \left\{ \overrightarrow{0} \right\}$ tal que:

$$
Aw = \lambda w
$$

Donde:

- $A$ es la [[Matriz]] asociada a $T$
- $\lambda \in k$, un escalar.

Podemos afirmar que $\lambda$ es [[Autovalor]] de $T$, y $w$ es el [[Autovector]] asociado a $\lambda$.

## Cálculo de $w$

Igualando la ecuación original al [[Elemento neutro|Vector nulo]], obtenemos lo siguiente.

$$
(A - \lambda I) \overrightarrow{w} = \overrightarrow{0}
$$

Este [[Sistema de ecuaciones lineales homogéneo (SELH)]] deberá ser [[Sistema incompatible (SI)]], para que existan ==soluciones diferentes al [[Elemento neutro|Vector nulo]]==. Para esto, forzamos al [[Determinante]] de la [[Matriz#Matriz de coeficientes|Matriz de coeficientes]] a que sea $0$.

$$
|A - \lambda I| = 0
$$

## Polinomio característico

Al calcular dicho [[Determinante]], obtendremos un polinomio $p(\lambda)$, llamado ==polinomio característico==.

$$
|A - \lambda I| = p(\lambda)
$$

> [!note]
> El [[Término independiente]] del [[Autovector#Polinomio característico|Polinomio característico]] siempre es $|A|$, pues al evaluar la expresión en $\lambda = 0$, obtenemos que $p(0) = |A|$.

Si $\lambda = 0$ es [[Autovalor|Valor propio]], entonces $|A| = 0$. En este caso, $A$ no es [[Matriz inversible]], es decir, $\nexists A^{-1}$.

## Ecuación característica

Si igualamos al [[Autovector#Polinomio característico]] a $0$, obtenemos la ==ecuación característica==.

$$
p(\lambda) = 0
$$
