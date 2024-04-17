# Unión
Todos los elementos presentes en dos o más conjuntos, comunes o no. Se representa con la suma ($A+B$).

Para dos conjuntos $A$ y $B$:
$$
A \cup B= C
$$

Es equivalente a la compuerta *OR*, y es representada como:
```mermaid
flowchart LR
    A[A]
    B[B]
    OR["≥1"]
    Z[Z]

    A & B --> OR
    OR --> Z
```