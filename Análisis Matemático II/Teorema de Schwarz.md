---
aliases:
  - Teorema de Clairaut
created: 2025-05-20 14:45:30
modified: 2025-05-20 15:03:42
title: Teorema de Schwarz
---

# Teorema de Schwarz

Si las [[Derivada parcial|Derivadas parciales]] cruzadas o mixtas $f_{xy}$ y $f_{yx}$ son [[Continuidad|Continuas]] en un [[Conjunto abierto]] $S$, entonces ==son iguales== en cada punto de $S$.

```mermaid
flowchart LR
    A["f(x, y)"]
    
    B["f_x"]
    C["f_y"]
    
    D["f_xx"]
    E["f_xy = f_yx"]
    F["f_yy"]
    
    G["f_xxx"]
    H["f_xxy = f_xyx = f_yxx"]
    I["f_xyy = f_yxy = f_yyx"]
    J["f_yyy"]
    
    A --> B & C
    B --> D & E
    C --> E & F
    D --> G & H
    E --> H & I
    F --> I & J
```
