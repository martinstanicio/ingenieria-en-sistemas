# Unión (OR)

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
    OR["|"]
    Z[Z]

    A & B --> OR
    OR --> Z
```

O también como:

```mermaid
flowchart LR
    A[A]
    B[B]
    OR["≥1"]
    Z[Z]

    A & B --> OR
    OR --> Z
```

## Tabla de verdades

| $A$ | $B$ | $Z=AB=A \lor B$ |
| --- | --- | ---------------- |
| 0   | 0   | 0                |
| 0   | 1   | 1                |
| 1   | 0   | 1                |
| 1   | 1   | 1                |
