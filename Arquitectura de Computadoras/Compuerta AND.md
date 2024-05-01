# Compuerta AND

Es una [[Compuertas lógicas|compuerta lógica]], representada por una ==multiplicación== en el álgebra de Boole. Se comporta de forma similar a una [[Conjunción (∧)]] o [[Intersección (∩)]].

## Representación simbólica

Podemos representarla de forma simbólica, de dos formas:

- $A \cdot B = Z$
- $A \land B = Z$
- $A \cap B = Z$

## Representación gráfica

Podemos representarla de forma gráfica:

```mermaid
flowchart LR
    A[A]
    B[B]
    AND["&"]
    Z[Z]

    A & B --- AND
    AND --- Z
```

## Tabla de verdades

Podemos representarla mediante una [[Tabla de verdades]], igual a la de la de una [[Conjunción (∧)]]:

![[Conjunción (∧)#^fd3490]]

| $A$ | $B$ | $Z = A \cdot B$ |
| --- | --- | --------------- |
| 0   | 0   | 0               |
| 0   | 1   | 0               |
| 1   | 0   | 0               |
| 1   | 1   | 1               |
