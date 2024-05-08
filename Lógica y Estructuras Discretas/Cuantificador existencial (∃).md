---
created: 2024-04-19 13:23:27
modified: 2024-05-08 01:33:30
title: Cuantificador existencial (∃)
---

# Cuantificador existencial (∃)

Se utiliza para referirse a **por lo menos uno o más** de los elementos del [[Lógica y Estructuras Discretas/Universo|Universo]] o [[Conjunto]] en el que estamos trabajando. Utiliza el símbolo "$\exists$".

Para que sea verdadero, basta que se cumpla para al menos uno de los elementos del [[Lógica y Estructuras Discretas/Universo|Universo]] del discurso, pero para que sea falso, hay que demostrar que que no se cumple para ninguno de los elementos del mismo.

Por ejemplo:

$$
\exists x: P(x)
$$

Siempre identificando el [[Lógica y Estructuras Discretas/Universo|Universo]] del discurso, por ejemplo:

$$
U: \mathbb{Z}
$$

Por lo tanto podemos establecer esta [[Equivalencia lógica]]:

$$
\exists x \in \mathbb{Z}: P(x) \Leftrightarrow P(x_1) \lor P(x_2) \lor \cdots \lor P(x_n)
$$
