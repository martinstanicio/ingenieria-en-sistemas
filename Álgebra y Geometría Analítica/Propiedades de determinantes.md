# Propiedades de determinantes

Al momento de utilizar [[Determinante|determinantes]] de [[Matriz|matrices]], existe una serie de propiedades que podemos utilizar.

1. Si $A \in k^{n \times n}$ contiene una línea nula, luego $det(A) = 0$.
2. Sean $A, B \in k^{n \times n}$, si $B$ se obtiene de $A$ multiplicando una de sus líneas por un número $c$,  luego $det(B) = c \cdot det(A)$.
3. Sean $A, B, C \in k^{n \times n}$, si $A$, $B$ y $C$ tienen todas sus líneas idénticas, excepto la línea $ij$-ésima, tal que la línea $ij$-ésima de $C$ es la suma de las líneas $ij$-ésimas de $A$ y $B$, luego el determinante $|C| = |A| + |B|$.
4. Si $B$ se obtiene intercambiando 2 líneas paralelas de $A$, luego $|B| = -|A|$.
5. Si una matriz $A$ contiene 2 líneas paralelas iguales, luego $|A| = 0$.
6. Si una matriz $A$ contiene 2 líneas paralelas múltiplos entre sí, luego $|A| = 0$.
7. Si en $A \in k^{n \times n}$ se reemplaza una línea por la suma de ella más un múltiplo de otra, el determinante de la nueva matriz es igual a $det(A)$.
8. Sea $A \in k^{n \times n}$, $|A| = |A^t|$.
9. Sea $A, B \in k^{n \times n}$, $|A \cdot B| = |A| \cdot |B|$.
10. Si $A \in k^{n \times n}$, y es inversible $\exists A^{-1} \in k^{n \times n}$ tal que $A \cdot A^{-1} = I$, $|A^{-1}| = \frac{1}{|A|}$
