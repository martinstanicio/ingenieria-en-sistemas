# Compuerta OR

Es una [[Compuertas lógicas|compuerta lógica]], representada por una ==suma== en el álgebra de Boole. Se comporta igual que una [[Disyunción (∨)]].

## Representación simbólica

Podemos representarla de forma simbólica, de dos formas:

- $A + B = Z$
- $A \lor B = Z$

## Representación gráfica

Podemos representarla de forma gráfica, de dos formas:

```mermaid
flowchart LR
    A[A]
    B[B]
    OR["≥1"]
    Z[Z]

    A & B --- OR
    OR --- Z
```

## Tabla de verdades

Podemos representarla mediante una [[Tabla de verdades]], igual a la de la de una [[Disyunción (∨)]]:

![[Disyunción (∨)#^632ed6]]

| $A$ | $B$ | $Z = A + B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 1           |
| 1   | 0   | 1           |
| 1   | 1   | 1           |
