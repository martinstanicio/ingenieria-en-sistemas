---
aliases:
  - Señal
created: 2024-05-07 21:08:58
modified: 2024-05-08 01:33:30
title: Bandera
---

# Bandera

Se utiliza para saber si la ejecución de un [[Programa propio]] pasó por un cierto punto del código o no. Es decir, es una [[Variables|variable]] que puede ser verdadera o falsa.

Por ejemplo, podemos utilizarla para saber si una de las ramas de una [[Bifurcaciones|bifurcación]] fue ejecutada o no.

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["bandera = 0"]
    
    C1{C1}
    
	bandera[["bandera = 1"]]

    C2{"bandera = 1"}
    C2si{{"Se ejecutó la rama del 'sí' de la birfurcación"}}
    C2no{{"No se ejecutó la rama del 'sí' de la birfurcación"}}

	fin([fin])
    
	comienzo --> variables --> C1
	C1 -- Sí --> bandera --> C2
	C1 -- No --> C2
	C2 -- Sí --> C2si --> fin
	C2 -- No --> C2no --> fin
```
