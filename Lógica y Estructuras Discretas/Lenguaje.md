---
aliases:
  - Lenguajes
created: 2025-02-27 18:41:12
modified: 2025-06-10 21:52:43
title: Lenguaje
---

# Lenguaje

Se llama [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] sobre $\Sigma$ al [[Conjunto]] de [[Lógica y Estructuras Discretas/Cadena|Cadenas]] $L$ tal que $L \subseteq \Sigma^*$, donde $\Sigma^*$ es la [[Cerradura de Kleene]] del [[Alfabeto]] $\Sigma$.

> [!important]
> Un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] es de tipo $i$ si existe una [[Gramática]] de tipo $i$ que lo genera.

Se dice que un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L$ es generado por una [[Gramática]] $G$ si se cumple lo siguiente.

$$
L(G) = \set{ \alpha \in T^*: S \to^+ \alpha }
$$

> [!tip]
> Es decir, que el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L(G)$ generado por la [[Gramática]] $G$ es la [[Cerradura de Kleene]] de los terminales $T^*$, que pueden ser obtenidos luego de aplicar una o más producciones, partiendo del símbolo distinguido $S$.
