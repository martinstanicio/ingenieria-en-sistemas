---
created: 2024-04-24 11:53:07
modified: 2024-05-08 01:33:30
title: Compuerta NAND
---

# Compuerta NAND

Es una [[Compuertas lógicas|compuerta lógica]] que representa a una [[Compuerta AND]] seguida por una [[Compuerta NOT]].

## Representación simbólica

Podemos representarla de forma simbólica, de dos formas:

- $\overline{A \cdot B} = Z$
- $-(A \land B) = Z$

## Representación gráfica

Podemos representarla de forma gráfica:

```mermaid
flowchart RL
    A[A]
    B[B]
    AND["&"]
    Z[Z]

    AND --- A & B
    Z --o AND
```

## Tabla de verdades

Podemos representarla mediante una [[Tabla de verdades]].

| $A$ | $B$ | $AB$ | $Z = \overline{AB}$ |
| --- | --- | ---- | ------------------- |
| 0   | 0   | 0    | 1                   |
| 0   | 1   | 0    | 1                   |
| 1   | 0   | 0    | 1                   |
| 1   | 1   | 1    | 0                   |
