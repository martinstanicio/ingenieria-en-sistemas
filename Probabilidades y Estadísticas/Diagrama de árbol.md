---
aliases:
  - Diagramas de árbol
created: 2025-06-22 16:41:22
modified: 2025-06-22 17:41:27
title: Diagrama de árbol
---

# Diagrama de árbol

Un diagrama de [[Árbol]] es una forma de representar visualmente todas las posibilidades en un [[Experimento]] con [[Eventos mutuamente excluyentes]].

```mermaid
flowchart LR
    A@{ shape: sm-circ }
    Q11@{ shape: text, label: "$$Q_1$$" }
    R11@{ shape: text, label: "$$R_1$$" }
    R12@{ shape: text, label: "$$R_2$$" }
    R13@{ shape: text, label: "$$R_3$$" }
    Q21@{ shape: text, label: "$$Q_2$$" }
    R21@{ shape: text, label: "$$R_1$$" }
    R22@{ shape: text, label: "$$R_2$$" }
    R23@{ shape: text, label: "$$R_3$$" }
    T11@{ shape: text, label: "$$P \\left( Q_1 \\cap R_1 \\right) = P \\left( R_1 \\vert Q_1 \\right) \\cdot P \\left( Q_1 \\right)$$" }
    T12@{ shape: text, label: "$$P \\left( Q_1 \\cap R_2 \\right) = P \\left( R_2 \\vert Q_1 \\right) \\cdot P \\left( Q_1 \\right)$$" }
    T13@{ shape: text, label: "$$P \\left( Q_1 \\cap R_3 \\right) = P \\left( R_3 \\vert Q_1 \\right) \\cdot P \\left( Q_1 \\right)$$" }
    T21@{ shape: text, label: "$$P \\left( Q_2 \\cap R_1 \\right) = P \\left( R_1 \\vert Q_2 \\right) \\cdot P \\left( Q_2 \\right)$$" }
    T22@{ shape: text, label: "$$P \\left( Q_2 \\cap R_2 \\right) = P \\left( R_2 \\vert Q_2 \\right) \\cdot P \\left( Q_2 \\right)$$" }
    T23@{ shape: text, label: "$$P \\left( Q_2 \\cap R_3 \\right) = P \\left( R_3 \\vert Q_2 \\right) \\cdot P \\left( Q_2 \\right)$$" }
    
    
    A --> |"$$P \left( Q_1 \right)$$"| Q11
    A --> |"$$P \left( Q_2 \right)$$"| Q21
    Q11 --> |"$$P \left( R_1 \vert Q_1 \right)$$"| R11 --> T11
    Q11 --> |"$$P \left( R_2 \vert Q_1 \right)$$"| R12 --> T12
    Q11 --> |"$$P \left( R_3 \vert Q_1 \right)$$"| R13 --> T13
    Q21 --> |"$$P \left( R_1 \vert Q_2 \right)$$"| R21 --> T21
    Q21 --> |"$$P \left( R_2 \vert Q_2 \right)$$"| R22 --> T22
    Q21 --> |"$$P \left( R_3 \vert Q_2 \right)$$"| R23 --> T23
```

Luego, si quiero calcular la [[Probabilidad]] de cualquiera de los [[Evento|Eventos]] en las hojas del [[Diagrama de árbol]], solo debo seguir el camino desde el inicio hasta el [[Evento]], multiplicando la [[Probabilidad]] de cada [[Evento]] que pase.

$$
P \left( Q_i \cap R_j \right) = P \left( R_j \vert Q_i \right) \cdot P \left( Q_i \right)
$$
