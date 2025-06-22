---
created: 2025-06-22 17:51:40
modified: 2025-06-22 17:58:51
title: Teorema de Bayes
---

# Teorema de Bayes

Sean $A_1, A_2, \dots, A_n$ un [[Conjunto]] de [[Eventos mutuamente excluyentes]] y [[Eventos exhaustivos|Exhaustivos]], con [[Probabilidad|Probabilidades]] *previas* $P \left( A_i \right)$. Entonces, para cualquier otro [[Evento]] $B$ para el cual $P \left( B \right) > 0$, la [[Probabilidad]] *posterior* de $A_j$ dado que $B$ ha ocurrido es:

$$
P \left( A_j \vert B \right) =
\frac{P \left( A_j \cap B \right)}{P \left( B \right)} =
\frac{P \left( B \vert A_j \right) \cdot P \left( A_j \right)}{\sum_{i = 1}^n P \left( B \vert A_i \right) \cdot P \left( A_i \right)}
$$

Esto se debe a que $P \left( A_j \cap B \right) = P \left( B \vert A_j \right) \cdot P \left( A_j \right)$, gracias a la definición de [[Probabilidad condicional]], y $P \left( B \right) = \sum_{i = 1}^n P \left( B \vert A_i \right) \cdot P \left( A_i \right)$, gracias a la [[Ley de probabilidad total]].
