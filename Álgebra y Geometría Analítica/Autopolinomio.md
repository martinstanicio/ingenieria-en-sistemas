---
aliases:
  - Polinomio propio
  - Polinomio característico
  - Eigenpolinomio
created: 2024-07-07 20:08:09
modified: 2024-08-07 13:40:34
title: Autopolinomio
---

# Autopolinomio

Para obtener los [[Autovector|Autovectores]] o [[Autovalor|Autovalores]] asociados a una [[Transformación lineal]] con [[Matriz]] asociada $A$, deberemos calcular un [[Determinante]] para asegurarnos que el [[Sistema de ecuaciones lineales homogéneo (SELH)|SELH]] sea [[Sistema compatible (SC)#Sistema compatible indeterminado (SCI)|SCI]].

$$
|A - \lambda I| = p(\lambda)
$$

Obtendremos un polinomio $p(\lambda)$, llamado ==autopolinomio==, ==polinomio propio==, ==polinomio característico== o ==eigenpolinomio==.

> [!note]
> El [[Término independiente]] del [[Autovector#Polinomio característico|Polinomio característico]] siempre es $|A|$, pues al evaluar la expresión en $\lambda = 0$, obtenemos que $p(0) = |A - 0I| = |A|$.

Si $\lambda = 0$ es [[Autovalor|Valor propio]], entonces $|A| = 0$. Por lo tanto, $A$ no es [[Matriz inversible]].

> [!tip]
> Si evalúo al [[Autopolinomio|Polinomio característico]] $p(\lambda)$ en la [[Matriz]] original $A$, entonces $p(A) = N$, donde $N$ es la [[Matriz]] nula.
