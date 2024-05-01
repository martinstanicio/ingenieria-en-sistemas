# 20240430 - Bifurcaciones anidadas 2

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

    C3{C3}
	E[E]
	F[F]

    G[G]

	fin([fin])

	comienzo --> C1
	C1 -- Sí --> A --> B --> fin
	C1 -- No --> C2
	C2 -- Sí --> C --> D --> fin
	C2 -- No --> C3
	C3 -- Sí --> E --> F --> fin
	C3 -- No --> G --> fin
```

## Pseudocódigo

```
comienzo

si C1 entonces
    A
    B
sino
    si C2 entonces
        C
        D
    sino
        si C3 entonces
            E
            F
        sino
            G
        fin si
    fin si
fin si

fin
```
