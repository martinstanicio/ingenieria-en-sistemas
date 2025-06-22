---
aliases:
  - Diagramas de árbol
created: 2025-06-22 16:41:22
modified: 2025-06-22 16:47:12
title: Diagrama de árbol
---

# Diagrama de árbol

Un diagrama de [[Árbol]] es una forma de representar visualmente todas las posibilidades en problemas de conteo y [[Probabilidad]].

```mermaid
flowchart LR
    R@{ shape: sm-circ }
    O11@{ shape: text, label: "$$O_1$$" }
    P11@{ shape: text, label: "$$P_1$$" }
    P12@{ shape: text, label: "$$P_2$$" }
    P13@{ shape: text, label: "$$P_3$$" }
    O21@{ shape: text, label: "$$O_2$$" }
    P21@{ shape: text, label: "$$P_1$$" }
    P22@{ shape: text, label: "$$P_2$$" }
    P23@{ shape: text, label: "$$P_3$$" }
    
    R --> |"$$P \left( O_1 \right)$$"| O11
    R --> |"$$P \left( O_2 \right)$$"| O21
    O11 --> |"$$P \left( P_1 \vert O_1 \right)$$"| P11
    O12 --> |"$$P \left( P_2 \vert O_1 \right)$$"| P11
    O13 --> |"$$P \left( P_3 \vert O_1 \right)$$"| P11
```
