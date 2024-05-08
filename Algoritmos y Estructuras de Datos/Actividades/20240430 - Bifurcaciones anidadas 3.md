---
created: 2024-04-30 21:51:09
modified: 2024-05-08 01:33:30
title: 20240430 - Bifurcaciones anidadas 3
---

# 20240430 - Bifurcaciones anidadas 3

Replicar el pseudocódigo en un diagrama de flujo.

## Pseudocódigo

```
comienzo

si C1 entonces
    A
    B
    si C2 entonces
        C
        D
        si C3 entonces
            E
            F
        sino
            si C4 entonces
            sino
                G
                H
            fin si
        fin si
        I
        J
    sino
        si C5 entonces
            K
        fin si
    fin si
sino
    L
fin si

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

    C1{C1}
	A[A]
	B[B]

    C2{C2}
	C[C]
	D[D]

    C3{C3}
	E[E]
	F[F]

    C4{C4}

    G[G]
    H[H]

    I[I]
    J[J]

    C5{C5}
    K[K]

	fin([fin])

	comienzo --> C1
	C1 -- Sí --> A --> B --> C2
	C1 -- No --> L --> fin
	C2 -- Sí --> C --> D --> C3
	C2 -- No --> C5
	C3 -- Sí --> E --> F --> I
	C3 -- No --> C4
	C4 -- Sí --> I
	C4 -- No --> G --> H --> I
	C5 -- Sí --> K --> fin
	C5 -- No --> fin
	I --> J --> fin
```
