---
aliases:
  - Máquinas de Mealy
created: 2025-03-01 21:39:22
modified: 2025-03-01 21:45:52
title: Máquina de Mealy
---

# Máquina de Mealy

Una [[Máquina de estados finitos]] donde el [[Lógica y Estructuras Discretas/Estado|Estado]] no determina directamente la [[Salidas|Salida]].

Por ejemplo, una máquina expendedora de caramelos de $7, que solo acepta monedas de $2 y $5.

```mermaid
stateDiagram
    [*] --> $0
    $0 --> $2: $2 / Nada
    $0 --> $5: $5 / Nada
    $1 --> $3: $2 / Nada
    $1 --> $6: $5 / Nada
    $2 --> $4: $2 / Nada
    $2 --> $0: $5 / Caramelos
    $3 --> $5: $2 / Nada
    $3 --> $1: $5 / Caramelos
    $4 --> $6: $2 / Nada
    $4 --> $2: $5 / Caramelos
    $5 --> $0: $2 / Caramelos
    $5 --> $3: $5 / Caramelos
    $6 --> $1: $2 / Caramelos
    $6 --> $4: $5 / Caramelos
```
