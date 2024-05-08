---
created: 2024-04-24 12:01:08
modified: 2024-05-08 01:33:30
title: Compuerta NOR
---

# Compuerta NOR

Es una [[Compuertas lógicas|compuerta lógica]] que representa a una [[Compuerta OR]] seguida por una [[Compuerta NOT]].

## Representación simbólica

Podemos representarla de forma simbólica, de dos formas:

- $\overline{A + B} = Z$
- $-(A \lor B) = Z$

## Representación gráfica

Podemos representarla de forma gráfica, de dos formas:

```mermaid
flowchart RL
    A[A]
    B[B]
    OR["≥1"]
    Z[Z]

    OR --- A & B
    Z --o OR
```

## Tabla de verdades

Podemos representarla mediante una [[Tabla de verdades]].

| $A$ | $B$ | $A + B$ | $Z = \overline{A + B}$ |
| --- | --- | ------- | ---------------------- |
| 0   | 0   | 0       | 1                      |
| 0   | 1   | 1       | 0                      |
| 1   | 0   | 1       | 0                      |
| 1   | 1   | 1       | 0                      |
