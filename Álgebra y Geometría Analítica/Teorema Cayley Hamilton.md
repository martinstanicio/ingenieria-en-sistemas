---
created: 2024-07-08 22:24:36
modified: 2024-11-09 16:03:24
title: Teorema Cayley Hamilton
---

# Teorema Cayley Hamilton

Sea $A \in \mathbb{R}^{n \times n}$, luego $A$ satisface su [[Autoecuación|Ecuación característica]].

$$
p(\lambda) = 0 \Rightarrow p(A) = N
$$

Donde $p(\lambda)$ es el [[Autopolinomio|Polinomio característico]], y $N$ es la [[Matriz]] nula.

---

El [[Autopolinomio|Polinomio característico]] tiene la siguiente estructura.

$$
p(\lambda) =
a_n \lambda^n + a_{n - 1} \lambda^{n - 1} + \dots + a_1 \lambda + a_0
$$

No podemos evaluar esta ecuación en $A$ directamente, ya que el [[Término independiente]] es un escalar, y el resto de términos son matrices. Por lo tanto, definimos la siguiente estructura.

$$
P(A) =
a_n A^n + a_{n - 1} A^{n - 1} + \dots + a_1 A + a_0 I
$$

Donde $I \in \mathbb{R}^{n \times n}$ es la [[Matriz identidad]] correspondiente.
