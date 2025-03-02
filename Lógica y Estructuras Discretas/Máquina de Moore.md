---
aliases:
  - Máquinas de Moore
created: 2025-03-01 21:38:19
modified: 2025-03-01 21:58:52
title: Máquina de Moore
---

# Máquina de Moore

Una [[Máquina de estados finitos]] donde cada [[Lógica y Estructuras Discretas/Estado|Estado]] está asociado a una única [[Salidas|Salida]].

Por ejemplo, una lámpara, donde $q_1$ es oscuridad y $q_2$ es luz.

```mermaid
stateDiagram
    [*] --> Oscuridad
    Oscuridad --> Oscuridad: Off
    Oscuridad --> Luz: On
    Luz --> Oscuridad: Off
    Luz --> Luz: On
```

| $f$       | On  | Off       |
| --------- | --- | --------- |
| Oscuridad | Luz | Oscuridad |
| Luz       | Luz | Oscuridad |


| $g$       | $O$ |
| --------- | --- |
| Oscuridad |     |
