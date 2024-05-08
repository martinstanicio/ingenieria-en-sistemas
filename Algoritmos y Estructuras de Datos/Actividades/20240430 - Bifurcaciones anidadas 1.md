---
created: 2024-04-30 21:17:10
modified: 2024-05-08 01:33:31
title: 20240430 - Bifurcaciones anidadas 1
---

# 20240430 - Bifurcaciones anidadas 1

Replicar el diagrama de flujo en pseudocódigo.

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

    E[E]

    C3{C3}
	F[F]
	G[G]

	fin([fin])

	comienzo --> C1
	C1 -- Sí --> A --> B --> C2
	C1 -- No --> E --> C3
	C2 -- Sí --> C --> D
	C2 -- No --> D
	D --> fin
	C3 -- Sí --> F --> fin
	C3 -- No --> G --> fin
```

## Pseudocódigo

```
comienzo

si C1 entonces
    A
    B
    si C2 entonces
        C
    fin si
    D
sino
    E
    si C3 entonces
        F
    sino
        G
    fin si
fin si

fin
```
