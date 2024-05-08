---
created: 2024-04-24 11:12:45
modified: 2024-05-08 01:33:30
title: Compuerta NOT
---

# Compuerta NOT

Es una [[Compuertas lógicas|compuerta lógica]], actúa como un ==inversor==. Se comporta de forma similar a una [[Negación (-)]] o [[Complemento]].

## Representación simbólica

Podemos representarla de forma simbólica, de tres formas:

- $\overline{Z}$
- $-Z$
- $\lnot Z$

## Representación gráfica

Podemos representarla de forma gráfica.

```mermaid
flowchart RL
    Z[Z]
    NOT["1"]
    NOTZ[-Z]

    NOTZ --o NOT --- Z
```

## Tabla de verdades

Podemos representarla mediante una [[Tabla de verdades]], igual a la de la de una [[Negación (-)]]:

![[Negación (-)#^f39b71]]

| $Z$ | $\bar{Z}$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |
