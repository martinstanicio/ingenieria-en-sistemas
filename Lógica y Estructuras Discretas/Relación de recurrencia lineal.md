---
created: 2024-07-28 11:16:22
modified: 2024-07-28 11:36:31
title: Relación de recurrencia lineal
---

# Relación de recurrencia lineal

Una [[Relación de recurrencia]] es ==lineal== cuando todos los términos de la [[Sucesión]] solo están afectados por ==sumas== o ==multiplicaciones por un escalar==.

## Coeficientes no constantes

Cuando los números que acompañan a $a_k$, llamados coeficientes, ==dependen de $n$==, decimos que son coeficientes ==no constantes==.

## Coeficientes constantes

Cuando los números que acompañan a $a_k$ son escalares independientes.

### Homogénea

Cuando ==todos== los términos ==contienen a un término de la sucesión==.

$$
a_n = c_1 a_{n - 1} + c_2 a_{n - 2} + \dots + c_k a_{n - k}
$$

Si $c_k \neq 0$, se dice que es de orden $k$.

#### Teorema 1

Sea una [[Relación de recurrencia lineal]], con $r_1, \dots, r_t$ siendo $t$ raíces distintas de la ==ecuación característica==, con multiplicidades $m_1, \dots, m_t$, sujetas a $\forall i: m_i \geq 1$ y $m_1 + \dots + m_t = k$, donde $k$ es el orden de la ecuación de recurrencia. Luego $a_n$ es solución sí y solo sí:

$$
a_n = P_{m_1 - 1}(n) \cdot r_1^n + P_{m_2 - 1}(n) \cdot r_2^n + \dots + P_{m_t - 1}(n) \cdot r_t^n
$$

Donde $P_{m_j - 1}(n)$ es un polinomio evaluado en $n$ de grado $m_j - 1$, con $m_j$ la [[Multiplicidad algebraica]] asociada a la raíz $r_j$.

### No homogénea

Cuando tiene un [[Término independiente]] $F(n) \neq 0$, es decir, un término que no involucra a ningún término de la sucesión.

$$
a_n = c_1 a_{n - 1} + c_2 a_{n - 2} + \dots + c_k a_{n - k} + F(n)
$$

Si $c_k \neq 0$, se dice que es de orden $k$.

#### Teorema 2
Si $a_n^p$ es una ==solución particular== y $a_n^h$ es la ==solución de la relación homogénea asociada==, luego cualquier solución es de la forma:
$$
a_n = 
