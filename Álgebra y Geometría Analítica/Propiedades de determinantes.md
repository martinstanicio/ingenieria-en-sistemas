---
created: 2024-05-05 17:14:13
modified: 2024-07-07 19:37:04
title: Propiedades de determinantes
---

# Propiedades de determinantes

Al momento de utilizar [[Determinante|determinantes]] de [[Matriz|matrices]], existe una serie de propiedades que podemos utilizar.

1. Si $A \in k^{n \times n}$ contiene una línea nula, luego $det(A) = 0$. ^p01
2. Sean $A, B \in k^{n \times n}$, si $B$ se obtiene de $A$ multiplicando una de sus líneas por un número $c$,  luego $det(B) = c \cdot det(A)$. ^p02
3. Sean $A, B, C \in k^{n \times n}$, si $A$, $B$ y $C$ tienen todas sus líneas idénticas, excepto la línea $ij$-ésima, tal que la línea $ij$-ésima de $C$ es la suma de las líneas $ij$-ésimas de $A$ y $B$, luego el determinante $|C| = |A| + |B|$. ^p03
4. Si $B$ se obtiene intercambiando 2 líneas paralelas de $A$, luego $|B| = -|A|$. ^p04
5. Si una matriz $A$ contiene 2 líneas paralelas iguales, luego $|A| = 0$. ^p05
6. Si una matriz $A$ contiene 2 líneas paralelas múltiplos entre sí, luego $|A| = 0$. ^p06
7. Si en $A \in k^{n \times n}$ se reemplaza una línea por la suma de ella más un múltiplo de otra, el determinante de la nueva matriz es igual a $det(A)$. ^p07
8. Sea $A \in k^{n \times n}$, $|A| = |A^t|$. ^p08
9. Sea $A, B \in k^{n \times n}$, $|A \cdot B| = |A| \cdot |B|$. ^p09
10. Si $A \in k^{n \times n}$, y es inversible $\exists A^{-1} \in k^{n \times n}$ tal que $A \cdot A^{-1} = I$, $|A^{-1}| = \frac{1}{|A|}, |A| \neq 0$. ^p10
11. Si se multiplican los elementos de una línea por los adjuntos de otra línea, y se suman los productos, el resultado es $0$. ^p11
12. El determinante de una matriz triangular es el producto de los elementos de su diagonal principal. ^p12
