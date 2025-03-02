---
created: 2025-03-01 21:22:29
modified: 2025-03-01 21:40:22
title: Diagrama de estados
---

# Diagrama de estados

Un diagrama que permite representar el flujo de [[Entradas]], [[Salidas]] y [[Lógica y Estructuras Discretas/Estado|Estados]] de una [[Máquina]].

Por ejemplo, el [[Diagrama de estados]] de una lámpara.

```mermaid
stateDiagram
    [*] --> Oscuridad
    Oscuridad --> Oscuridad: OFF
    Oscuridad --> Luz: ON
    Luz --> Oscuridad: OFF
    Luz --> Luz: ON
```
