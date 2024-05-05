# Estructura de casos

Un tipo de [[Estructuras de control#De selección]] que ejecuta un 

Se puede representar con [[Pseudocódigo]] o [[Diagrama de flujo]]. Python implementó está estructura en la versión 3.10, pero también se puede hacer algo similar utilizando [[Bifurcaciones]] anidadas con `elif`.

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
