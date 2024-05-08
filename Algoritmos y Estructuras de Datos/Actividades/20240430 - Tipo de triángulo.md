---
created: 2024-04-30 22:36:38
modified: 2024-05-08 01:33:30
title: 20240430 - Tipo de triángulo
---

# 20240430 - Tipo de triángulo

Se ingresan los 3 lados de un triángulo, mostrar qué tipo de triángulo es según sus lados.

## Pseudocódigo

```
comienzo

declarar ladoA = real, ladoB = real, ladoC = real

leer(ladoA)
leer(ladoB)
leer(ladoC)

si ladoA == ladoB entonces
    si ladoA == ladoC entonces
        mostrar("Equilatero")
    sino
        mostrar("Isosceles")
sino
    si ladoA == ladoC entonces
        mostrar("Isosceles")
    sino
        si ladoB == ladoC entonces
            mostrar("Isosceles")
        sino
            mostrar("Escaleno")
        fin si
    fin si
fin si

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`ladoA = real
	ladoB = real
	ladoC = real`"]
    
	leerA[/ladoA/]
    leerB[/ladoB/]
    leerC[/ladoC/]
    
    si1{ladoA == ladoB}
    
	si2{ladoA == ladoC}
	si2si{{Equilatero}}
	si2no{{Isosceles}}
    
    si3{ladoA == ladoC}
	si3si{{Isosceles}}
    
    si4{ladoB == ladoC}
	si4si{{Isosceles}}
	si4no{{Escaleno}}
    
	fin([fin])
    
	comienzo --> variables --> leerA --> leerB --> leerC --> si1
	si1 -- Sí --> si2
	si1 -- No --> si3
	si2 -- Sí --> si2si --> fin
	si2 -- No --> si2no --> fin
	si3 -- Sí --> si3si --> fin
	si3 -- No --> si4
	si4 -- Sí --> si4si --> fin
	si4 -- No --> si4no --> fin
	
	mostrar --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240430-tipo-de-triangulo.py"
```
