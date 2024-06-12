---
created: 2024-05-03 17:32:33
modified: 2024-06-11 21:50:53
title: Estructura de casos
---

# Estructura de casos

Un tipo de [[Estructura de selección]] que compara una [[Variables|Variable]] con una serie de *casos*, y ejecuta las instrucciones correspondientes dependiendo del valor de la misma.

Se puede representar con [[Pseudocódigo]] o [[Diagrama de flujo]]. [[Python]] implementó está estructura en la versión 3.10, pero también se puede hacer algo similar utilizando [[Bifurcaciones]] anidadas con `elif`.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
    condicion{variable}
    
    A1[A1]
	A2[A2]
    
    B1[B1]
	B2[B2]
    
    C1[C1]
	C2[C2]
    
	fin([fin])
    
	comienzo --> condicion
	condicion -- constanteA --> A1
	condicion -- constanteB --> B1
	condicion -- constanteC --> C1
	A1 --> A2 --> fin
	B1 --> B2 --> fin
	C1 --> C2 --> fin
```

## Pseudocódigo

![[Pseudocódigo#^estructura-de-casos]]

## Python

En [[Python]] tenemos la posibilidad de especificar múltiples posibles valores dentro de un mismo caso, utilizando `|`.

```python
x = 3

match x:
    case 1:
	    print("El número es 1")
	case 2|3:
	    print("El número es 2 o 3")
	case _:
		print("El número no es ni 1, ni 2, ni 3")
```
